# Given
This vault uses some complicated arrays! 
I hope you can make sense of it, special agent. 
The source code for this vault is here: 
[VaultDoor1.java](https://jupiter.challenges.picoctf.org/static/29b91e638ccbd76aaa8c0462d1c64d8d/VaultDoor1.java)

# Solution
Just like the warmup, this one takes in user input and trims off "picoCTF{" from the front and "}" from the back,
and then checks that the remaining string is equal to something else.

This one does that equality checking character-by-character,
and we can easily convert `checkPassword` into a Python script that prints out the flag for us, like this:
```
password = list(" "*32)
password[0]  = 'd'
password[29] = '3'
password[4]  = 'r'
password[2]  = '5'
password[23] = 'r'
password[3]  = 'c'
password[17] = '4'
password[1]  = '3'
password[7]  = 'b'
password[10] = '_'
password[5]  = '4'
password[9]  = '3'
password[11] = 't'
password[15] = 'c'
password[8]  = 'l'
password[12] = 'H'
password[20] = 'c'
password[14] = '_'
password[6]  = 'm'
password[24] = '5'
password[18] = 'r'
password[13] = '3'
password[19] = '4'
password[21] = 'T'
password[16] = 'H'
password[27] = 'f'
password[30] = 'b'
password[25] = '_'
password[22] = '3'
password[28] = '6'
password[26] = 'f'
password[31] = '0'
print("".join(password))
```
<details>
  <summary>(Some block editing tips)</summary>
  
  >  Most modern text editors allow you to type in multiple places at once by `Alt` + Clicking on the spots where you want to edit. This gives you multiple cursors that all do the same thing. 

  >  Similarly, you can `Alt`+`Shift`+ click and drag to get your cursor in the same spot across multiple lines, and even highlight over some blocks

  >  Another helpful tool for this which isn't exclusive to block-editing is that `Ctrl`+ left/right arrow keys (respectively) 
    skips to the start/end of the previous/next alphanumeric string OR special character string 
 
  >  This is often useful to keep your cursor lined up when different lines have the same structure, but perhaps different length words/numbers/etc
</details>

Giving us the answer:
```
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0}
```
