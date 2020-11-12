[dropmail.me](https://dropmail.me/en/) works via a websocket on url `wss://dropmail.me/websocket`.

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