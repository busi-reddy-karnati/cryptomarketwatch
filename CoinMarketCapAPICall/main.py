from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'


secret_key = os.environ.get('coinmarketcap_api_key')
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD',
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': secret_key,
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    for i in range(10):
        print(data['data'][i]['name']+" PRICE: "+str(data['data'][i]['quote']['USD']['price'])+" Percent Change(1hr): "+str(data['data'][i]['quote']['USD']['percent_change_1h']))


except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
