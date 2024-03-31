#crypto 
# Description
You found some strange symbol in an old monastery. Can you make any sense out of it?
![monastery.jpg](../Screenshots/monastery.png)
\

## Hint
After decoding the symbols, combine them to one single number, and do two more conversions.

# Solution
First let's see if a search on *monastery cipher* yields anything.
One of the results is a page to Wikipedia for [Cistercian numerals](https://en.wikipedia.org/wiki/Cistercian_numerals), which is exactly the type of encoding being used. So let's see how we can decode it.

On https://www.dcode.fr/cistercian-numbers you can convert to and from cisterian numbers, and the way the system works is that there's a line and it can contains quadrants to represent numbers from 0  to 9999, depending on the symbol in each quadrant. The vertical without anything is equal to 0

![cisterian 0](../Screenshots/char(0).png)

And the value the symbols can have is
![](../Screenshots/Pasted%20image%2020240331140555.png)

 So by identifying the symbol and its location it's possible to know which value it represents.

And the numbers from 1 to 9 are:
![Cisterian digits](../Screenshots/Pasted%20image%2020240331141429.png)
\

But rather than doing the conversion ourselves, let's identify which symbols are in each quadrant and put them on dcode so that we can get the value.

The first one is equal to 3, the second which is  composed by ![char(15)](https://www.dcode.fr/tools/cistercian-numbers/images/char(15).png)![char(8)](https://www.dcode.fr/tools/cistercian-numbers/images/char(8).png)![char(39)](https://www.dcode.fr/tools/cistercian-numbers/images/char(39).png) is equal to 9058, the third one which is composed by ![char(7)](https://www.dcode.fr/tools/cistercian-numbers/images/char(7).png)![char(17)](https://www.dcode.fr/tools/cistercian-numbers/images/char(17).png)![char(39)](https://www.dcode.fr/tools/cistercian-numbers/images/char(39).png)![char(21)](https://www.dcode.fr/tools/cistercian-numbers/images/char(21).png) is equal to 9177, and so on until we get the representation of each symbol:
`3 9058 9177 8201 6164 2533 7143 5656 7784 3452 4910 7101 2237 9901`
Combined in a single number they form:
`39058917782016164253371435656778434524910710122379901`
How could we make this turn into text for the flag? Working backwards could mean that we might have to make a hex to ascii conversion, so let's turn this number into base 16, because turning it to hex and then to ascii would do nothing but ending up with the same string. So let's treat it as a number by converting it to base 16 in [cyber chef](https://cyberchef.org/)
![decimal to base 16](../Screenshots/Pasted%20image%2020240331142540.png)
This looks promising since 68 represents the hex value for the letter h. Let's convert the entire thing with the *From Hex* recipe
![flag](../Screenshots/Pasted%20image%2020240331142643.png)

And thus we get the flag `he2024{monk_numberalz}`