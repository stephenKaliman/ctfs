# Given
This vault uses ASCII encoding for the password. The source code for this vault is here: 
[VaultDoor4.java](https://jupiter.challenges.picoctf.org/static/09d3002ae349631324a17e2255ae8df2/VaultDoor4.java)

# Solution

A few things to note:
- The first line of numbers in the java code are decimal
- The second line is hex
- the third appears to be base 8
  - In python, we need to change those leading 0's to `0o`
- the final line is just characters in their regular character form

Python's `chr()` method turns numbers back into characters, regardless of their input format.
This little script gives us the answer:
```
nums = [
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o143, 0o61 ,
            '9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e' ,
        ]
chars = [chr(num) for num in nums[:-8]]
chars += nums[-8:]
print("".join(chars))
```

flag:
```
picoCTF{jU5t_4_bUnCh_0f_bYt3s_c194f7458e}
```
