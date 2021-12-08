import os

class Config(object):
    ENV = 'DEV'
    APPNAME = 'coinstats scaper'
    CURRENCIES = ['GBP','USD']
    COINSTATSURLS = {'<some name>':'<some coinstats portfolio url>'} # e.g. {'bob':'https://coinstats.app/p/Gq6UAw'}
    LOG_FORMAT = os.getenv("LOG_FORMAT") or '%(asctime)s - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(levelname)s - %(message)s' # https://docs.python.org/3/howto/logging.html#changing-the-format-of-displayed-messages
    LOG_LEVEL = 'DEBUG' # change to CRITICAL to shut up script
    INFLUX_HOST = '<your ip & port>' # e.g. 192.168.1.1:8086
    INFLUX_TOKEN = '<your influx token>'
    INFLUX_ORG = '<your influx org>'
    INFLUX_BUCKET = '<your influx bucket>'
