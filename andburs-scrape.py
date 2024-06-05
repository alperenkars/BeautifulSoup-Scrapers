from bs4 import BeautifulSoup
import requests
import csv

filename="andburs-scrape.csv"
f=open(filename, 'w')

# csv_file.writelines(["title  link text \n"])
writer=csv.writer(f, delimiter=";")


source=requests.get('https://anadolubursiyerleri.ku.edu.tr/program-hakkinda-neler-dediler/2020-bursiyerleri/').text
soup=BeautifulSoup(source, 'lxml')

for article in soup.findAll('tr'):
    # print(article,"\n")
    
    name=article.findAll('td')[0].text.strip()
    bursveren=article.findAll('td')[1].text.strip()
    school=article.findAll('td')[2].text.strip()
    city=article.findAll('td')[3].text.strip ()
    major=article.findAll('td')[4].text.strip()
    
   
    writer.writerow([name, bursveren, school, city, major])
    # f.write( bursveren+" "+school+" "+city+" "+major)
    # f.write( bursveren+" "+school+" "+city+" "+major)
    # f.write("\n")
    
    
f.close()