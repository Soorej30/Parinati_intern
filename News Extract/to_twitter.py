from twitter import *

class twitter_post:
    def post_on_twitter(news_to_print):
        access_token = "1135801629138022400-mL5MNQbONIDH7WnlqY99NPctpOrSLK"
        access_token_secret = "jRxyhSVaPE6ag0hEkux5cM57Ed5rFG7n2ucn76c9hKG5l"
        consumer_key = "GdZVh0VORYpshq5En0yALqqiN"
        consumer_secret = "74badK5fPOkiyIuAXrrDGZGBNRubhWMxyoI5nKtDuUl22QLUqh"

        t=Twitter(auth=OAuth(access_token,access_token_secret,consumer_key,consumer_secret))

        t.statuses.update(status=news_to_print["title"]+' '+news_to_print["url"])