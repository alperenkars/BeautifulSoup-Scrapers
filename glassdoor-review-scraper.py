# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 14:44:59 2022

@author: sachr
"""



from bs4 import BeautifulSoup
import requests
import csv


filename="glassdoor1.csv"

csv_file=open(filename, 'w')

headers=['pros', 'cons', 'rate']
# csv_file.writelines(["title  link text \n"])
writer=csv.writer(csv_file, delimiter=";")
writer.writerow(headers)

source = requests.get('https://www.glassdoor.com/Reviews/Robert-Bosch-Reviews-E3353.htm').text
soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('li', attrs={"class":"noBorder empReview cf pb-0 mb-0"}):
    pros=article.find('span', attrs={"data-test":"pros"}).text.strip()
    cons=article.find('span', attrs={"data-test":"cons"}).text.strip()
    rate=article.find('span', attrs={"class":"ratingNumber mr-xsm"}).text.strip()
# body=soup.find('body')
    writer.writerow([pros, cons, rate])

csv_file.close()
# for container in body.findAll('span', {"data-test": 'pros'}):