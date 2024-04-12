#misc 
# Description
Time for a TV evening!

🚩 Flag

- uppercase
- wrap in `he2024{` and `}`

## primetime.txt
```
01 Channel 1
02 Tele 2
03 El Tele Tre
04 Tele 4
05 Local News
06 International News 24
07 Epic Movies
08 CMM
09 Film9
10 Cinema-X
11 Cold North TV
12 Southern TV 5
13 Only News
14 Sports
15 More Sports
16 Most Sports
17 Music & More
18 Comic Cosmos
19 All The Comics
20 TV Twenty
21 Plenty And One
22 Children's Channel
23 No Man's Choice
24 Survival Channel
25 Gaming Overload
26 Game Duck
27 Hacky Easter TV
28 CTF
29 Dingo TV
30 Rockatansky
31 Only Techno
32 1337 TV
```

# Solution
Since the channels are naturally numbered, let's start by deleting all that aren't in a prime number and go from there.

```
02 Tele 2  
03 El Tele Tre  
05 Local News  
07 Epic Movies  
11 Cold North TV  
13 Only News  
17 Music & More  
19 All The Comics  
23 No Man's Choice  
29 Dingo TV  
31 Only Techno
```

Tried to see if there's a show that has a prime number of letter's in it. So let's delete the channel numbers and just have the show names

```
Tele 2
El Tele Tre
Local News
Epic Movies
Cold North TV
Only News
Music & More
All The Comics
No Man's Choice
Dingo TV
Only Techno
```

But there is more than one, like Tele 2, Local News, and others, so this must not be it.

After some time of going back and forth between challenges, I finally saw that if only the first letter of each channel is taken, they spell TELECOMANDO, which is the correct flag.