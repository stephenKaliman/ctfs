# Given
This vault uses an XOR encryption scheme. The source code for this vault is here: 
[VaultDoor6.java](https://jupiter.challenges.picoctf.org/static/cdb33ffba609e2521797aac66320ec65/VaultDoor6.java)

# Solution
So the code is taking our input string, character by character,
XOR'ing each character with the byte `0x55`, and comparing the resulting
byte to the hard-coded corresponding byte in the code.

Since XOR inverts itself, we can write a quick script to get back the correct string
from the byte array in the code:
```
nums = [
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x6c, 0x60, 0x37, 0x30, 0x60, 0x31, 0x36,
        ]
chars = [chr(num^0x55) for num in nums]
print("".join(chars))
```
And the flag is:
```
picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_95be5dc}
```
