from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve

def soupme(url):
	page = urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')
	return soup

season = 2019

url = "https://www.hockey-reference.com/leagues/NHL_{}_games.html".format(season)
soup = soupme(url)
table_div = soup.find(id="div_games")
table = table_div.find_all('tr')
# table = table_div.find('table')
print(table[1])