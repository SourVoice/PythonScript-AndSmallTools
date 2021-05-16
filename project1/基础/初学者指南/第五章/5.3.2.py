import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    target = 'https://www.ncxsl.com/book/2/2320.html'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html, 'html.parser')
    div = bf.find_all('div', class_="yd_text2")
    print(div[0].text)
