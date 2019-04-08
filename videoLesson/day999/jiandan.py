

import requests
from bs4 import BeautifulSoup

response = requests.get("http://jandan.net/")
print(response.text)


soup = BeautifulSoup(response.text)
content = soup.find_all(name="div", attrs={'id': 'content'})






