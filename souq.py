import json

import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

titles=[]
images=[]
dates=[]
locations=[]

result = requests.get("https://www.eventbrite.com/d/az--tempe/events--this-weekend/.json")

sre = result.content

soup= BeautifulSoup(sre,"lxml")

title= soup.find_all("div",{"class":"eds-event-card__formatted-name--is-clamped eds-event-card__formatted-name--is-clamped-three eds-text-weight--heavy"})
date = soup.find_all("div",{"class":"eds-evet-card-content__sub-title eds-text-color--ui-orange eds-l-pad-bot-1 eds-l-pad-top-2 eds-text-weight--heavy eds-text-bm"})
location=soup.find_all("div",{"class":"card-text--truncated__one"})


file_list=(titles,dates,locations)
expand=zip_longest(*file_list)

for i in range(len(title)):
    titles.append(title[i].text)

    dates.append(date[i].text)
    locations.append(location[i].text)

with open('SouqDataappl.csv', "w") as myfile:
        wr = csv.writer(myfile)
        wr.writerow(["title", "date", "location"])
        wr.writerows(expand)



