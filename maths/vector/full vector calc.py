#-*-coding:utf8;-*-

def fck(a):
    n = a
    x = a
    y = []
    while x > 0:
        y.append(1)
        x = x -1
    dec_part = n - len(y)
    if dec_part == 0:
        return 0
    else:
        return 1

def f2i(a):
    x = a
    y = []
    while x > 0:
        y.append(1)
        x = x -1
    return len(y)	
	


def mod(a,b,c):
    import math
    modulus = math.sqrt(pow(a,2) + pow(b,2)+ pow(c,2))
    if fck(modulus) == 0:
            modulus = f2i(modulus)
    else:
        n = pow(a,2) + pow(b,2)+ pow(c,2)
        modulus = u"\u221a%d"%(n)
    return modulus

def scp(a1,a2,a3,b1,b2,b3):
    scp = (a1*b1)+(a2*b2)+(a3*b3)
    return scp

def vtp(a1,a2,a3,b1,b2,b3):
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
    return "%di %sj %sk" %(i_comp,j_comp,k_comp)

def det(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    det = ((a1*b2*c3)+(a2*b3*c1)+(b1*c2*a3)) - ((c1*b2*a3)+(c2*b3*a1)+(b1*a2*c3))
    return det
	


while True:
    print "Welcome To Vector Calculator v1.0 by Phvash"
    print "What would you like to do?"
    print "A: Modulus"
    print "B: Unit Vector"
    print "C: Vector Product"
    print "D: Scalar Triple Product"
    print "E: Projection of r1 on r2"

    choice = raw_input("Kindly Select an Option: ")

    if choice == "A" or choice == "B":
            print "a = xi + yj + zk"
            x = input("input value for x: ")
            y = input("input value for y: ")
            z = input("input value for z: ")

    elif choice == "C":
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
                 
    elif choice == "D":
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

        c2 = input("input value for c1: ")
        print "[ %d | %d | %d ]" %(a1,a2,a3)
        print "[ %d | %d | %d ]" %(b1,b2,b3)
        print "[ %d | %d | c3 ]" %(c1,c2)
        print "\n"

        c3 = input("input value for c1: ")
        print "[ %d | %d | %d ]" %(a1,a2,a3)
        print "[ %d | %d | %d ]" %(b1,b2,b3)
        print "[ %d | %d | %d ]" %(c1,c2,c3)
        print "\n"

    elif choice == "E":
        print "r1 = x1i + y1j + z1k"

        x1 = input("x1: ")
        y1 = input("y1: ")
        z1 = input("z1: ")
        print "r1 = %di + %dj + %dk" %(x1,y1,z1)

        print "r2 = x2i + y2j + z2k"

        x2 = input("x2: ")
        y2 = input("y2: ")
        z2 = input("z2: ")

        print "r2 = %di + %dj + %dk" %(x2,y2,z2)        

        
    else:
        pass

    #1. Modulus
    if choice == "A":
        modulus = mod(x,y,z)
        print "The modulus of 'a = %di + %dj + %dk' is"%(x,y,z),modulus
        print "\n"

    #2.Unit Vector
    if choice == "B":
         modulus = mod(x,y,z)
         print "         %di + %dj + %dk" %(x,y,z)
         print "|a| = -------------------"
         print "            ",modulus
         

    #3. Vector Product
    if choice == "C":
        vector_product = vtp(a1,a2,a3,b1,b2,b3)
        print "The vector product is:"
        print vector_product

    #4. Scalar Triple Product
    if choice == "D":
        scalar_triple_product = det(a1,a2,a3,b1,b2,b3,c1,c2,c3)
        print "The Scalar Triple Product is: %d" %(scalar_triple_product)
 
    #5. Projection of r1 on r2
    if choice == "E":
        scp_r1r2 = scp(x1,y1,z1,x2,y2,z2)
        mod_r2 = mod(x2,y2,z2)
        print scp_r1r2,"/",mod_r2

    print "\n"
    

