import nltk
from nltk.corpus import words
import random

nltk.download('words')
word_list = words.words()

def generate_random_word():
    while True:
        word = random.choice(word_list)
        if len(word) == 5:
            return word

random_word = generate_random_word()
print("Random 5-letter word:", random_word)
