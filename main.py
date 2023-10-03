import requests
from bs4 import BeautifulSoup

city = 'gdansk'
url = 'https://www.olx.pl/nieruchomosci/mieszkania/{}'.format(city)

response = requests.get(url)

titles = []
cards = None

if response.status_code == 200:
  soup = BeautifulSoup(response.text, 'html.parser')
  cards = soup.find_all('div', {'data-cy': 'l-card'})

for card in cards:
  title = card.find('h6').text
  titles.append(title)

print(len(titles))

