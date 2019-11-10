import random

def getQuote():
    file = "data/quotes.txt"
    quotes = open(file, "r", encoding="utf-8").read().split("\n")
    return random.choice(quotes)