print "Welcome to matrix determinant calculator"
print "\n"
print "[ a1 | a2 | a3 ]"
print "[ b1 | b2 | b3 ]"
print "[ c1 | c2 | c3 ]"
print "\n"

a1 = input("input value for a1: ")
print "[ %d | a2 | a3 ]" %(a1)
print "[ b1 | b2 | b3 ]"
print "[ c1 | c2 | c3 ]"
print "\n"

a2 = input("input value for a2: ")
print "[ %d | %d | a3 ]" %(a1,a2)
print "[ b1 | b2 | b3 ]"
print "[ c1 | c2 | c3 ]"
print "\n"

a3 = input("input value for a3: ")
print "[ %d | %d | %d ]" %(a1,a2,a3)
print "[ b1 | b2 | b3 ]"
print "[ c1 | c2 | c3 ]"
print "\n"


b1 = input("input value for b1: ")
print "[ %d | %d | %d ]" %(a1,a2,a3)
print "[ %d | b2 | b3 ]" %(b1)
print "[ c1 | c2 | c3 ]"
print "\n"

b2 = input("input value for b2: ")
print "[ %d | %d | %d ]" %(a1,a2,a3)
print "[ %d | %d | b3 ]" %(b1,b2)
print "[ c1 | c2 | c3 ]"
print "\n"

b3 = input("input value for b3: ")
print "[ %d | %d | %d ]" %(a1,a2,a3)
print "[ %d | %d | %d ]" %(b1,b2,b3)
print "[ c1 | c2 | c3 ]"
print "\n"

c1 = input("input value for c1: ")
print "[ %d | %d | %d ]" %(a1,a2,a3)
print "[ %d | %d | %d ]" %(b1,b2,b3)
print "[ %d | c2 | c3 ]" %(c1)
print "\n"

c2 = input("input value for c2: ")
print "[ %d | %d | %d ]" %(a1,a2,a3)
print "[ %d | %d | %d ]" %(b1,b2,b3)
print "[ %d | %d | c3 ]" %(c1,c2)
print "\n"

c3 = input("input value for c3: ")
print "[ %d | %d | %d ]" %(a1,a2,a3)
print "[ %d | %d | %d ]" %(b1,b2,b3)
print "[ %d | %d | %d ]" %(c1,c2,c3)

print "\n"

print "Deeterminant of"
print "[ %d | %d | %d ]" %(a1,a2,a3)
print "[ %d | %d | %d ]" %(b1,b2,b3)
print "[ %d | %d | %d ]" %(c1,c2,c3)
print "equals to: "
print "\n"

print a1,"[ %d | %d ]" %(b2,b3),"   ",a2,"[ %d | %d ]" %(b1,b3),"   ",a3,"[ %d | %d ]" %(b1,b2)
print "  [ %d | %d ]" %(c2,c3)," - ","  [ %d | %d ]" %(c1,c3)," + ","  [ %d | %d ]" %(c1,c2)

print "\n"
print "==>> %d((%d*%d)-(%d*%d)) - %d((%d*%d)-(%d*%d)) + %d((%d*%d)-(%d*%d))" %(a1,b2,c3,b3,c2,a2,b1,c3,b3,c1,a3,b1,c2,b2,c1)
print "==>> %d(%d-%d) - %d(%d-%d) + %d(%d-%d)" %(a1,b2*c3,b3*c2,a2,b1*c3,b3*c1,a3,b1*c2,b2*c1)
x = a1*((b2*c3)-(b3*c2))
y = (a2*(-1))*((b1*c3)-(b3*c1))
z = a3*((b1*c2)-(b2*c1))
print "==>>"," ",x," + ",y," + ",z," = ",x+y+z

print "\n"

print "Bye and Have a Nice Day! "



