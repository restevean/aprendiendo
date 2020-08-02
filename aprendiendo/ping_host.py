# Probando cosas que veo en Internet
from requests import get, exceptions

def ping_host():
    try:
        get('http://google.com', timeout = 3)
        print('connected')
    except exceptions.ConnectionError:
        print('not connected')

ping_host()