## sudo pip install --user websocket-client
from websocket import create_connection
import random

class mailbox(object):
	"""10 minute mailbox"""
	def __init__(self):
		super(mailbox, self).__init__()
		self.ws = create_connection("wss://dropmail.me/websocket")
		self.next = self.ws.recv
		self.close = self.ws.close
		self.email_hashes = []
		email_hash = self.next()[1:]
		self.email_hashes.append(email_hash)
		self.next()

	#adds a random email, returns its address
	def addRandomEmail(self):
		self.ws.send("M")
		email_hash = self.next()[1:]
		self.email_hashes.append(email_hash)
		return email_hash.split(":")[0]

	#requires email and has in form name@domain:hash
	def addEmail(self, email_hash):
		self.ws.send("R{}".format(email_hash))
		self.email_hashes.append(self.next()[1:])

	#returns the list of emails present in the socket
	def getEmails(self):
		emails = []
		for email_hash in self.email_hashes:
			emails.append(email_hash.split(":")[0])
		return emails

if __name__ == '__main__':
	box = mailbox()
	#adding emails
	print(box.addRandomEmail())
	print(box.email_hashes)
	print(box.getEmails())
	#reading mail
	print(box.next())