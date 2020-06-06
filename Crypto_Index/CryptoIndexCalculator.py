class CryptoIndexCalculator:
	index_value =0
	def calc_index(self, coin_data):
		total_market_cap=0
		index_value =0
		json_list = []
		for i in coin_data["data"]:
			total_market_cap+=coin_data["data"][i]["quote"]["USD"]["market_cap"]
		for i in coin_data["data"]:
			market_cap_weight = coin_data["data"][i]["quote"]["USD"]["market_cap"] / total_market_cap
			json_body = [{
			        "measurement": coin_data['data'][i]['name'].replace(" ",""),
				"time": coin_data["status"]["timestamp"]  ,      
			        "fields": {"Coin Weight": market_cap_weight}
			}]
			json_list.append( json_body)
			index_value += market_cap_weight* coin_data["data"][i]["quote"]["USD"]["price"]
		self.index_value = index_value
		json_body = [{
		        "measurement": 'index_value',
			"time": coin_data["status"]["timestamp"]  ,      
		        "fields": {"Value": index_value}
		}]
		json_list.append( json_body)
		return json_list
