# Given
Can you use your knowledge of format strings to make the customers happy?
Download the binary [here](https://artifacts.picoctf.net/c_mimas/67/format-string-0).
Download the source [here](https://artifacts.picoctf.net/c_mimas/67/format-string-0.c).

# Solution
Let's check out the source code, since they gave it to us,
and it might also be good to read up a little bit on [format string vulnerabilities](https://owasp.org/www-community/attacks/Format_string_attack)
too.

Taking a look at the code, we find the single-argument user-input printf issue in the `else` statements in both
`serve_patrick` and `serve_bob`. We also notice that before getting to this point, the program checks that we've
actually given input from the provided menu options.

So, we know a couple things:
1. We have to be typing one of the given options
2. We have to be taking advantage of printf

This doesn't leave us with many options. Only `"Gr%114d_Cheese"` has a % in it, to take advantage of the printf
in `serve_patrick()`

And in `serve_bob`, two options (`Pe%to_Portobello` or `Cla%sic_Che%s%steak`), have % in them, but
%t doesn't line up with any format string flags, so we go with the second option.
This causes the flag to be printed out, before the program throws a segfault:
```
picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_74f6c0e7}
```
