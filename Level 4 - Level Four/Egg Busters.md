#web 
# Description
Ghostbusters go Egg Hunting!

Open their webpage and find the `egg.png`.

[Egg Busters web site](http://ch.hackyeaster.com:2407)
## Hint
You don't need to have an account (sign-up doesn't work anyway).
Do some research!
# Solution
Let's start by looking at this site.
![](../Screenshots/Pasted%20image%2020240412182951.png)
Having in the name ghostbusters kind of reminds me of go buster, so I can run it and see if I can find something interesting by using a wordlist.

But first, let's see if there's a robots.txt for a quick win.
## robots.txt
```
User-agent: *
Sitemap: http://ch.hackyeaster.com:2407/sitemap.xml
Disallow: /ghost/
Disallow: /p/
Disallow: /email/
Disallow: /r/
```
There's a sitemap
![sitemap.xml](../Screenshots/Pasted%20image%2020240412183259.png)
a /ghost/ directory that redirects to a sign in
![/ghost/](../Screenshots/Pasted%20image%2020240412183357.png)
A /p/ directory that seems to lead nowhere. Same for /email/ and /r/
![404](../Screenshots/Pasted%20image%2020240412183518.png)

Ok, so the goal is finding egg.png... could it be as easy as going to `/egg.png`?
![egg.png](../Screenshots/Pasted%20image%2020240412183737.png)
Got the flag `he2024{p4th_tr4v3rs4ls_st1ll_h4pp3ns}` and it's valid... so this is surely not the intended solution, but hey, if it works it works.