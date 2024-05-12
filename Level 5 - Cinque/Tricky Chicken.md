#web 
# Description
Tricky Chicken can give you an egg.

But you must know the right code word!

[Tricky Chicken's web site](http://ch.hackyeaster.com:2402)

Note: The service is restarted every hour at x:00.

# Solution
Let's start by having a look at the page and analyzing its source.\
![index](../Screenshots/Pasted%20image%2020240331155843.png)
And its source is:
```
HTTP/1.1 200 OK
Date: Sun, 31 Mar 2024 13:57:56 GMT
Server: Apache/2.4.56 (Debian)
Last-Modified: Sat, 16 Mar 2024 16:54:19 GMT
ETag: "52f-613c9f9b4e4c0-gzip"
Accept-Ranges: bytes
Vary: Accept-Encoding
Content-Length: 1327
Connection: close
Content-Type: text/html; charset=utf-8

<html>
  <head>
      <link rel="stylesheet" href="https://cdn.rawgit.com/Chalarangelo/mini.css/v3.0.1/dist/mini-default.min.css">
      <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.9-1/core.js" type="src/javascript"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.9-1/md5.js" type="src/javascript"></script>
      <meta charset="utf-8">
  </head>
  <body style="padding: 50px; background-color: #ffffff; background-image: url('background.jpg'); background-size: cover;">
    <div style="width:150px; margin:0 auto;">
      <img src="logo.png" style="width:150px;"></img>
    </div>
    <div style="width:500px; margin:0 auto; text-align:center">
      <br/><br/>
      Enter the code:
      <br/><br/>
      <input type="text" id="code"></input>
      <br/>
      <input type="button" id="check" onclick="check_code()" value="Check the Code"></input>
    </div>
  </body>
  <script id="check" src="text/javascript">
    function check_code() {
        val = document.getElementById("code").value;
        hash = CryptoJS.MD5(val).toString();
        if (hash == "078bbb4bf0f7117fb131ec45f15b5b87") {
            alert("Correct!");
            document.location.href = "/" + hash + ".html";
        } else {
            alert("Wrong!");
        }
    }
  </script>
</html>
```

In this file at the end there's a JavaScript script that checks if the value of the input is equal to a hash `078bbb4bf0f7117fb131ec45f15b5b87` and then redirects to that hash + html, so http://ch.hackyeaster.com:2402/078bbb4bf0f7117fb131ec45f15b5b87.html\
![not an egg](../Screenshots/Pasted%20image%2020240331164935.png)

Let's see how the code check works on the browser by looking at the source and setting up a breakpoint in the check_code() function


![setting up a breackpoint](../Screenshots/Pasted%20image%2020240412185947.png)

```

var head = document.getElementsByTagName("head")[0];
var script = document.createElement('script');
script.src = 'https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.9-1/core.js';
head.appendChild(script);
var script2 = document.createElement('script');
script2.src = 'https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.9-1/md5.js';
head.appendChild(script2);

function check_code() {
    val = document.getElementById("code").value;
    if (val.length == 8 && val[0] == 'p' && val[1] == 'а' && val[2] == 'z' && val[3] == 'z' && val[4] == 'w' && val[5] == '0' && val[6] == 'r' && val[7] == 'D') {
        alert("Correct!");
        document.location.href = "/" + CryptoJS.MD5(val).toString() + ".html";
    } else {
        alert("Wrong!");
    }
}
```
The password seems to be `pazzw0rD`. Let's try entering that.

But that was still wrong? Even if the value was the same one of the conditions on the if was false. Let's try to copy each condition from the JavaScript and paste it in the browser console to see which one evaluates to false. But this needs to be done while the code is typed, as it's being obtained by JavaScript

![input pazzw0rD on the text field](../Screenshots/Pasted%20image%2020240412190714.png)

Is the length correct?

![length](../Screenshots/Pasted%20image%2020240412190607.png)
Is the first character correct?

![first character](../Screenshots/Pasted%20image%2020240412190504.png)

Is the second one correct?
![second character](../Screenshots/Pasted%20image%2020240412190847.png)
Wait... what? Could it be a unicode character that resembles the lowercase `a`? Copying it and comparing it to the actual lowercase a still evaluates to false, so they are definitely not the same letter.

![a!=а](../Screenshots/Pasted%20image%2020240412191035.png)
In that case, let's just replace the lowercase a with that other one and send the code pаzzw0rD

![code: pаzzw0rD](../Screenshots/Pasted%20image%2020240412191220.png)

And thus the real egg is obtained with the flag `he2024{such_4_tr1cky_ch1ck3N!}`

![flag](../Screenshots/Pasted%20image%2020240412191411.png)
