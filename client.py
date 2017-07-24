# by Alaa Prog  in 2017/7/16 # 
# client.py                  #
##############################
import socket, sys, threading


host = '127.0.0.1'# IP
port = 5555 # PORT 
class RECV(threading.Thread):
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.con = conn 
	def run(self):
		while 1:
			date_recv = self.con.recv(1024).decode("Utf8")
			print("#"+date_recv.replace(":"+names+":","> "))
			if not date_recv or date_recv.upper() =="exit":
				break
		self.con.close()
		sys.exit()

class SEND(threading.Thread):
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.con = conn
	def run(self):
		while 1:
			date_send = input()
			send = names+":"+date_send
			self.con.send(send.encode("Utf8"))
			



con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	con.connect((host, port))

	message_recu = con.recv(1024).decode("Utf8")
	print(message_recu,end=" ")
	names = input()
	con.send(names.encode("Utf8"))

except socket.error:
	sys.exit()


th_E = SEND(con)
th_R = RECV(con)
th_E.start()
th_R.start()
