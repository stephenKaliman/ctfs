# Given
Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. 
The laboratory is protected by a series of locked vault doors. 
Each door is controlled by a computer and requires a password to open. 
Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, 
but one of our junior agents obtained the source code for each vault's computer! 
You will need to read the source code for each level to figure out what the password is for that vault door. 
As a warmup, we have created a replica vault in our training facility. 
The source code for the training vault is here: 
[VaultDoorTraining.java](https://jupiter.challenges.picoctf.org/static/1afdf83322ee9c0040f8e3a3c047e18b/VaultDoorTraining.java)

# Solution
The flag is pretty clear from just a skim of the code, but to be thorough, 
here's a breakdown of what the code does in pseudocode:
```
class VaultDoorTraining{
  main:
    print("Enter vault password")
    collect user input
    trim off the length of "picoCTF{" from the start of the input, and trim one character from the end
    if(checkPassword(input)):
      print("Access Granted")
    else:
      print("Access Denied")
  checkPassword(input):
    true if input = "w4rm1ng_Up_w1tH_jAv4_eec0716b713"
    false otherwise
```

So clearly, the vault password (and thus the flag) is
```
picoCTF{w4rm1ng_Up_w1tH_jAv4_eec0716b713}
```
