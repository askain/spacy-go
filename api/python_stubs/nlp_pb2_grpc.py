# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import python_stubs.nlp_pb2 as nlp__pb2


class NlpStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LoadModel = channel.unary_unary(
                '/nlp.Nlp/LoadModel',
                request_serializer=nlp__pb2.TextRequest.SerializeToString,
                response_deserializer=nlp__pb2.TextResponse.FromString,
                )
        self.NlpProcess = channel.unary_unary(
                '/nlp.Nlp/NlpProcess',
                request_serializer=nlp__pb2.TextRequest.SerializeToString,
                response_deserializer=nlp__pb2.ParsedNLPRes.FromString,
                )
        self.DocSimilarity = channel.unary_unary(
                '/nlp.Nlp/DocSimilarity',
                request_serializer=nlp__pb2.TextSimilarityRequest.SerializeToString,
                response_deserializer=nlp__pb2.TextSimilarity.FromString,
                )


class NlpServicer(object):
    """Missing associated documentation comment in .proto file"""

    def LoadModel(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NlpProcess(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DocSimilarity(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NlpServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LoadModel': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadModel,
                    request_deserializer=nlp__pb2.TextRequest.FromString,
                    response_serializer=nlp__pb2.TextResponse.SerializeToString,
            ),
            'NlpProcess': grpc.unary_unary_rpc_method_handler(
                    servicer.NlpProcess,
                    request_deserializer=nlp__pb2.TextRequest.FromString,
                    response_serializer=nlp__pb2.ParsedNLPRes.SerializeToString,
            ),
            'DocSimilarity': grpc.unary_unary_rpc_method_handler(
                    servicer.DocSimilarity,
                    request_deserializer=nlp__pb2.TextSimilarityRequest.FromString,
                    response_serializer=nlp__pb2.TextSimilarity.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nlp.Nlp', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Nlp(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def LoadModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nlp.Nlp/LoadModel',
            nlp__pb2.TextRequest.SerializeToString,
            nlp__pb2.TextResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NlpProcess(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nlp.Nlp/NlpProcess',
            nlp__pb2.TextRequest.SerializeToString,
            nlp__pb2.ParsedNLPRes.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DocSimilarity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nlp.Nlp/DocSimilarity',
            nlp__pb2.TextSimilarityRequest.SerializeToString,
            nlp__pb2.TextSimilarity.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
