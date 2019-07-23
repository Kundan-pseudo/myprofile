a=input("Enter a Number")
x=a
c=0
while x>0:
    x=x/10
    c+=1
y=a
sum=0
while y>0:
    z=y%10
    y=y/10
    sum+=z**c
if a==sum:
    print "arngstrong"
else:
    print "Not a arngstrong"
print "thankyou"