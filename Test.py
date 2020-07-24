import socket 
import os 

server_address = ('localHost', 4999)
 
SIZE = 1024
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.bind(server_address) 
s.listen(5) 

while True: 
   print ("menunggu koneksi") 
   client,client_address=s.accept() 
   print "connect from: ",client_address 
   while True: 
        pesan=raw_input(" anda: ") 
        client.send(pesan) 
        pesan=client.recv(1024) 
        print " client", pesa
