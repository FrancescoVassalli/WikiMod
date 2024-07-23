import requests
from bs4 import BeautifulSoup
import html2text

url_base = "https://en.wikipedia.org/wiki/"
def getWikiPage(page):
    response = requests.get(url=url_base+page)
    soup = BeautifulSoup(response.content,'html.parser')
    paragraphs = soup.findAll('p')
    return [ html2text.html2text(paragraph.text) for paragraph in paragraphs]


