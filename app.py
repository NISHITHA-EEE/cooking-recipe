import json


data = json.load(open('recipies.py'))

keys = data.keys()

def get_recipi(word):
    word=word.title()
    if word in data:
         return data[word]
    else:
         return 'unknown recipe please try again'

food_item = input('what do you want to eat?')

print(get_recipi(food_item))