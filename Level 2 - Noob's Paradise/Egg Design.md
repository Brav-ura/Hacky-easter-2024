#web
# Description
Hope you like the design of this year's eggs!
![](../Screenshots/Pasted%20image%2020240330200718.png)
  
# Solution
It looks like the flag might be in one of these overlapped eggs. Let's inspect the HTML code of the image on the browser to see if we can find any clues.
```
<div id="layers" style="position: relative; width: 360px; height: 360px; background: none; transform: rotate(-30deg) skew(25deg) scale(0.8); transition: 0.5s; margin-top: -20px; margin-bottom: 60px;">  
    <img id="layer1" src="https://www.hackyeaster.com/img/eggdesign_layer1.png" style="position: absolute; width: 100%; transition: 0.5s; opacity: 0.96; transform: translate(-96px, 96px);">  
    <img id="layer2" src="https://www.hackyeaster.com/img/eggdesign_layer2.png" style="position: absolute; width: 100%; transition: 0.5s; opacity: 0.96; transform: translate(-64px, 64px);">  
    <img id="layer3" src="https://www.hackyeaster.com/img/eggdesign_layer3.png" style="position: absolute; width: 100%; transition: 0.5s; opacity: 0.96; transform: translate(-32px, 32px);">  
    <img id="layer4" src="https://www.hackyeaster.com/img/eggdesign_layer4.png" style="position: absolute; width: 100%; transition: 0.5s; opacity: 0.96;">  
</div>
```
So it is multiple images that are overlapped through CSS. Let's inspect each one separately to see which one has the flag.

Thankfully this is fairly straightforward on Firefox by hovering the mouse over the URL of the image.

And easily enough, the first layer listed is the one with the QR with the flag `he2024{blu3_gr33n_y3ll0w_4nd_r3d}`
![](../Screenshots/Pasted%20image%2020240330201448.png)
