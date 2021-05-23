import urllib.request as request
import json

print("Please enter the word you want to search..!")
word_to_search=input()
print("the word is: ",word_to_search)
with request.urlopen('https://api.dictionaryapi.dev/api/v2/entries/en_US/'+word_to_search+'') as response:
        source = response.read()
        data = json.loads(source)
print(data[len(data)-1]['meanings'])
