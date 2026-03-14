from bs4 import BeautifulSoup
import requests
url ="https://quotes.toscrape.com/page/2/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('small', class_='author')
quotes_2 = soup.find_all('span', class_='text')
print(response.status_code)
for quote in quotes:
     print(quote.get_text(strip=True)) 
for quote_2 in quotes_2:
    print(quote_2.get_text(strip=True))