import json
import re

def sol(string):
    sentences = []
    current_sentence = ""

    for char in string:
        if char in [".", "!", "?"]:
            current_sentence += char
            sentences.append(current_sentence.strip())
            current_sentence = ""
        elif current_sentence == "" and char != " ":
            current_sentence += char
        else:
            current_sentence += char

    question_sentences = [sentence for sentence in sentences if sentence.endswith("?")]
    return question_sentences

with open('input.txt') as inputfile:
    string = inputfile.readline()

sentences = sol(string)

with open('output.txt', 'w') as outfile:
    for s in sentences:
        outfile.write(s)
        outfile.write("\n")

