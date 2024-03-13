# Description
Coney Island Hackers are back!
They changed the passphrase of their secret web portal to: `coneʸisland`.
However, they implemented some protection:
-   letters and some special characters are not allowed
-   maximum length of the string entered is 75
[http://ch.hackyeaster.com:2302](http://ch.hackyeaster.com:2302)

**Hint**
eval

# Solution
The site has a form where you need to enter the password `coneʸisland` 
![[Pasted image 20230412122922.png]]

Entering the password as is returns an error saying that there was an invalid character: letter
![[Pasted image 20230412123015.png]]

Let's have a look at the source
## index.html
```
<!DOCTYPE html>
<html>
	<head>
		<title>Coney Island Hackers</title>
		<link rel="stylesheet" href="https://unpkg.com/purecss@2.0.6/build/pure-min.css" integrity="sha384-Uu6IeWbM+gzNVXJcM9XV3SohHtmWE+3VGi496jvgX1jyvDTXfdK+rfZc8C1Aehk5" crossorigin="anonymous">
		<link rel="stylesheet" href="https://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css">
		<link rel="stylesheet" href="styles.css">
	</head>
	<body>
		<div class="splash-container">
			<div class="splash">
				<img class="title-image" src="title.png">
				<h1 class="splash-head smaller">Coney Island Hackers 2</h1>
				<p class="splash-subhead"></p>
				<div class="green">enter passphrase to enter</div>
				<form role="form" method="GET" action="/">
					<div class="form-group"></div>
					<label for="passphrase"></label>
					<input class="form-control" id="name" type="text" placeholder="passphrase" name="passphrase">
					<button class="pure-button pure-button-primary" type="submit" name="form">Login</button>
				</form>
				<p></p>
			</div>
		</div>
	</body>
</html>
```


So it just sends a GET request with the parameter passphrase and everything else is on the backend.

So first let's figure out which characters are allowed.
Using the entire ASCII range:
`!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~`

to use the intruder in burp leads to the following results:


So let's test out which characters are allowed. The following list will do, as it represents the entire ascii range of printable characters.

### characters
```
!
"
#
$
%
&
'
(
)
*
+
,
-
.
/
0
1
2
3
4
5
6
7
8
9
:
;
<
=
>
?
@
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
[
\
]
^
_
`
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
{
|
}
~
```

These will be sent through burp's intruder on the request that sends the password
`GET /?passphrase=<payload>&form=`
And we will add a filter to catch when it finds the `found invalid character` string so that we can discard those. We add them under the settings tab inside intruder
![[Pasted image 20230419085249.png]]

And the resulting responses are what our valid charset is:
### valid charset
```
!
"
#
%
&
'
(
)
*
+
,
0
1
2
3
4
5
6
7
8
9
:
;
?
@
[
]
^
`
-
.
```
With that in mind, we can leverage the following research to find a way to enter an expression that ends up being evaluated as a letter
https://portswigger.net/research/executing-non-alphanumeric-javascript-without-parenthesis

The premise is this, since certain expressions return specific strings, like: undefined = `[][[]]`
\[object Object\] = `[[]+{}][+[]]`
false = `[![]+[]][+[]]`

So the string cone\<to be figured out\>island
is something like
c = `[[]+{}][+[]][5]` from \[obje**c**t Object\]
o = `[[]+{}][+[]][1]` from \[**o**bject Object\]
n = `[[][[]]+[]][+[]][1]`  from u**n**defined
e = `[[]+{}][+[]][4]` from \[obj**e**ct Object\]
ʸ = TBD but maybe just send it as ʸ
i = `[[][[]]+[]][+[]][5]` from undef**i**ned
s = `[![]+[]][+[]][3]` from fal**s**e
l = `[![]+[]][+[]][2]` from fa**l**se
a =  `[![]+[]][+[]][1]` from f**a**lse
n = `[[][[]]+[]][+[]][1]`  from u**n**defined
d = `[[][[]]+[]][+[]][2]`  from un**d**efined

And each letter has to be concatenated with a `+`

So the passphrase ends up like this
`[[]+{}][+[]][5]+[[]+{}][+[]][1]+[[][[]]+[]][+[]][1]+[[]+{}][+[]][4]+"ʸ"+[[][[]]+[]][+[]][5]+[![]+[]][+[]][3]+[![]+[]][+[]][2]+[![]+[]][+[]][1]+[[][[]]+[]][+[]][1]+[[][[]]+[]][+[]][2]`
And while in eval it does evaluate to `coneʸisland`
![[Pasted image 20230419102139.png]]
It is unfortunately too long at 183 characters, while the limit is 75
![[Pasted image 20230419102216.png]]

Object.getPrototypeOf("") = String {""}

If I can somehow be able to run the following code:
`String.fromCharCode(99,111,110,101,696,105,115,108,97,110,100)`
evaluates to `coneʸisland`

A few things that need a solution before that happens:
- S
- C
- h
- r
- g
- 

 `eval("\u0063\u006f\u006e\u0065\u02b8\u0069\u0073\u006c\u0061\u006e\u0064")`

If I could use an inverted slash in the eval, I could do this. So base64 and the btoa() function could be the key.

The string
`v;\` gets encoded to `djtc`, which are characters that I have

Another approach is looking for a way to optimize my current solution. This would look like this:

c = `[[]+{}][0][5]` from \[obj**e**ct Object\]
o = `[[]+{}][0][1]` from \[obj**e**ct Object\]
n = `[[][[]]+[]][0][1]`  from u**n**defined
e = `[[]+{}][0][4]` from \[obj**e**ct Object\]
ʸ = send it as it is ʸ
i = `[[][[]]+[]][0][5]` from u**n**defined
s = `[![]+[]][0][3]` from fal**s**e
l = `[![]+[]][0][2]` from fa**l**se
a = `[![]+[]][0][1]` from f**a**lse
n = `[[][[]]+[]][0][1]`  from u**n**defined
d = `[[][[]]+[]][0][2]`  from un**d**efined

Leaving us with the payload:
```
[[]+{}][0][5]+[[]+{}][0][1]+[[][[]]+[]][0][1]+[[]+{}][0][4]+'ʸ'+[[][[]]+[]][0][5]+[![]+[]][0][3]+[![]+[]][0][2]+[![]+[]][0][1]+[[][[]]+[]][0][1]+[[][[]]+[]][0][2]
```
Which is still too large, at 163 chars long

What if I defined variables for those strings that are repeated?
So:
 `_=[[][[]]+[]][0]` which is "undefined"
 `_1=[[]+{}][0]`  which is "\[object Object\]"
 `_2=[![]+[]][0]`  which is "false"
 
But the variable named `_` should be the one that is repeated the most, since it's in my best interest to use as few characters as possible, so instead:

 `$=[[][[]]+[]][0]` which is "undefined"
 But then after trying to test this in the javascript console, it seems that just entering $ returns an empty function rather than the variable that I defined, so there goes that character that I wanted to spare.
 ![[Pasted image 20230426105551.png]]
 `$1=[[][[]]+[]][0]` which is "undefined"
 `$2=[[]+{}][0]`  which is "\[object Object\]"
 `$3=[![]+[]][0]`  which is "false"
 c = `$2[5]`
 o = `$2[1]`
 n = `$1[1]`
 e = `$1[3]`
 ʸ = 'ʸ'
 i = `$1[5]`
 s = `$3[3]`
 l = `$3[2]`
 a = `$3[1]`
 n = `$1[1]`
 d = `$1[2]` 

Then I would have to declare them at the beginning of the payload and then just use them and concatenate them... but wait, the underscore is an invalid character! Then I must find one that I can name a variable with. According to [w3schools](https://www.w3schools.com/js/js_variables.asp)

Variable names can start with $ and _ so we can use the dollar sign instead
So it would look like:
```
$1=[[][[]]+[]][0];$2=[[]+{}][0];$3=[![]+[]][0];$2[5]+$2[1]+$1[1]+$1[3]+'ʸ'+$1[5]+$3[3]+$3[2]+$3[1]+$1[1]+$1[2]
```
Which is 111 characters long >\_< !


Let's see, how could we reduce further the characters? Let's have a look at how to reduce the declaration length.

So since `[][[]]` is undefined and anything that you concatenate to another array will yield an string (`+[]`), the way to represent the word undefined as string is:
`[][[]]+[]` and we just have to assign that to a variable

So `$1=[][[]]+[]` which is shorter than `$1=[[][[]]+[]][0]` by 5 characters
![[Pasted image 20230426131141.png]]
And now we can access the letters by doing `$1[0]`

For `[object Object]` we can just assign the expression `[]+{}` to a variable that that will be the string in question `$2=[]+{}`. Accessing the letters will be the same. `$2[0]`
![[Pasted image 20230426131832.png]]

For false we'll do something similar, just the expression that leads to false `![]` and convert it to a string with `+[]` resulting in `![]+[]` as what we have to assign to our 3rd variable
![[Pasted image 20230426132056.png]]
Let's see how much we improved our payload

```
$1=[][[]]+[];$2=[]+{};$3=![]+[];$2[5]+$2[1]+$1[1]+$1[3]+'ʸ'+$1[5]+$3[3]+$3[2]+$3[1]+$1[1]+$1[2]
```
Down to 100 characters. Still need to optimize it further. 25 characters fewer are required.
![[Pasted image 20230426132626.png]]

What about finding out new ways to get strings? If I can get the necessary letters with fewer or shorter definitions, then maybe it will be possible.

So `eval($+[])` evaluates to the string 
```
"function () {
    [native code]
}"
```
from
c o n e y i s l a n d it has 
c o n e \_ i \_ \_ a n d
false has the l and s missing, so these will make it so that I only use 2 declarations which are quite shorter:
c = `$1[3]`
o = `$1[6]`
n = `$1[2]`
e = `$2[4]`
'ʸ'
i = `$1[5]`
s = `$2[3]`
l = `$2[2]`
a = `$2[1]`
n = `$1[2]`
d = `$1[28]`
`$1=$+[];$2=![]+[];$1[3]+$1[6]+$1[2]+$2[4]+'ʸ'+$1[5]+$2[3]+$2[2]+$2[1]+$1[2]+$1[28]`

What if I declare all of the letters that I need in a single variable? Doing this will also get rid of the necessity to use a concatenation with an empty array to convert eveything into a string
So `$1=$+![]` is equal to
`"function () { [native code] }false"`
```
$1=$+![];$1[3]+$1[6]+$1[2]+$1[24]+'ʸ'+$1[5]+$1[36]+$1[35]+$1[20]+$1[2]+$1[28]
```

And the dissaster struck. I realized I cannot use the $ symbol. So this approach will not work at all.

Now, I still can declare variables using ISO 8859-1 or Unicode letters such as `å` and `ü`

So let's go back to a previous payload, one that didn't use the $ as part of where we took the string from
`$1=[][[]]+[];$2=[]+{};$3=![]+[];$2[5]+$2[1]+$1[1]+$1[3]+'ʸ'+$1[5]+$3[3]+$3[2]+$3[1]+$1[1]+$1[2]`

And replace the variable names. Since they're a character shorter, it might be enough reduction to comply with the limit
ñ = `undefined[object Object]false`
`ñ=[][0]+{}+![];ñ[14]+ñ[10]+ñ[1]+ñ[3]+'ʸ'+ñ[5]+ñ[27]+ñ[26]+ñ[25]+ñ[1]+ñ[2]`

And it's finally 74 characters long!!!
![[Pasted image 20230503104031.png]]
