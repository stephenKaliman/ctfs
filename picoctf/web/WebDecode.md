# Given
After starting up the instance, the problem says:
Do you know how to use the web inspector?
Start searching here to find the flag

(not including the link since it is only generated once the instance is started)

# Solution:
The challenge and prompt give away 2 things:
1. The flag will probably be Base64 encoded, since this is the normal encoding used for web/urls
2. The flag is going to be hidden probably as a comment or something similar within the page source

- Opening up inspect element, there isn't really anything of note on the home page -- the HTML lines up exactly with what we see,
  and the CSS files have nothing of note. The font names have some gibberish in them, but they don't decode to anything via Base64
- The About page has an interesting-looking logo which after zooming in appears to be a picture of some sort of black cloth.
  but there doesn't immediately appear to be any extra information there, so we move on within the About page
- The section tag within "about.html" has an out-of-place looking attribute called "notify-true" with value `cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMWY4MzI2MTV9`

Base64 decoding this (with a tool such as [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false))) gives us the flag:
```
picoCTF{web_succ3ssfully_d3c0ded_1f832615}
```
