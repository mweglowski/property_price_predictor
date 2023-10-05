import requests
from bs4 import BeautifulSoup

city = 'gdansk'
url = 'https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/{}'.format(city)

response = requests.get(url)

titles = []
prices = []
cards = None

if response.status_code == 200:
  soup = BeautifulSoup(response.text, 'html.parser')
  cards = soup.find_all('div', {'data-cy': 'l-card'})

for card in cards:
  title = card.find('h6').text
  price = card.find('p').text
  price = int(''.join(price[:price.index('z')].split()))
  titles.append(title)
  prices.append(price)

print(sum(prices) / len(prices))
  
