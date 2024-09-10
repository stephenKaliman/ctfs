# Given:
I made a program to solve a problem, but it seems too slow :(
Download the program [here](https://artifacts.picoctf.net/c_titan/19/flag_printer.py).
Download the message [here](https://artifacts.picoctf.net/c_titan/19/encoded.txt).

So, first thing I did was take a look at the code. Basically, it does the following:
0. establish a modulus m = 7514777789 (which is prime, so probably not too much to dig into there)
  1. Save the galois field `GF = galois.GF(m)` -- good thing m is (a power of a) prime
1. Take the input as a list of ordered pairs `(x_1, y_1)...(x_n, y_n)`
2. Save a vector called `solution`, which is `GF(y%m)`
3. Save a square `n x n` matrix called `matrix`, whose (one-indexed) `(i,j)`th entry is `GF(x_i^{j-1}%m)`
4. Find the solution to the linear system of matrix and solution.

Some notes:
- Since `m` is prime, this field luckily just looks like the integers mod m.
- Some quick testing of the galois module tells me that since this field is just the ring of integers mod m, GF(m) isn't really doing anything fancy, just basically returning the
  same number back, but "as a field element"
- GF(0) is going to be the 0 element, which means that since x_1=0, the entire first row of `matrix` is just going to be all 0's.
