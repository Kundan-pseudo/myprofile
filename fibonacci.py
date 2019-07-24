a=0
b=1
n=input("Enter the nth term")
print a
print b
for i in range (1,n):
    s=a+b
    a=b
    b=s
    print s
