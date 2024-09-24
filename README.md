# folding-at-home-badge-backend

![](https://folding-at-home-badge-backend.simplecode.gr/api/badge/rept0id/)

## User

### How to use

Let's suppose your username on Folding@Home is "rept0id". 

Then, you can add this badge to any repo by :

```
![](https://folding-at-home-badge-backend.simplecode.gr/api/badge/rept0id/)
``` 

Frontend coming soon by 🌼 [Irina Kalman](https://www.github.com/irinakalman). 🌼

## Developer

### Proxy

We assume that there is a top-level proxy redirecting traffic to this container. This is the recommended setup.

**Set up a proxy (preferably Nginx) to redirect traffic to the container.**

However, if you want to skip the recommended setup, change the interface in the configuration from `127.0.0.0` to `0.0.0.0`. This will expose the container publicly. This is not recommended, and you do so at your own risk.

### How to use

First time : 

`
cp .env.original .env
`
and 
`nano .env`, edit the conf.

First and every other time :

```
sudo docker-compose up -d --build
```
