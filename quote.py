import random

file = "data/quotes.txt"
quotes = open(file, "r", encoding="utf-8").readlines() # use builtin readlines

def reload():
    quotes = open(file, "r", encoding="utf-8").readlines()

def getQuote() -> str:
    return random.choice(quotes).strip()