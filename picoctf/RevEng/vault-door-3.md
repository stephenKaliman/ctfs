# Given
This vault uses for-loops and byte arrays. The source code for this vault is here: 
[VaultDoor3.java](https://jupiter.challenges.picoctf.org/static/a648ca6dd275b9454c5d0de6d0f6efd3/VaultDoor3.java)

# Solution
We can easily undo the scrambling in python, by reversing the assignments:
```
encoded = list("jU5t_a_sna_3lpm18gb41_u_4_mfr340")
decoded = list(" "*len(encoded))
decoded[:8] = encoded[:8]
for i in range(8,16):
    decoded[23-i] = encoded[i]
for i in range(16,32,2):
    decoded[46-i] = encoded[i]
for i in range(17,32,2):
    decoded[i] = encoded[i]
print("".join(decoded))
```

This tells us that they flag is:
```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}
```
