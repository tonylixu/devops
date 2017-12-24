### Checkout the Nginx container
### Create a Nginx Proxy Docker network
* From the command line

```bash
# docker network create nginx-proxy-public
```

* Go into the Nginx Docker directory

```bash
# docker-compose up -d
```

* Check the Nginx is up and running

```bash
# docker-compose ps
pixelcloud-nginx_proxy-docker_gen     /usr/local/bin/docker-gen  ...   Up
pixelcloud-nginx_proxy-lets_encrypt   /bin/bash /app/entrypoint. ...   Up
pixelcloud-nginx_proxy-nginx          nginx                            Up      0.0.0.0:443->443/tcp, 0.0.0.0:80->80/tcp

```
### Import client certs into containers
After the above step, any container that joins `nginx-proxy-public` network will need a client certs on the client side when connecting to the Nginx proxy network.