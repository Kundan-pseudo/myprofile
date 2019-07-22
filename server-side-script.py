import socket as s
import time
so= s.socket(s.AF_INET,s.SOCK_STREAM)
rs=raw_input("Enter the ip adress")
host=s.gethostbyname(rs)
port= 80
so.bind((host,port))
so.listen(5)
while True:
    co,addr=so.accept()
    print("Got a connection from %s" %str(addr))
    ct=time.ctime(time.time()) + "\r\n"
    co.send(ct.encode('ascii'))
    co.close()