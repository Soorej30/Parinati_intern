from newsapi import NewsApiClient
import requests
import time
import schedule
import datetime
import json
import to_telegram
import to_twitter

class generate_news:
    def __init__(self):
        self.api_key='8eeae742e4f14e9da4712ca86633120e'      
        self.current_time=int(time.time())+19800
        self.from_time=str(datetime.datetime.utcfromtimestamp(self.current_time-60))
        self.to_time=str(datetime.datetime.utcfromtimestamp(self.current_time))        
        self.getnews()

    def getnews(self):
        url1 = requests.get("https://newsapi.org/v2/everything?q=cryptocurrency&from="+self.from_time+"&to="+self.to_time+"&language=en&apiKey=8eeae742e4f14e9da4712ca86633120e")
        news_list=url1.json()
        print(news_list)
        self.post_on_twitter_and_telegram(news_list)

    def post_on_twitter_and_telegram(self,news_list):
        for x in news_list["articles"]:
            to_telegram.telegram_post.post_on_telegram(x)
            to_twitter.twitter_post.post_on_twitter(x)

schedule.every(1).minute.do(generate_news)
while True:
    schedule.run_pending()
    time.sleep(1)