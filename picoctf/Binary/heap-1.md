# Given
Can you control your overflow?
Download the binary [here](https://artifacts.picoctf.net/c_tethys/1/chall).
Download the source [here](https://artifacts.picoctf.net/c_tethys/1/chall.c).

# Solution
After connecting, it looks about the same, but following the same procedure doesn't give us the flag.
Let's take a look at the source code.
```
...
void check_win() {
    if (!strcmp(safe_var, "pico")) {
        printf("\nYOU WIN\n");
...
```
So, it looks like we have to change safe_var to "pico", and we can just do this by appending "pico"
to the end of our input from the last heap challenge. 
This gives us the flag:
```
picoCTF{starting_to_get_the_hang_79ee3270}
```
