#pwn
# Description
Welcome to the Index of Planets!

- `nc ch.hackyeaster.com 2403`

# Solution
Let's connect to the port and see what we get as a response

![planet index prompt](../Screenshots/Pasted%20image%2020240412191656.png)
And here's an index of planets where you can enter one of the numbers and information about that planet will return and then exit.

![index 3](../Screenshots/Pasted%20image%2020240412191804.png)
Let's enter something that is not and index and observer the behavior.

![not_index](../Screenshots/Pasted%20image%2020240412191912.png)
And it just exits.

Entering an index greater than 8 returns the invalid index error message

![invalid index](../Screenshots/Pasted%20image%2020240412192144.png)

Ok, what about a command? `;whoami`
So it didn't like it either. Same for everything that is not a number... well, almost everything.

Entering `-1` is a valid input, and not only that, it returns the error output of exactly the command that is being executed.

![-1 integer underflow](../Screenshots/Pasted%20image%2020240412192324.png)

And the number gets underflowed. So this might be a way forward.

There is also an important piece of information in the prompt. The date of the last update is August 2006, which happens to be when Pluto was demoted to a dwarf planet. So maybe the goal is to try and print the file corresponding to it by manipulating the indexes.

Since we can make it underflow by entering a negative number, if we enter a large enough negative number it might be possible to make it go to 9.

So 65536 - 9 = 65527, so that's the number to give.

![index -65527](../Screenshots/Pasted%20image%2020240412193520.png)

A different error message that leaks the exact comparison that is being made. So the index modulo 10 + 7 needs to be less than or equal to 0. In the case of our input evaluates to more than that (16). Ok, what if we underflow all the way to negative numbers again? This way, the result will be a negative number, so the condition will be met. Now rather than 1 underflow, let's make it 2 underflows by multiplying the maximum number, 65536 times 2  minus 9 which is the offset that we need and supply that as a negative number.

So let's enter `-131063`
\
![pluto ftw](../Screenshots/Pasted%20image%2020240412194900.png)
and we get our flag `he2024{plut0_41nt_n0_plan3t_n0_m0r3}`
