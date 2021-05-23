# pip install websocket-client
from websocket import create_connection
import json

class mailbox(object):
	def __init__(self):
		super(mailbox, self).__init__()
		self.ws = create_connection("wss://dropmail.me/websocket")
		self.close = self.ws.close
		self.email_hashes = []
		self.id = json.loads(self.ws.recv()[1:])['id']
		email_hash = self.ws.recv()
		self.email_hashes.append(email_hash)
		self.ws.recv() #Discards the list of avilable domains

	#get next email
	def next(self):
		mail_content = self.ws.recv()[1:]
		return json.loads(mail_content)

	#adds a random email, returns its address
	def add_random_email(self):
		self.ws.send("M")
		email_hash = self.ws.recv()[1:]
		self.email_hashes.append(email_hash)
		return email_hash.split(":")[0]

	#requires email and has in form name@domain:hash
	def add_hash(self, email_hash):
		email_hash = email_hash.strip()
		if email_hash not in self.email_hashes:
			self.ws.send("R{}".format(email_hash))
			self.email_hashes.append(self.ws.recv()[1:])

	#returns the list of emails present in the socket
	def get_emails(self):
		emails = []
		for email_hash in self.email_hashes:
			emails.append(email_hash.split(":")[0])
		return emails

if __name__ == '__main__':
	box = mailbox()
	#adding emails
	print(box.add_random_email())
	print(box.email_hashes)
	print(box.get_emails())
	print(box.id)
	#reading mail
	print(box.next())