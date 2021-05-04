#Importacion de librerias
import json
from difflib import get_close_matches

#lectura del archivo JSON
data = json.load(open("data.json"))

#definicion de la funcion translate
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

#input para ingresar la palabra        
word = input("Enter word: ")

#resultado del programa
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)