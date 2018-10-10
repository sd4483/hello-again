from difflib import SequenceMatcher
from difflib import get_close_matches
import json
data = json.load(open("data.json"))
w = input("Enter word: ")
def mydict(word):
    word = word.lower()
    close_match = get_close_matches(word, data.keys(), n=1)
    if word in data: 
        return data[word]
    elif len(close_match) != 0:
        for match in close_match:
            return data[match]
    else:
        return "The word doesn't exist, please double check it!"
print(mydict(w))