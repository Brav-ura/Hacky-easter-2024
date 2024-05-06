#forensics 
# Description
My friend sent me this image, but I don't get the message.

Never heard of this stenago thing.\

![stenago.png](../Screenshots/Pasted%20image%2020240506203222.png)
# Solution
Since this seems to be a steganography challenge, let's use a site that is specialized for this sort of things https://georgeom.net/StegOnline/upload and upload the image.

Let's try some of the basic things, like showing the strings
## Strings (5 chars+)
```
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 6.0.0">
xmlns:tiff="http://ns.adobe.com/tiff/1.0/">
<tiff:Orientation>1</tiff:Orientation>
<rdf:Description rdf:about=""
</rdf:Description> 
[SNIPPED]
```
Nothing of any particular value in here.

## Manipulating color values
We have the option to see full red, full green, full blue, inverse RGB values and LSB (least significant bit) half.

Couldn't see anything interesting in any, except a curious pattern on the very beginning of the image
\

![Suspicious pattern](../Screenshots/Pasted%20image%2020240506204513.png)
\

And looking more closely to the original image, there is also something weird going on in it. That pattern stops after the same spot. An added red line shows where it stops.
\

![same pattern](../Screenshots/Pasted%20image%2020240506204756.png)
\
## Exploring the bit planes
While there's nothing at plain sight on red 0
\

![red 0](../Screenshots/Pasted%20image%2020240506205522.png)
\

Or red 1
\

![red 1](../Screenshots/Pasted%20image%2020240506205611.png)
\

The pattern that we saw is present on red 2
\

![red 2](../Screenshots/Pasted%20image%2020240506205722.png)
\

This pattern is also present in green 3
\
![green 3](../Screenshots/Pasted%20image%2020240506205925.png)
\

And in blue 4
\
![blue 4](../Screenshots/Pasted%20image%2020240506210011.png)
\
## Extracting data from the bit planes
By selecting the bits where the pattern was shown: red 2, green 3 and blue 4
\
![extracting data](../Screenshots/Pasted%20image%2020240506210304.png)
\

We can see that what it was is the flag repeated, hidden in specific bits for the color values of the image
\

![flag](../Screenshots/Pasted%20image%2020240506210512.png)
\
So the flag is `he2024{h1d1ng_stuff_1n_p1x3ls}`