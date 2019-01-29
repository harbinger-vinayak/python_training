
import requests
import sys
import json

try:

    # print 'Exveption throwed'
    # raise SystemError
    share_name = 'BOM531219'
    authkey = 'CZaTnx9DAjD7nTBpVJhV'
    url = 'https://www.quandl.com/api/v3/datasets/BSE/{}.json?api_key={}'.format(share_name, authkey)

    response = requests.get(url)

    if response.status_code != 200:
        sys.exit(1)

    content = json.loads(response.content)
    lastDate = []
    lastValue = []
    for data in (content['dataset']['data'])[:2]:
        lastDate.append(data[0])
        lastDate.append(float(data[5]))
    print lastDate
except Exception as E:
    print E
    print 'My Exception handled'
