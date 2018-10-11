from difflib import get_close_matches
import json

data = json.load(open("data.json"))     #loasing data
w = input("Enter word: ")               #getting input from the user

def mydict(word):
    word = word.lower()                 #making the input lower case to match it with words in data
    
    """if the entered word has a typo, this checks for a close match"""
    close_match = get_close_matches(word, data.keys(), cutoff=0.8,n=1) 

    if word in data:                    #checks if the entered word is in data
        return data[word]               #returns the meaning for entered word
    elif word.upper() in data:          #this checks for acronyms like USA or NATO
        return data[word.upper()]
    elif word.title() in data:          #this checks for nouns like Delhi, Singapore, etc
        return data[word.title()]       #returns the noun if it is found
    elif len(close_match) != 0:         #if the word is not is data, this executes, this is where close match object comes in handy
        
        """this asks the user, if the close match is what the user intended to enter"""
        match_check = input("Did you mean {} instead? Enter Y if yes, or N if no:\n" .format(close_match[0])) 

        if match_check.lower() == "y": 
            return data[close_match[0]] #if the user types y, this executes, else the following executes
        elif match_check.lower() == "n":
            return "The word doesn't exist, please double check it"
        else:
            return "Please enter only Y OR N"
    else:
        return "The word doesn't exist, please double check it!"

"""This is to clean the output and display it in as a formatted sentence"""
output = mydict(w) 
if type(output) == list:
    for i in output:
        print (i) 
else:
    print (output)

