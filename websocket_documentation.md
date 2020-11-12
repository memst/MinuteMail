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

### Formatted example of email data that you'd receive:
Pay attention to the I at the beginning
```json
I{
   "to_mail_orig":"zbitobdkvvbb@dropmail.me",
   "to_mail":"zbitobdkvvbb@dropmail.me",
   "text_source":"text",
   "text":"This is message text",
   "subject":"This is the message subject line",
   "ref":"l2vnogdc02kme9oetllg27ivstqdcer6",
   "received":"2020-11-12T13:30:24Z",
   "has_html":true,
   "from_mail":"sender@email.xx",
   "from_hdr":"'Sender Name' <sender@email.xx>",
   "decode_status":0,
   "attached":[
      
   ]
}
```