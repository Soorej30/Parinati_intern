import time
import requests
import json
from influxdb import InfluxDBClient
import threading

class data:
    def __init__(self,start_time,end_time):
        self.start_time=str(start_time)
        self.end_time=str(end_time)


    def getdata(self,currency='BTC'):
        urlused="https://test.deribit.com/api/v2/public/get_last_trades_by_currency_and_time?currency="+currency+"&start_timestamp="+self.start_time+"&end_timestamp="+self.end_time+"&count=1000"
        print(urlused)
        data_received=requests.get(urlused)
        pydata=data_received.json()
        print(pydata)
        
        total_liquidation=0

        for trade in pydata["result"]["trades"]:
            if "liquidation" in trade:
                total_liquidation+=trade["amount"]

        return total_liquidation

    def savedata(self,total,currency):
        client = InfluxDBClient(host='localhost', port=8086)
        client.switch_database('liquidation')
        json_body=[
             {
                "measurement": "liqdata",
                
                "time": time.ctime(int(self.start_time)),
                "fields":{
                    "end_time": time.ctime(int(self.end_time)),  
                    "Total_liquidation": total,  
                    "Currency": currency            
                }
        }]
        
        client.write_points(json_body)
        
currency=input()
while True:
    start_time=int(time.time())
    end_time=start_time-60
    dt=data(start_time,end_time)
    tot=dt.getdata(currency)
    dt.savedata(tot,currency)

    timeused=int(time.time())-start_time
    time.sleep(60-timeused)


