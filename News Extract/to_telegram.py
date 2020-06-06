import time
import schedule
import requests

class telegram_post:
    def post_on_telegram(bot_message):
    
        bot_token = '826894897:AAFudHyoYX3VgghruQW48KAieJO7trN6DbA'
        bot_chatID= "-320443975"
        send_text = 'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+bot_chatID+'&parse_mode=Markdown&text='+bot_message["title"]+' '+bot_message["url"]
        response = requests.get(send_text)
