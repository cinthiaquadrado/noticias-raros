import requests
from bs4 import BeautifulSoup

url = 'https://www.camara.leg.br/noticias/ultimas'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

wanted_keywords = ['doenças raras', 'doença rara', 'paciente raro']
matching_news = []

news_items = soup.find_all('li', class_='l-lista-noticias__item')

for item in news_items:
    title_element = item.find('h3', class_='g-chamada__titulo')
    if title_element:
        title_text = title_element.a.text.strip()
        link = title_element.a['href']
        for keyword in wanted_keywords:
            if keyword in title_text:
                matching_news.append({'title': title_text, 'link': link})
                break  

for news in matching_news:
    print("Título:", news['title'])
    print("Link:", news['link'])
    print()
