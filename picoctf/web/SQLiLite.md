# Given
Can you login to this website?
Additional details will be available after launching your challenge instance.

# Solution
Try a basic injection, like typing in `admin' OR 1=1;--` into the username slot.
Looks like this works, it says we got logged in and the flag is "in plain sight".
Checking inspect element, it's in a hidden element:
```
picoCTF{L00k5_l1k3_y0u_solv3d_it_ec8a64c7}
```

And just in case we didn't get a good injection on the first try, it does show us what our final query was.
