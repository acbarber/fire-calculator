import requests
import json
import sys
import os

tax_year = sys.argv[1]
with open('taxee_creds.json','r') as f:
    creds = json.load(f)
state_list = [i.split('.')[0] for i in os.listdir('./state_tax/2019/')]


fed = requests.get(f'https://taxee.io/api/v2/federal/{tax_year}', headers =creds )
print(state_list)
