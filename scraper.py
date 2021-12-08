import requests
import logging
import random
from bs4 import BeautifulSoup
import string
from datetime import datetime, time
import os
from re import sub
from decimal import Decimal

def random_query():
    letters = string.ascii_letters
    query = ''.join(random.choice(letters) for i in range(random.randint(3,10)))
    param = ''.join(random.choice(letters) for i in range(random.randint(3,10)))
    output = '?' + param + '=' + query
    return(output)

def GET_UA():
    uastrings = [
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",\
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",\
                    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",\
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36",\
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",\
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
                ]
    return random.choice(uastrings)

def get_soup(url,cookies,randomness = True):
    useragent = GET_UA()
    headers = {'User-Agent': useragent}
    if randomness:
        url = url + random_query()
    logging.info("requesting {}".format(url))
    r = requests.get(url, headers=headers, cookies=cookies)
    if r.status_code == 200:
        return BeautifulSoup(r.text, 'html.parser')
    else:
        return False

def currencytofloat(currency):
    return (Decimal(sub(r'[^\d.]', '', currency)))

def get_coinstats(url,currencysymbol):
    soup = get_soup(url,{'CURRENCY_SYMBOL': currencysymbol })
    if soup:
        balance = soup.findAll("span", attrs={"class" : "main-price"})
        return ([currencytofloat(balance[0].contents[0]),currencysymbol])
    else:
        return False