from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

import api_key

class CoinMarketCapAPI:
	url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
	def __init__(self):
		headers = {
			'Accepts': 'application/json',
			'X-CMC_PRO_API_KEY': api_key.key,
		}
	
		self.session = Session()
		self.session.headers.update(headers)
	
	def load_data(self, id_str):
		parameters = {
			'id': id_str,
			'convert':'USD'
		}
		try:
			response = self.session.get(self.url, params=parameters)
			coin_data = json.loads(response.text)
		
		except (ConnectionError, Timeout, TooManyRedirects) as e:
			print(e)
			exit()
		else: 		
			print( "Data loaded successfully from api")
			return coin_data
