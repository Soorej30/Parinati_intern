from influxdb import InfluxDBClient

class InfluxDatabase:
	def __init__( self, db_name, host = 'localhost', port=8086, username = 'root', password= 'root' ):
		self.client = InfluxDBClient(host, port, username, password, db_name )
		self.client.create_database(db_name)

	def update_database(self, json_list):
		for i in json_list:
			self.client.write_points(i)
		print('Database updated successfully!!')

	def print_database(self):
		result = self.client.query( 'show measurements;')
		result = result.get_points()
		result = list( result)
		for temp in result:
			print( temp['name'].replace(" ","") + ':')
			query_string = 'select * from ' + temp['name'].replace(" ","") + ';'
			print(self.client.query(query_string))
			print()
		
		
