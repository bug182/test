'''
#testing 'or' with 'if' statements
answer = input('y/n: ')

def test(a):
    if a.lower() == 'y' or a.lower() == 'n':
        print('THIS WORKS!!!')
    else:
        print('THIS STILL WORKS!!!')


test(answer)
#testing web usement

import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.tamswithmark.com/shows/anything-goes-beaumont-1987/')
soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.findAll('tr', {"class": "upcoming_performance"})
'''
