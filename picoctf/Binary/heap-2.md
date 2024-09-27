# Given
Can you handle function pointers?
Download the binary [here](https://artifacts.picoctf.net/c_mimas/49/chall).
Download the source [here](https://artifacts.picoctf.net/c_mimas/49/chall.c).

# Solution
Starting off by trying the same stuff we've done before doesn't really get us anywhere.
So, let's take a look at the code.
Asking to print out the flag calls the function `check_win()` which then does this:
```
void check_win() { ((void (*)())*(int*)x)(); }
```
Sort of strange looking if you're not familiar with it, and even I'm not fully familiar with it, 
but I know enough C to guess that this is a function pointer.
That means, it's taking the value of x, interpreted as a pointer, and running whatever "function" x
is pointing to.

So now we just have to find the right function, and get its address.

Conveniently, there is this function above, with a very helpful comment:
```
void win() {
    // Print flag
    char buf[FLAGSIZE_MAX];
    FILE *fd = fopen("flag.txt", "r");
    fgets(buf, FLAGSIZE_MAX, fd);
    printf("%s\n", buf);
    fflush(stdout);
    exit(0);
}
```
which is great. But initially, I had no idea how to figure out what the address of this function is.
I know that it's stored in the "text" section of a binary, so I tried `strings chall` but unfortunately that
only printed out the names of functions, and no info about their addresses. A quick search led me to `nm`, which
printed out all the functions and their addresses, and gave me `0x4011a0` for the address of `win()`.

Unfortunately, I have no idea how to print out arbitrary bytes within the netcat client, so I had to do something like this
to get the bytes in there:
```
echo -e '2\n01234567890123456789012345678901\xa0\x11\x40\n4\n' | nc mimas.picoctf.net 54266
```
the 'e' option on echo lets it convert those `\x__` bytes to characters when it prints them out. 
I pre-selected option 2 to fill out the buffer, put in our 32 bytes, and then put in the bytes of the address in
reverse order, because of little-endianness (which I believe is generally the default). Then, my input string
also pre-queues the "print the flag" option, and then pipes all of this as input to the netcat command.

This successfully prints out the flag:
```
picoCTF{and_down_the_road_we_go_dde41590}
``` 
