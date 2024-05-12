#crypto 
# Description
Someone invented a new code, can you crack it?

`5.3 5.1 3.5 1.1 4.4 3.3 5.4 4.2 1.1 5.1 3.5 5.9 3.1 2.3 2.2 4.5 2.3 3.1`

🚩 Flag
- uppercase
- no spaces
- example: `he2024{FLAGFLAG}`
## Hint
`I==J`
# Solution
Since I is equal to J, there is an encoding where this is also true, the polybius square https://en.wikipedia.org/wiki/Polybius_square
\

![polybius square](../Screenshots/Pasted%20image%2020240512160722.png)
\

But this is a square. Could it be a triangle or a cube? After all, the image for this challenge is a sierpinski triangle.

Searching for triangle message encoding leads to this image on [Reddit](https://www.reddit.com/r/1899/comments/199micm/spoilers_s1_triangle_message_encoding/)
![triangle message encoding](../Screenshots/Pasted%20image%2020240512161110.png)
\

In the numbers of the description of the challenge, the lowest possible value is 1.1, and the highest is 5.9. If we were to take these values as coordinates for this figure, as we'd do on a polybius square, the first digit representing the row, and the second being the corresponding triangle from left to right, decoding the message leads to:
`5.3 5.1 3.5 1.1 4.4 3.3 5.4 4.2 1.1 5.1 3.5 5.9 3.1 2.3 2.2 4.5 2.3 3.1`
- 5.3 =  T
- 5.1 = R
- 3.5 = I/J
- 1.1 = A
- 4.4 = N
- 3.3 = G
- 5.4 = U
- 4.2 = L
- 1.1 = A
- 5.1 = R
- 3.5 = I/J
- 5.9 = Z
- 3.1 = E
- 2.3 = D
- 2.2 = C
- 4.5 = O
- 2.3 = D
- 3.1 = E
So the flag is `he2024{TRIANGULARIZEDCODE}`
