
import requests
import logging
import sys
import json

logging.basicConfig(format='%(levelname)-10s: %(message)s', filename='webApi.log', filemode='w', level=logging.DEBUG)

share_name = 'BOM531219'
authkey = 'fKXsYh9Qi9ySbS8X6pNh'
url = 'https://www.quandl.com/api/v3/datasets/BSE/{}.json?api_key={}'.format(share_name, authkey)

logging.debug('Complete url is: {}'.format(url))
response = requests.get(url)
logging.debug(response.content)

if response.status_code != 200:
    logging.error('Error: response type{}'.format(response))
    sys.exit(1)

content = json.loads(response.content)
logging.info('Company Name: {}'.format(content['dataset']['name']))

for data in content['dataset']['data']:
    print data[0], float(data[5])
