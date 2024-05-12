#misc
# Description
I got this flag, but it seems to be encoded in a format called "PEM".

```
-----BEGIN FLAG-----  
aGUyMDI0e2hleC1hLWRlY2ltYWx9  
-----END FLAG-----  
```
## Hint
[CyberChef](https://gchq.github.io/CyberChef)

# Solution
Let's try to decode it in cyberchef by searching what there is available with the keyword PEM.
There's a PEM to Hex
![](../Screenshots/Pasted%20image%2020240331095919.png)

Using that gives us, as expected a Hex value. Let's try to get the value from Hex to it's raw value with the *From Hex* recipe
![](../Screenshots/Pasted%20image%2020240331100114.png)
\

And we've got the flag `he2024{hex-a-decimal}`