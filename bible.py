import requests
import re

url_api = "https://bible-api.com"
actual_reference = None
translation = None

def menu():
    while True:
        print(f'Actual Translation: {translation}\n(1) Get new reference\n(2) Next Chapter\n(3) Previous Chapter\n(4) Change Translation')
        option = int(input(":"))
        if option == 1: set_reference() 
        elif option == 2: next_chapter()
        elif option == 3: previous_chapter()
        elif option == 4: set_translation()
        else: break

def set_reference():
    global actual_reference
    global translation
    pattern = r"^[1-3]?\s?[A-Za-zÀ-ÖØ-öø-ÿ]+(?:\s[A-Za-zÀ-ÖØ-öø-ÿ]+)*\s\d+:\d+$"
    reference = input("Type the biblical reference (ex: Genesis 1:1): ")
    
    if re.match(pattern, reference):    
        url = f'{url_api}/{reference}?translation={translation}'
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            data = response.json()
            print(data)

            actual_reference = reference
            print(reference)
        else:
            print("Invalid reference")
    else:
        print("Invalid format.")
        set_reference()

def set_translation():
    global translation
    url = f'{url_api}/data'
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data = response.json().get("translations", [])
        print("Translactions: ")
        print("\n".join(f"{t['identifier']} - {t['name']}" for t in data))
        translations = [t['identifier'] for t in data]

        translation = input("Select the desired translaction: ")
        
        while translation not in translations:
            print("Invalid Translation")
            translation = input("Select the desired translaction: ")

def next_chapter():
    pass

def previous_chapter():
    pass

def main():
    set_translation()
    menu()

if __name__ == "__main__":
    main()
