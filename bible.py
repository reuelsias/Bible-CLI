import requests
import sys

arguments = sys.argv
url_base = "https://bible-api.com/"

def request(book, chapter, verse):
    if verse:
        url = url_base + book + chapter + ":" + verse + "?translation=almeida"
    else:
        url = url_base + book + chapter + "?translation=almeida"
        
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data = response.json()
        formatted_verses = [f"{verse['verse']}.{verse['text']}" for verse in data["verses"]]
        for verse in formatted_verses:
            print(verse) 

def main():
    book = input("Book: ")
    chapter = input("Chapter: ")
    verse = input("Verse: ")

    request(book, chapter, verse)

if __name__ == "__main__":
    main()
