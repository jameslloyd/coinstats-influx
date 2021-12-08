#boilerplate
import logging
import os
from config import *
config = Config() # config.py
#end boilerplate
#influx
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

#influx
from scraper import get_coinstats

def main():
    #do stuff
    logging.basicConfig(format=config.LOG_FORMAT ,level=config.LOG_LEVEL)
    logging.info('Started application {} in {}'.format(config.APPNAME, config.ENV))
    currencies = config.CURRENCIES
    who = config.COINSTATSURLS

    with InfluxDBClient(url=config.INFLUX_HOST, token=config.INFLUX_TOKEN, org=config.INFLUX_ORG) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)
    #    james = get_coinstats('https://coinstats.app/p/Gq6UAd','GBP')
        for w in who:
            for c in currencies:
                coinstats = get_coinstats(who[w],c)
                point = Point("portfolio").tag("who", w).tag("currency", c).field("value", coinstats[0]).time(datetime.utcnow(), WritePrecision.NS)
                write_api.write(config.INFLUX_BUCKET, config.INFLUX_ORG, point)

if __name__ == '__main__': 
    main()