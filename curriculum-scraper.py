from bs4 import BeautifulSoup
import requests
import csv


filename="curriculum.csv"

csv_file=open(filename, 'w')
writer=csv.writer(csv_file, delimiter=';')
writer.writerow(['DERS ADI', 'KREDİ'])

source=requests.get('https://cs.ku.edu.tr/undergraduate/ug-curriculum/').text
soup=BeautifulSoup(source, 'lxml')
donem=0
for box in soup.findAll('div', class_='tab-list'):
    donem+=1
    writer.writerow([str(donem)+".DÖNEM"])
    table=box.find('table', class_='course-information').tbody
    for coursebox in table.findAll('tr'):
        info=coursebox.findAll('td')
        name=info[0].text
        credit=info[3].text
        
        writer.writerow([name, credit])
        
    writer.writerow("\n")
    
csv_file.close()