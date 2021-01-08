from googlesearch import search
from os import system

while True:
    word = input("keyword: ")
    results = search(word, num_results=30)
    print(results)
