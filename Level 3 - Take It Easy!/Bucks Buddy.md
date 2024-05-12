#web 
# Description
You already know the username (`joe`) and his password (`letmein1`). But, what's next?

[BucksBuddy web site](http://ch.hackyeaster.com:2401)

Note: The service is restarted every hour at x:00.
# Solution
Let's first start looking at the page and its source.
**index**
```
[SNIPPED]
<body>
    <div id="head">
        <a href="/"><img class="item-left" src="/static/logo.png" /></a>
        <h1 class="item-center">Bucks<span>Buddy</span></h1>     
        <div class="item-right">
            ||| <a href="/login">Login</a>
        </div>
[SNIPPED]        
```

**/static/app.js**
```
var ZWHOPPER = 999;

$(window).scroll(function() {
    if($(window).scrollTop() + $(window).height() != $(document).height() - 400) {
        whopperImg = `<div><img style="z-index: ${ZWHOPPER};" class="whoppertileNext" src="/static/whopper.png"/></div>`;
        ZWHOPPER = ZWHOPPER - 1;
        $("#whopper").append(whopperImg);
    }
 });
```
Going to the image URL `/static/whopper.png` returns a 404, so this JavaScript seems useless.

**/login**
```
[SNIPPED]
			<form method="POST" action="/login">
				<div class="item">
					<input class="input" type="text" name="login"
						placeholder="Your Login Name" autofocus="">
				</div>

				<div class="item">
					<input class="input" type="password" name="password"
						placeholder="Your Password">
				</div>
				<div class="item">
					<input class="button" type="submit" name="submit" value="Login" />
[SNIPPED]
```
The login page only has the fields for login and password.

So let's authenticate

![](../Screenshots/Pasted%20image%2020240331132215.png)

This prompts for a second factor authentication. It's unlikely that this needs to be brute forced. Since we don't even know how many digits the code consists of. So let's select the *Try another way* link.


![](../Screenshots/Pasted%20image%2020240331132410.png)

Nowhere on the page have we found information regarding joe, so brute forcing the values is out of the question. So let's have a look at the request that this form generates.

```
POST /questions HTTP/1.1
Host: ch.hackyeaster.com:2401
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 45
Origin: http://ch.hackyeaster.com:2401
Connection: close
Referer: http://ch.hackyeaster.com:2401/questions
Cookie: session=RFFDv85XfU4lqokqt4TYLltlGlyBbooNx4NPYM0MT1g
Upgrade-Insecure-Requests: 1

question0=test&question1=test&submit=Continue
```
What would happen if we don't send the parameters at all? Only the sumbit=Continue

![](../Screenshots/Pasted%20image%2020240331132729.png)

So this returns the QR with the flag, `he2024{Not_that_easy_anymore, sigh!}`, with an interesting bit of trivia about an actual vulnerability that happened. Guess that sometimes it's just that easy, huh?