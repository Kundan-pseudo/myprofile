import socket as s
so= s.socket(s.AF_INET,s.SOCK_STREAM)
rs=raw_input("Enter the ip adress")
host=s.gethostbyname(rs)
port= 80
so.connect((host,port))
tm=so.recv(1024)
so.close()
print("The time got from the server is %s" % tm.decode('ascii'))