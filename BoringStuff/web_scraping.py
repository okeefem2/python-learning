import requests
import sys
import bs4

# game = sys.argv[1]
game = 'nerts-card-game'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
response = requests.get('https://gamerules.com/rules/' + game, headers=headers)

response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, 'html.parser')

descriptionItems = soup.select('.entry-content > p')

for item in descriptionItems:
    print(item.text)
