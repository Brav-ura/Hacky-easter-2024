# Description
I got this string, can you decode it?  
`BOrqQ1,O>91gas<?Z'e(?Y++tAnE37`

# Solution
Since this is some type of encoding, going to dcode to identify the cipher might give us a lead. https://www.dcode.fr/cipher-identifier

Entering the string in the cipher identifier returns ASCII85 as a likely case of the type of encoding being used
![](Screenshots/Pasted%20image%2020240320085613.png)

Entering the string into the ASCII85 decoder returns the decoded string `dCode decodes ASCII85`, so using dCode was the intended tool to solve this challenge.