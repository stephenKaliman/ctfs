# Given
What was I last working on? I remember writing a note to help me remember...
You can download the challenge files here:
- [challenge.zip](https://artifacts.picoctf.net/c_titan/162/challenge.zip)

# Solution
- We open up the zip file, and it seems like it's a git repo with 1 txt file.
- Opening this txt file, they tell us to check the commit history.
- You can look through the files, or just use grep for "picoCTF"
- As one might expect, the flag is in COMMIT_EDITMSG:
```
picoCTF{t1m3m@ch1n3_e8c98b3a}
```
