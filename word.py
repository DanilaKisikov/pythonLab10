import json

import requests


def getNewWord(jsonText):
    my_json = json.loads(jsonText)

    jsonObject = my_json[0]

    name = jsonObject["word"]

    phonetics = jsonObject["phonetics"][0]["text"]

    definitions = jsonObject["meanings"][0]["definitions"]

    meaning = ""
    example = ""
    def_len = len(definitions)
    for i in range(def_len):
        definition = definitions[i]
        if "example" in definition.keys():
            example = definition["example"]
            meaning = definition["definition"]
            break

        elif i == def_len:
            meaning = definitions[0]["definition"]
            example = "No example has been founded"

    word = Word(name, phonetics, meaning, example)

    return word


def getResponse(this_word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + this_word

    response = requests.get(url).text

    my_word = getNewWord(response)

    print(my_word.name)
    print(my_word.example)
    print(my_word.meaning)
    print(my_word.phonetic)

    return my_word


class Word:

    def __init__(self, name, phonetic_text, meaning, example):
        self.name = name
        self.phonetic = phonetic_text
        self.meaning = meaning
        self.example = example
