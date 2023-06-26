import requests
from bs4 import BeautifulSoup
import html2text
import openai
import os
import sys

url_base = "https://en.wikipedia.org/wiki/"
openai.api_key = os.getenv("OPEN_API_KEY")
base_prompt = "Play as a G,PG,PG13, R or explicit rater for wikipedia pages. Format your response with Rating: \n Reasoning: "


def getWikiPage(page):
    response = requests.get(url=url_base+page)
    soup = BeautifulSoup(response.content,'html.parser')
    paragraphs = soup.findAll('p')
    return [ html2text.html2text(paragraph.text) for paragraph in paragraphs]

def rate(text):
    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'system', "content": base_prompt}, {'role': 'user', 'content': text}],
        temperature=0
    )
    return result

def concatText(paragraphs):
    i=0
    wordCount=0
    result=""
    while i<len(paragraphs) and wordCount<500:
        result = result+'\n'+paragraphs[i]
        wordCount = wordCount+len(paragraphs[i].split())
        i=i+1
    return result


def main(argv):
    paragraphs = getWikiPage(argv)
    text = concatText(paragraphs)
    print(rate(text))


if __name__ == "__main__":
    main(sys.argv[1])