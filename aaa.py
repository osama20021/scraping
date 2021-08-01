import json
from urllib.request import urlopen

with urlopen("https://sis.ou.edu/ted/home/byOther?stat_code=ID&sbgi_code=004114&trns_subj_code=&trns_subj_crse=") as response:
   source=response.read()

#print(source)

data= json.load(source)

print(json.dumps(data, indent=2))

