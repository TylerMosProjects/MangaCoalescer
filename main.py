import requests
from bs4 import BeautifulSoup

URL = ("https://sailmanga.com")
page = requests.get(URL)

#print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="latest-list")


#print(results.prettify())

titles = soup.find_all('strong')
for title in titles:
    print(title.text)
