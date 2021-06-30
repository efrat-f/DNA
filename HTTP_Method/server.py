import json
import operator
from itertools import islice

from flask import Flask, Response, request

app = Flask(__name__)

wordCounter = {}


@app.route("/sanity")
def sanity():
    return Response("Server up and running")


# get word in params(or null)
@app.route("/word", methods=["GET"])
def get_word():
    word = request.args.get("word")
    word2 = ''.join(e for e in word if e.isalpha()).casefold()
    count = wordCounter.get(word2)
    if count is None:
        count = 0
    return Response(json.dumps({"count": count}))


# get body with json with word field
@app.route("/word", methods=["POST"])
def add_word():
    word = request.get_json().get("word")
    if word:
        word2 = ''.join(e for e in word if e.isalpha()).casefold()
        count = wordCounter.get(word2)
        if count is None:
            count = 0
        wordCounter[word2] = count + 1
        return Response(json.dumps({"text": f"Added {word2}", "currentCount": count + 1}))


# get body with json with sentence field
@app.route("/words", methods=["POST"])
def add_words():
    num_old_words = 0
    sentence = request.get_json().get("sentence")
    for word in sentence.split():
        word2 = ''.join(e for e in word if e.isalpha()).casefold()
        count = wordCounter.get(word2)
        if count is None:
            count = 0
        else:
            num_old_words += 1
        wordCounter[word2] = count + 1
    num_new_words = len(sentence.split())
    return Response(
        json.dumps({"text": f"Added {num_new_words} words, {num_old_words} already existed", "currentCount": -1}))


@app.route("/total", methods=["GET"])
def get_total():
    return Response(json.dumps({"text": "Total count", "count": sum(wordCounter.values())}))


# get body with json with word field
@app.route("/word", methods=["DELETE"])
def delete_word():
    word = request.get_json().get("word")
    word2 = ''.join(e for e in word if e.isalpha()).casefold()
    if word2 not in wordCounter:
        return Response("word does not exists")
    wordCounter.pop(word2)
    return Response(json.dumps({"deleted": word2}))


# get body with json with word and new_word fields
@app.route("/word", methods=["PUT"])
def update_word():
    word = request.get_json().get("word")
    word2 = ''.join(e for e in word if e.isalpha()).casefold()
    new_word = request.get_json().get("new_word")
    new_word2 = ''.join(e for e in new_word if e.isalpha()).casefold()
    if word2 not in wordCounter:
        return Response("word does not exists")
    wordCounter[new_word2] = wordCounter.pop(word2)
    return Response(json.dumps({"updated": new_word2}))


@app.route("/popular", methods=["GET"])
def get_popular_word():
    if wordCounter == {}:
        return Response("there are no words")
    max_v = max(wordCounter.items(), key=operator.itemgetter(1))
    return Response(json.dumps({"text": max_v[0], "count": max_v[1]}))


@app.route("/ranking", methods=["GET"])
def get_populars_word():
    if wordCounter == {}:
        return Response("there are no words")
    sort_dict = dict(sorted(wordCounter.items(), key=lambda item: item[1])[::-1])
    if len(sort_dict) < 5:
        return Response(json.dumps({"ranking ": sort_dict}))
    return Response(json.dumps({"ranking ": dict(islice(sort_dict.items(), 5))}))


if __name__ == '__main__':
    app.run(port=3000)
