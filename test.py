import requests 
import time

api_key = "9c8eb388-12c2-4bdf-8e72-250e5c6a1c2a"
bot_key = "5464096807:AAFylK-XhUy_sU7K1pmshe3U7gtklMUO1m8"
chat_id = "5267116310"
limit = 5000
time_interval = 120*60

def get_price():
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    
    parameters ={
        "start":"1",
        "limit":"2",


    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url,headers=headers, params=parameters).json()
    btc_price = response["data"][0]["quote"]["USD"]["price"]
    return btc_price
    return response

print(get_price())


def send_update(chat_id,msg):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)

def main():
    while True:

        price = get_price()
        print(price)
    

        if price < limit:
            send_update(chat_id, f"Price of bitcion is down!: {price}")
    
        time.sleep(time_interval)

main()








