import sys
import os
import grpc
import time
import spacy
import utils
from python_stubs import nlp_pb2
from python_stubs import nlp_pb2_grpc

from spacy.matcher import Matcher

from concurrent import futures


class NlpService(nlp_pb2_grpc.NlpServicer):
    def __init__(self):
        self.modelName = None
        self.nlp = None
        self.matcher = None

    def LoadModel(self, request, context):
        self.modelName = request.text
        self.nlp = spacy.load(request.text)
        response = nlp_pb2.TextResponse()
        response.message = "Model loaded '{}'".format(request.text)
        return response

    def NlpProcess(self, request, context):
        doc = self.nlp(request.text)
        response = utils.doc2proto(doc, self.modelName)
        return response

    def DocSimilarity(self, request, context):
        docA = self.nlp(request.texta)
        docB = self.nlp(request.textb)
        response = nlp_pb2.TextSimilarity()
        response.similarity = docA.similarity(docB)
        return response

    def AddRule(self, request, context):
        if self.matcher == None:
            self.matcher = Matcher(self.nlp.vocab)
        matcher_id = request.id
        patterns = [{pat.key: pat.value} for pat in request.patterns]
        self.matcher.add(matcher_id, None, patterns)
        response = nlp_pb2.TextResponse()
        response.message = "Rule with id '{}' added to matcher.".format(matcher_id)
        return response

    def RemoveRule(self, request, context):
        if self.matcher == None:
            return nlp_pb2.TextResponse(message="No rules exists with matcher")
        self.matcher.remove(request.text)
        return nlp_pb2.TextResponse(
            message="Rule with id '{}' removed from matcher.".format(request.text)
        )

    def GetRule(self, request, context):
        if self.matcher == None:
            return nlp_pb2.TextResponse(message="No rules exists with matcher")
        _, patterns = self.matcher.get(request.text)
        return nlp_pb2.Rule(
            id=request.text,
            patterns=[
                nlp_pb2.Pattern(key=list(pat.keys())[0], value=list(pat.values())[0])
                for pat in patterns[0]
            ],
        )

    def GetMatches(self, request, context):
        doc = self.nlp(request.text)
        matches = self.matcher(doc)
        reponse = nlp_pb2.Matches(
            matches=[nlp_pb2.Match(id=str(i[0]), start=i[1], end=i[2]) for i in matches]
        )
        return reponse

    def ResetMatcher(self, request, context):
        self.matcher = None
        return nlp_pb2.TextResponse(message="Matcher object reset successful.")    


def serve(server_address):

    # private_key_path = os.path.join(
    #     os.environ["GOPATH"], "src/github.com/yash1994/spacy-go/server.key"
    # )
    # certificate_chain_path = os.path.join(
    #     os.environ["GOPATH"], "src/github.com/yash1994/spacy-go/server.crt"
    # )

    # if not os.path.exists(private_key_path):
    #     private_key_path = "server.key"

    # if not os.path.exists(certificate_chain_path):
    #     certificate_chain_path = "server.crt"

    # with open(private_key_path, "rb") as f:
    #     private_key = f.read()
    # with open(certificate_chain_path, "rb") as f:
    #     certificate_chain = f.read()

    # server_credentials = grpc.ssl_server_credentials(
    #     ((private_key, certificate_chain,),)
    # )

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    nlp_pb2_grpc.add_NlpServicer_to_server(NlpService(), server)
    # server.add_secure_port(server_address, server_credentials)
    server.add_insecure_port(server_address)
    server.start()
    try:
        while True:
            time.sleep(10000)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        server_address = "localhost:50051"
        print("Default Server Address: {}".format(server_address))
    else:
        server_address = sys.argv[1]
        print("Custom Server Address: {}".format(server_address))

    serve(server_address)
