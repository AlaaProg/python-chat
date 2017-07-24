# by Alaa Prog  in 2017/7/16 #
# Server.py                  #
##############################
import socket ,sys, threading

class recv_data(threading.Thread):
	def __init__(self, conn,name):
		threading.Thread.__init__(self)
		self.con = conn 
		self.name name
	def run(self):
		while 1:
			try:
				rec = self.con.recv(1024).decode("u8")
				names_to = rec.split(':')[1]
				if names_to.strip() in client_server:
					client_server[names_to].send(rec.encode("u8"))
				else:
					send = "Not Connect %s"%names_to
					client_server[rec.split(':')[0]].send(send.encode("u8"))
			except:
				self.con.close()
				if client_server != {}:
					del client_server[self.name]
				print ("Close:~ ",client_server.keys())
				break;
		   

    

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1' # IP
port = 5555 # PORT 
soc.bind((host, port))
soc.listen(20)
client_server = {} # Name Client 
print(" Run Server ...... /!")
while True:
	c, dres = soc.accept()
	c.send("Places Your Name:".encode('u8'))
	name = c.recv(1024).decode("u8")
	therd_recv = recv_data(c,name)
	therd_recv.start()
	client_server.update({name:c})
