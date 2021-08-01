import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv


result = requests.get("https://sis.ou.edu/ted/home/byOther?stat_code=MA&sbgi_code=003087&trns_subj_code=&trns_subj_crse=")



soup= BeautifulSoup(result.text ,"lxml")



table=soup.find('table',{'summary':'other matches'})


headers=[]

for i in table.find_all('th'):
    title=i.text.strip()
    headers.append(title)

df=pd.DataFrame(columns=headers)

for row in table.find_all('tr')[1:]:
    data=row.find_all('td')
    row_data=[td.text.strip()for td in data]
    length=len(df)
    df.loc[length]=row_data


with open('SouqDataappl.csv', "w") as myfile:
     wr = csv.writer(myfile)
     wr.writerow(["headers"])
     wr.writerows(expand)
