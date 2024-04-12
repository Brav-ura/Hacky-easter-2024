#web 
# Description
After a lengthy slumber spanning nine years, Wise Rabbit finally resurfaces on Hacky Easter!

_A simple number guessing,_  
_might be a little stressing,_  
_but with a simple tweak,_  
_you'll find the egg you seek._

[Wise Rabbit's Page](http://ch.hackyeaster.com:2405)

## wiserabbit3.txt
```
<html>
    <head>
    <link rel="stylesheet" href="https://cdn.rawgit.com/Chalarangelo/mini.css/v3.0.1/dist/mini-default.min.css">
    </head>
    <body style="padding: 50px; background-color: #ffffff; background-image: url('background.jpg'); background-size: cover;">
    <div style="width:300px; margin:0 auto;">
      <img src="rabbit.jpg" style="width:300px; border-radius: 150px;"></img>
    </div>
    <br/><br/>

<?php
require_once('egg.php');
$code = $_GET['code'] ?? null;
if (isset($code)) {
    echo('<div class="card" style="margin:0 auto;">');
    if (strpos($code, ".")) {
        echo('<p><mark class="inline-block secondary">invalid character found!</mark></p>');
    } else if (!is_numeric($code)) {
        echo('<p><mark class="inline-block secondary">no number!</mark></p>');
    } else if (strlen($code) <= 5) {
        echo('<p><mark class="inline-block secondary">too short!</mark></p>');
    } else if ($code < 13037) {
        echo('<p><mark class="inline-block secondary">too small!</mark></p>');
    } else if ($code > 13037) {
        echo('<p><mark class="inline-block secondary">too big!</mark></p>');
    } else{
        echo('<p><mark class="inline-block">congrats!</mark></p><br/><img style="width: 256px; padding:32px;" src="'.$img.'"/>');
    }
    echo('</div>');
} else {
?>
<form action="/" method="GET" style="width:480px; margin:0 auto; padding-left:20px;">
    Wise Rabbit says:<br/><br/>
    <blockquote>
    In the search for the right number, a tweak in the quest,<br/>
    Digits dance, a numerical jest.<br/>
    Tweaking and turning, a code wizard's delight,<br/>
    </blockquote>
    <br/>
    <input type="number" name="code" placeholder="Code"></input>
    <input type="submit" value="Submit"></input>
</form>
<?php
}
?>
</body>
</html>
```
# Solution
This challenge has a numeric input field and the wise rabbit's saying.\

![Wise rabbit](../Screenshots/Pasted%20image%2020240409193940.png)
Since the source code of the backend code of this challenge is available, reading it is the best way to figure out how to solve it.
The following part of the code is the backend logic that determines if we're shown the flag or not.
```
if (isset($code)) {
    echo('<div class="card" style="margin:0 auto;">');
    if (strpos($code, ".")) {
        echo('<p><mark class="inline-block secondary">invalid character found!</mark></p>');
    } else if (!is_numeric($code)) {
        echo('<p><mark class="inline-block secondary">no number!</mark></p>');
    } else if (strlen($code) <= 5) {
        echo('<p><mark class="inline-block secondary">too short!</mark></p>');
    } else if ($code < 13037) {
        echo('<p><mark class="inline-block secondary">too small!</mark></p>');
    } else if ($code > 13037) {
        echo('<p><mark class="inline-block secondary">too big!</mark></p>');
    } else{
        echo('<p><mark class="inline-block">congrats!</mark></p><br/><img style="width: 256px; padding:32px;" src="'.$img.'"/>');
```

The goal is to enter the correct number. 
- A number that doesn't have a dot, so no ordinary floats
- That has 5 digits or more
- Isn't less than 13037, and isn't greater than 13037

So it has to be equal to 13037 but with 5 digits or more.

At first I thought about the idea of representing the number in scientific notation, but what if I add a 0 on the left?
<br/>
![Input 013037](../Screenshots/Pasted%20image%2020240409195839.png)

That returns the egg with the flag `he2024{p33_4g3_p33_c0d3_cr4ck3d!}`\
<br/>
![flag](../Screenshots/Pasted%20image%2020240409200006.png)