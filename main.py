#!/bin/env/python3
import logging
import os
from time import sleep

from nautapy.nauta_api import NautaClient, NautaProtocol
from requests.exceptions import ConnectionError

# Define config variables
WAIT_TIME = int(os.environ.get('NW_WAIT_TIME', 60))
NAUTA_USER = os.environ.get('NW_NAUTA_USER')
NAUTA_PASSWORD = os.environ.get('NW_NAUTA_PASSWORD')

# define logging level
LOG_LEVEL = os.environ.get('NW_LOG_LEVEL', 'WARNING')
date_strftime_format = "%y/%m/%d %H:%M:%S"
message_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=getattr(logging, LOG_LEVEL.upper(), logging.WARNING),
                    format=message_format,
                    datefmt=date_strftime_format)

client = NautaClient(NAUTA_USER, NAUTA_PASSWORD)

if __name__ == '__main__':
    logging.info(f'Starting nauta-watchdog using {WAIT_TIME} seconds loop')

    if not NAUTA_USER or not NAUTA_PASSWORD:
        logging.error('Nauta username or password not defined. Use NW_NAUTA_USER and NW_NAUTA_PASSWORD environment variables')
        exit(1)

    while True:
        logging.debug('Staring iteration')

        if not NautaProtocol.is_connected(timeout=30):
            logging.debug('Not connected')
            try:
                logging.debug('Connecting')
                client.login()
                logging.debug('Successfully connected')
            except ConnectionError as e:
                logging.warning(e)
            except Exception as e:
                logging.error(e)
        else:
            logging.debug('Connected')

        logging.debug(f'Waiting {WAIT_TIME} seconds for next iteration')
        sleep(WAIT_TIME)
