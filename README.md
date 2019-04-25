# 10minmail.py
### Just what *you* need
##### _to know to run this damn file._


This is a command-line python client which generates an email address that lasts 10 minutes. It is not traceable back to you. It is a wrapper on the WebSocket endpoint exposed by this [disposable e-mail service](https://dropmail.me/en/).

### Usage for the web socket

```
#create a new connection
websocket = create_connection("wss://dropmail.me/websocket")
#get the email an the hash
email_hash = websocket.recv()
#get just the email
email = email_hash[1:].split(":")[0]
#get the avilable domains (uselesss)
websocket.recv()
#use pre-existing email and hash
websocket.send("R{}".format(email_hash))
#This just repeats the email and the hash you've just given, useless output
websocket.recv()
#To get new mail
mail = websocket.recv()
```