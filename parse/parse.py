#Здесь происходит парсинг

import requests#Запрос - ответ
from bs4 import BeautifulSoup as BS#Библиотека для парсинга

class Parse():
    def __init__(self, url):
        self.url = url
        self.values = []
        source =  requests.get(self.url)#Извлекаем данные из саита
        self.html = BS(source.text, 'lxml')#Текст

    def get_content(self):
        table = self.html.find('table', {'id': 'courses-main'})#all table
        tbody = table.find('tbody')

        for tr in tbody.find_all('tr'):
            td = tr.find_all('td',{'class':''})
            for value in td:
                if value.text != '':
                    self.values.append(value.text.lstrip())  

        self.values = self.values[4:]
        return self.values
