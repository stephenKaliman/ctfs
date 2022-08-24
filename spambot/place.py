from register import register
from login import login
from submit import submit

def place(userid):
    register(userid)
    _id = login(userid)
    for i in [1,2,3]:
        submit(_id, i, userid)


place("user13DX")
for i in range(26,513):
    userid = f"user{i}"
    place(userid)
