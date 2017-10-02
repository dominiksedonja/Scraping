from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import random

x = 0

url = "http://quotes.yourdictionary.com/theme/marriage/"
response = urlopen(url).read()
soup = BeautifulSoup(response)
vsi_citati = soup.findAll("p", {"class": "quoteContent"})

izbrani_citati = random.sample(vsi_citati, 5)

for citat in izbrani_citati:
    x += 1
    print str(x) + ". " + citat.string