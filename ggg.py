import pandas as pd
import json
url = "https://sis.ou.edu/ted/home/byOther?stat_code=ID&sbgi_code=004114&trns_subj_code=&trns_subj_crse="
df = pd.read_html(url)[0]


print(df)




for item in df['TransferSubject']:
    print(item)

with open("sample.json", "w") as outfile:
    outfile.write(str(item))



