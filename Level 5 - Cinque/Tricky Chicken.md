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
![](../Screenshots/Pasted%20image%2020240331164935.png)
