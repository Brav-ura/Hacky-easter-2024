#crypto 
# Description
Prison guards found a snippet of paper with a hand-written message:

`    Hello! This message is for John. He is in block A, 12. 10 days ago, 12 am, 14th of July you asked me about my friends out there. O{h, awesome what they managed to do! We will certainly succeed. I don't think there will be any problems. I now need to organize how, we, us will start. Ideally you know it, past reading this message. My best regards. O}k    `  

There seems to be a hidden message in there. Can you find it?

# Solution
Looking at the text, the curly brackets {} are present within the text, so this suggests that the message is in plain text, hidden in plain sight. There are a bunch of numbers in the first part of the text as well, and there are enough to form 2024.

Looking at the brackets, since they are the characters that are the most out of place, let's see if there's a pattern where they appear.
`there. O{h, awes`
`regards. O}k `

In the first one, there's a punctuation mark and then the 3rd character after it is the opening curly bracket. 
In the second one, that same pattern seems to repeat.

Following that logic, let's get the 3rd character after each punctuation mark.

Hello! T`h`is message is for John. H`e` is in block A, 1`2`. 1`0` days ago, 1`2` am, 1`4`th of July you asked me about my friends out there. O`{`h, a`w`esome what they managed to do! W`e` will certainly succeed. I `d`on't think there will be any problems. I `n`ow need to organize how, w`e`, u`s` will start. I`d`eally you know it, p`a`st reading this message. M`y`  
best regards. O`}`k

Which ends up forming: `he2024{wednesday}`