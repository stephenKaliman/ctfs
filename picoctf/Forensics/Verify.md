People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.
You can download the challenge files here:
- [challenge.zip](https://artifacts.picoctf.net/c_rhea/10/challenge.zip)

# Solution
Again, not much of forensics, but whatever.

Basically, you can do this even if you have no idea what's going on with checksums.
1. Test out the decrypt script, on its own, and it tells you it wants a filename
2. Test it on a file (i.e. checksum) and it'll tell you `This flag is fake! Keep looking!`
3. So, we write a loop for it to decrypt all the files, and then we can get the flag out of there
```
for filename in files/* do
  ./decrypt.sh "$filename";
done > decrypted.txt 2>&1
```
- The for loop does what it looks like
- the `> decrypted.txt` redirects standard output to the specified file
- the `2>&1` merges the output from stream 2 (the standard error output stream) with stream 1 (the standard input stream, which is now going directly into `decrypted.txt`)

run `grep "picoCTF" decrypted.txt` and we get the flag:
```
picoCTF{trust_but_verify_c6c8b911}
```
