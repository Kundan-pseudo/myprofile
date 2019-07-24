try:
    open("fname", "r")
except IOError:
    pass;
print "exception handled" 
