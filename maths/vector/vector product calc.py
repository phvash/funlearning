print "Welcome to vector product calculator"
print "\n"
print "[ i  | j  | k  ]"
print "[ a1 | a2 | a3 ]"
print "[ b1 | b2 | b3 ]"
print "\n"

a1 = input("input value for a1: ")
print "[ i | j | k ]"
print "[ %d | b2 | b3 ]" %(a1)
print "[ c1 | c2 | c3 ]"
print "\n"

a2 = input("input value for a2: ")
print "[ i | j | k ]" 
print "[ %d | %d | b3 ]" %(a1,a2)
print "[ c1 | c2 | c3 ]"
print "\n"

a3 = input("input value for a3: ")
print "[ i | j | k ]" 
print "[ %d | %d | %d ]" %(a1,a2,a3)
print "[ c1 | c2 | c3 ]"
print "\n"

b1 = input("input value for b1: ")
print "[ i | j | k ]" 
print "[ %d | %d | %d ]" %(a1,a2,a3)
print "[ %d | c2 | c3 ]" %(b1)
print "\n"

b2 = input("input value for b2: ")
print "[ i | j | k ]" 
print "[ %d | %d | %d ]" %(a1,a2,a3)
print "[ %d | %d | c3 ]" %(b1,b2)
print "\n"

b3 = input("input value for b3: ")
print "[ i | j | k ]" 
print "[ %d | %d | %d ]" %(a1,a2,a3)
print "[ %d | %d | %d ]" %(b1,b2,b3)
print "\n"

i_comp = ((a2*b3)-(a3*b2))
raw_j_comp = ((a1*b3)-(a3*b1))
raw_k_comp = ((a1*b2)-(a2*b1))


if raw_k_comp > 0:
    k_comp = "+%d" %(raw_k_comp)
else:
    k_comp = raw_k_comp

if raw_j_comp < 0:
    raw_j_comp = (raw_j_comp *(-1))
    j_comp = "+%d" %(raw_j_comp)
else:
    j_comp = "-%d" %(raw_j_comp)
    
print "%di %sj %sk" %(i_comp,j_comp,k_comp)

print "\n"
print "Bye and Have a Nice"
