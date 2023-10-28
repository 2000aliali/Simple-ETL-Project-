import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.jumia.ma/catalog/?q=redmi&page='

columns = {'name': [], 'price': [], 'img url': []}

for page in range(1, 15):
    print('---', page, '---')
    r = requests.get(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")

    anchor = soup.find('div', {'class': '-paxs row _no-g _4cl-3cm-shs'}).find_all('article', {'class': 'prd _fb col c-prd'})

    for pt in anchor:
        img = pt.find('a').find('div', {'class': 'img-c'}).find('img', {'class': 'img'})

        name = pt.find('a').find('div', {'class': 'info'}).find('h3', {'class': 'name'})

        price = pt.find('a').find('div', {'class': 'info'}).find('div', {'class': 'prc'})

        columns['name'].append(name.text)
        columns['price'].append(price.text)
        columns['img url'].append(img.get('data-src'))

data = pd.DataFrame(columns)
data.to_csv('XIAOMI_Redmi_products.csv', index=False)  # Save as a CSV file


