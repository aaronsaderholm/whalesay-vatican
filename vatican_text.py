# Scrapes The Vatican Assassin Lorem Ipsum page 
# for the lorem ipsum quotes within:

# http://vaticanassass.in

from bs4 import BeautifulSoup
import urllib.request

url = "http://vaticanassass.in/index.php"

attempts = 0
quote = None

# Occasionally the Vatican Ipsum pages comes back with nothing.

while attempts < 10:
	page = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(page, 'html.parser')

	quote = soup.find(id="copytext").get_text()
	if quote:
		break

	attempts += 1
	continue
	
print(quote.rstrip())
