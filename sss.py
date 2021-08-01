import requests
from bs4 import BeautifulSoup
import csv
import json


class TableScraper:
    results = []

    def fetch(self, url):
        return requests.get(url)

    def parse(self, html):
        content = BeautifulSoup(html, 'lxml')
        table = content.find('table')
        rows = table.findAll('tr')
        self.results.append([header.text for header in rows[0].findAll('th')])

        for row in rows:
            if len(row.findAll('td')):
                self.results.append([data.text for data in row.findAll('td')])

    def to_csv(self):
        with open('table.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(self.results)

    def to_json(self):
        with open('table.json','w') as json_file:
            writer=json.dumps(json_file)
            writer.writerows(self.results)

    def run(self):
        response = self.fetch("https://sis.ou.edu/ted/home/byOther?stat_code=ID&sbgi_code=004114&trns_subj_code=&trns_subj_crse=")
        self.parse(response.text)
        #self.to_csv()
        self.to_json()



if __name__ == '__main__':
    scraper = TableScraper()
    scraper.run()