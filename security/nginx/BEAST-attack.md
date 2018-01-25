## Nginx - Prevent BEAST Vulunerability

### What is BEAST
`BEAST` stands for "Browser Exploit Against SSL/TLS" is an attack against the cipher block chaining (CBC) method used with SSL/TLS. This weakness was discovered in 2002, but finally proven in 2011 by security researchers Thai Duong and Juliano Rizzo. To launch/perform a `BEAST` attack, below conditions need to be met:
* Vulnerable version of SSL must be used using a block cipher (CBC in particular)
* JavaScript or a Java applet injection. Should be in the same origin of the web site.
* Data sniffing of the network connection must be possible.

### Protecting Against BEAST Attack
To gurad against the attack, we have to define that ciphers we allow. Secondly, we have to set our preferenc eof the ciphers to be determined by the server. Next we define what protocols we want to uesr, resulting in older SSL versions to be disallowed.
```bash
ssl_ciphers RC4:HIGH:!aNULL:!MD5;
ssl_prefer_server_ciphers on;
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
```
Regarding the ciphers, we can be more specific that list above. We list specifically what ciphers we want to allow by defining the full list:
```bash
ssl_ciphers “EECDH+ECDSA+AESGCM EECDH+aRSA+AESGCM EECDH+ECDSA+SHA384 EECDH+ECDSA+SHA256 EECDH+aRSA+SHA384 EECDH+aRSA+SHA256 EECDH+aRSA+RC4 EECDH EDH+aRSA RC4 !aNULL !eNULL !LOW !3DES !MD5 !EXP !PSK !SRP !DSS”;
```

After making the changes, reload Nginx. You can check your ssl frpm [SSL checker](https://cryptoreport.thawte.com/checker/).

### RC4 vs BEAST
Today, only TLS 1.2 with GCM suites offer fully robust security. All other suites suffer from one problem or another (e.g, RC4, Lucky 13, BEAST), but most are difficult to exploit in practice. Because GCM suites are not yet widely supported, most communication today is carried out using one of the slightly flawed cipher suites. It is not possible to do better if you’re running a public web site.

The one choice you can make today is whether to prioritize RC4 in most cases. If you do, you will be safe against the BEAST attack, but vulnerable to the RC4 attacks. On the other hand, if you remove RC4, you will be vulnerable against BEAST, but the risk is quite small. Given that both issues are relatively small, the choice isn’t clear.

However, the trend is clear. Over time, RC4 attacks are going to get better, and the number of users vulnerable to the BEAST attack is going to get smaller.
