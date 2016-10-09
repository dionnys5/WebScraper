import urllib
import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen("https://twitter.com/TheEconomist")
twitterEconomist = BeautifulSoup(page,"html.parser")
for tweets in twitterEconomist.findAll('li',{'data-item-type':'tweet'}):
    texto = tweets.find('p').text
    print(texto)
