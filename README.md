# spaCy-Go

This is an insecured, lightweighted version of [yash1994' spaCy-Go](https://github.com/yash1994/spacy-go).

> ☢ `lightweight` means Doc returns only tokens.
>
> The other functions like `doc.ents`, `doc.sents` are commented-out.
>
> Check `api/utils.py`.

And also extended network timeout for better stability.

<br>

Tested on
- python 3.8
- go1.20.6

<br>

### Install GO client

```bash
go get -v "github.com/askain/spacy-go"
```

<br>

### Run python gRPC server

```bash
pip install -r requirements.txt

python -m spacy download en_core_web_sm

python api/server.py
```

<br>

### Use GO client

```Go
package main

import (
	"fmt"

	spacygo "github.com/askain/spacy-go"
)

func main() {

	// load language model
	var modelName string = "en_core_web_sm"
	r, err := spacygo.Load(modelName)

	if err != nil {
		return
	}

	fmt.Printf("%v \n", r.GetMessage())

	// annotate text
	var text string = "I propose to consider the question, 'Can machines think?"

	doc, err := spacygo.Nlp(text)

	// print annotated info : part-of-speech
	for i, token := range doc.GetTokens() {
		fmt.Printf("token %v '%v' part-of-speech tag: %v \n", i, token.GetText(), token.GetPos())
	}

	// calculate text similarity
	var texta string = "I like apples"
	var textb string = "I like oranges"

	textSimilarity, err := spacygo.Similarity(texta, textb)

	fmt.Printf("text similarity between %v and %v is %v", texta, textb, textSimilarity.GetSimilarity())
}
```

<br>

Run your own module.

Run the gRPC server before this or your command will be stuck.

```bash
go run yourfile.go
```

<br>

Run your main function but temporary disable Spacy-Go.

It is OK not to run the gRPC server.

```bash
USE_SPACYGO=0 go run yourfile.go
```