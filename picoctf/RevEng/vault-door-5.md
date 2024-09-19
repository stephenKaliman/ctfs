# Given
In the last challenge, you mastered octal (base 8), decimal (base 10), 
and hexadecimal (base 16) numbers, but this vault door uses a different 
change of base as well as URL encoding! The source code for this vault is here: 
[VaultDoor5.java](https://jupiter.challenges.picoctf.org/static/0a53bf0deaba6919f98d8550c35aa253/VaultDoor5.java)


# Solution
Thanks to very readable code, we don't even need to write a script for this one.
The hard-coded expected string has been url-encoded, and then base64 encoded.
So, we can just put it through the reverse in [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)URL_Decode()&ieol=CRLF)
to get the flag:

```
picoCTF{c0nv3rt1ng_fr0m_ba5e_64_0b957c4f}
```
