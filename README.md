# MinuteMail
A python package for recieving mail from temporary email addresses.

## Installation

This package has been published on PyPi, to install it run
```pip install MinuteMail```

## Usage

```python
# Import package
import MinuteMail

# Create a new mailbox
box = MinuteMail.mailbox()

# A new mailbox already comes with one email address
print(box.get_emails()[0])

# You can save the passwords to addresses to a file
'''
with open ('email_hashes.txt', 'w') as f:
	for hash in box.email_hashes:
		f.write(hash)
		f.write('\n')
'''
# You can then read the hashes and add them to the box in the next session
'''
with open ('email_hashes.txt', 'r') as f:
	for hash in f:
		box.add_hash(hash)
'''

#Wait for and print arriving mail
while True:
	print(box.next())

```

### Emails come in JSON format. Here's an example of what you'd recieve
```json
{
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