# Given
Can you solve this?
What two positive numbers can make this possible: `n1 > n1 + n2 OR n2 > n1 + n2`

# Solution
So, obviously this is possible with negative numbers. But it's asking for positive numbers.

Immediate cue that somehow our positive numbers must be turning into negative numbers in the backend,
i.e. integer overflow. If you're not familiar with this, look into [two's complement representation](https://en.wikipedia.org/wiki/Two%27s_complement).

The first natural guess is that we're dealing with 32-bit 2's complement integers, so I'll enter
2^31-1 and 1, to get the overflow.
Typing in these numbers:
```
2147483647 1
```

gives us the flag:
```
picoCTF{Tw0_Sum_Integer_Bu773R_0v3rfl0w_f6ed8057}
```
