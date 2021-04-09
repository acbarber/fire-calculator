import requests
import json
import sys
import os

with open('taxee_creds.json','r') as f:
    creds = json.load(f)

tax_year = sys.argv[1]
state_list = [i.split('.')[0] for i in os.listdir('./state_tax/2019/')]

# Get fed tax json for given year and save it
fed = requests.get(f'https://taxee.io/api/v2/federal/{tax_year}', headers =creds )
with open(f'./federal_tax/{tax_year}/fed.json', 'w') as f:
    json.dump(fed.json(), f)

# Get state tax json for given year and save it
for state in state_list:
    r = requests.get(f'https://taxee.io/api/v2/state/{year}/{state}', headers =creds )
    with open(f'./state_tax/{year}/{v}.json', 'w') as f:
        json.dump(r.json(), f)

# TODO: Get fica tax json for given year and save it (probably have to web scrape)
