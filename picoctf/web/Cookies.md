# Given
Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:27177/

# Solution
I started by trying stuff out in devtools, specifically focusing on the cookies (under the application tab)
thanks to the challenge name.
The only cookie that appears is a "name" cookie which has value -1 when the form hasn't yet been submitted.
When I type in "snickerdoodle", the suggested prompt, this cookie's value turns to 0.
Ok, interesting.
Trying "chocolate chip" gives a value of 1, and "peanut butter" gives a value of 5.
Doesn't seem like there's much here. 

Unfortunately, trying to add cookies, like "admin=true" or "user=admin" was useless, so I went back to the cookies.

It seemed like somehow each cookie was getting a number.
Opened up Burpsuite to see how the number was getting generated, and it seemed like the form first went to an endpoint,
was then converted to a number, and then the number was forwarded to the "check" page which generated the final response.
I sent the intermediate form, which looked like this:
```
GET /check HTTP/1.1
Host: mercury.picoctf.net:27177
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://mercury.picoctf.net:27177/
Accept-Encoding: gzip, deflate, br
Cookie: name=1
Connection: keep-alive
```
to the repeater.
Trying a very large # like 100 generated an error response saying "not a valid cookie". 
Trying values one at a time, working up from 0, eventually generated a response with the flag:
```
picoCTF{3v3ry1_l0v3s_c00k135_064663be}
```
