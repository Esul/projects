import requests
import json
from random import randint


def get_temp(city):
    """
    Return Temperature in the specified city
    """
    city = city.lower().capitalize()
    token = 'aqac-iqneboda-tqveni-tokeni'

    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city, token))
    temp = response.json()
    return temp['main']['temp']


def random_cat_fact():
    """
    Gets random cat facts from the web
    """
    facts = open("cat_facts.txt", "r", encoding="utf-8")
    all_facts = json.load(facts)
    facts.close()

    return str(all_facts["all"][randint(0, len(all_facts["all"]))]["text"])


def bored():
    """
    Gets random activity
    """

    response = requests.get('https://www.boredapi.com/api/activity/')
    activity = response.json()
    return activity['activity']


def get_crypto_value(crypto_id):
    """
    Get crypto value
    """
    url = 'https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd'.format(crypto_id)
    response = requests.get(url)
    price = response.json()
    return price[f'{crypto_id}']['usd']
