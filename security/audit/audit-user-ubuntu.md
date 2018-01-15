## Auditing Your Ubuntu Servers
You might be wondering how to audit your Ubuntu server / your Ubuntu local machine. Well, In this blog I will show you how easy it is do so. Auditing can be done by many ways of which few we shall discuss here. There are 3 following scenarios which we will be discussing:

### Finding from where logins are done & commands are executed
We can find the IP from where a ssh login has been done and commands have been executed. Also we can get the status of logins & those commands.

Suppose a Server has 2 users:
* Ubuntu which has sudo access.
* tony is a another user created by useradd.
* Login to your server using Ubuntu user.
Also, login to server in with user tony from another machine which might be running on the same or other network.

Now, if we want to check from where the ssh logins have been made
Run command ->

`pstree -p` and grep whatever command you want to audit
like `grep sshd`
or simply `ps -ef | grep sshd`