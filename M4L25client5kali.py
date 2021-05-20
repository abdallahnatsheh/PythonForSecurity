#First we are going to import the socket library
import socket

#Next we create a socket object

s = socket.socket()

print ("Socket successfully created")

#reserve a port

port = 1989

#bind to the port
s.bind(('', port))
print ("Socket binded to %s" %(port))

#put the socket into listening mode
s.listen(5)
print ("Socket is now listening")

# a forever loop until we exit

while True:
	#establish connection with client
	c, addr =s.accept()
	print ("Got connection from", addr)