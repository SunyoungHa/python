import encodings
from urllib import request
from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://movie.daum.net/ranking/reservation"
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
lists=soup.find_all('div', class_="thumb_cont")


with open('movie.csv', 'w', encoding='utf8',newline='') as csvfile:
    thewriter=writer(csvfile)
    header=['Title', 
    'Score' ]
    thewriter.writerow(header)

    for list in lists:
        movie_title=list.find('a',class_='link_txt').text.replace('\n','')
        score=list.find('span', class_="txt_append").text.replace('\n','')

        info=[movie_title,  score ]
        thewriter.writerow(info)
