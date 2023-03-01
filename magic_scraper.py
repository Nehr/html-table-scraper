import requests
from bs4 import BeautifulSoup

URL = "https://scryfall.com/sets/one"
page = requests.get(URL)

FILE_NAME = 'magic_set.txt'

soup = BeautifulSoup(page.content, "html.parser")

#results = soup.find("div", class_="card-grid")

first_card_set = soup.find("div", class_="card-grid")

i = 0
cards = first_card_set.find_all("a", class_="card-grid-item-card")

with open(FILE_NAME, 'w') as f:
    for card in cards:
        i += 1
        card_name = card.find_all("span", class_="card-grid-item-invisible-label")
        card_name_h = card_name[-1].text.strip()
        print(f'card name: {card_name[-1].text.strip()}, {str(i)}/{str(len(cards))}')
        f.write(card_name_h + "\n")
f.close()


print('done')
