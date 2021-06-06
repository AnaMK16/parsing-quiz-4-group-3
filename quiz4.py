from bs4 import BeautifulSoup
import requests
import csv
from time import sleep
from random import randint


f = open('Top_Movies.csv', 'w',encoding='utf-8_sig', newline = '\n')
file_obj = csv.writer(f)
file_obj.writerow(['Title','Runtime','Genre','Ranking'])


h = {'Accept-Language':'en-US'}
page = 1

url = 'https://www.imdb.com/list/ls005337232/?st_dt=&mode=detail&page=1&sort=list_order,ascstart= ' +str(page)

while page < 6:
    r = requests.get(url, params=h)
    #print(r)
    c = r.text
    soup = BeautifulSoup(c,'html.parser')
    sec = soup.find('div', class_='lister list detail sub-list')
    movies = sec.find_all('div', class_ = 'lister-item mode-detail')
    
    for each in movies:
        title =  each.h3.a.text
        runtime = each.find('span',class_='runtime').text
        genre = each.find('span',class_='genre').text.strip()
        rating = each.find('span',class_='ipl-rating-star__rating').text

        file_obj.writerow([title,runtime,genre,rating])
        print(title)
        
    
    page += 1
    sleep(randint(10,15))


