'''
Author: Dionnys Santos Marinho
@date 09/27/2016
'''

import urllib
import urllib.request
from bs4 import BeautifulSoup

url = "https://twitter.com/UOL"
WebPage = urllib.request.urlopen(url)
soup = BeautifulSoup(WebPage,"html.parser")
print("Tweet Scraping...")
with open("UolTweets.txt","w") as f:
    for tweets in soup.findAll('div',{"class":"content"}):
        t = tweets.find('p').text
        f.write(t+"\n")
print("Done!")
f.close()
