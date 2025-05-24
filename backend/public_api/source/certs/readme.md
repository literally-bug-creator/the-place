# How to generate private token?
```
openssl genrsa -out jwt-private.pem 2048
```

# How to generate public token by private token?
```
openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem
```
