import requests
from bs4 import BeautifulSoup

url = "https://www.gdut.edu.cn/"

response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

links = soup.find_all('a')


print(response.status_code)

for link in links:
    href = link.get("href")
    print(href)

