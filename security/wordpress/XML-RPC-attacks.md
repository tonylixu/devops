### What is XML-RPC?
WordPress utilizes XML-RPC to remotely execute functions. The popular plugin JetPack and the WordPress mobile application are two great examples of how WordPress uses XML-RPC. This same functionality also can be exploited to send thousands of requests to WordPress in a short amount of time. This scenario is effectively a brute force attack.

### How to Recognizing an XML-RPC Attack
You will see tons of entries in your apache `access_log` like the following:
```bash
185.188.204.5 - - [21/Nov/2017:15:19:48 +0000] "POST /xmlrpc.php HTTP/1.0" 500 251 "-" "Mozilla/4.0 (compatible: MSIE 7.0; Windows NT 6.0)"
```

You will see high server resource usages, for example, Memory. `sar -r` :)

Your wordpress website will be brought down frequently and the `Error connecting to database` will be seen for your browser.

### How to prevent
* You could install the Jetpack plugin for WordPress can block the XML-RPC multicall method requests with its Protect function. You will still see XML-RPC entries in your web server logs with Jetpack enabled. However, Jetpack will reduce the load on the database from these malicious log in attempts by nearly 90%. To install, just go to "Plugins" -> "Add New" then install "Jetpack".
* At Apache/Nginx level. Restart the process after.
  * For Apache, add the following to your conf file:
```bash
<Files xmlrpc.php>
    Order Allow,Deny
    Deny from all
</Files>
```
  * For Nginx:
```bash
location /xmlrpc.php {
      deny all;
}
``` 