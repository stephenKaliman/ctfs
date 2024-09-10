# Given:
YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzJhMnd6TW1zeWZRPT0nCg==

The `==` at the end tells me this is Base64, so we can decode it to this:

# Step 1:
b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ=='

Again, the `==` tells me this is still Base64 and the `b'...'` looks like the bytes form of strings in python, so we can just take out what's inside those single quotes.
Decoding gives us:

# Step 2:
wpjvJAM{jhlzhy_k3jy9wa3k_86kl32k2}

which, considering the capitals and the `picoCTF{...}`  flag format, this is pretty clearly just a caesar cipher. Passing it through a decoder with the right offset gives:

# Solution:
picoCTF{caesar_d3cr9pt3d_86de32d2}
