from bs4 import BeautifulSoup as bs
import requests as rq

resp = rq.get('https://sites.google.com/a/sogyo.nl/intranet/boerderij')
print(resp)
print(resp.text)