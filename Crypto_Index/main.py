from CryptoIndexCalculator import CryptoIndexCalculator
from InfluxDatabase import InfluxDatabase 
from CoinMarketCapAPI import CoinMarketCapAPI 
import json
import time

f = open( 'index.json', 'r')
index_meta_data = json.load(f)
index_api = CoinMarketCapAPI()
calc = CryptoIndexCalculator()
database_obj_list = []

for index_name in index_meta_data:
	database_obj_list.append(InfluxDatabase(index_name, 'localhost', 8086, 'root', 'root'))

while True:
	num=0
	for index_name in index_meta_data:
		index_coins_id_list = index_meta_data[index_name]
		coin_data = index_api.load_data( str(index_coins_id_list).replace('[', '').replace(']','').replace(' ',''))
		json_list = calc.calc_index( coin_data)
		database_obj_list[num].update_database( json_list)
		database_obj_list[num].print_database()
		num+=1
	time.sleep( 3600)

