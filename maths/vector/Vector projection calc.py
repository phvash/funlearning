#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import math
print "Projection of r1 on r2:"
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

s_prdt = (x1*x2) + (y1*y2) + (z1 * z2)
print s_prdt
mod_r2 = math.sqrt(pow(x2,2) + pow(y2,2) + pow(z2,2))

if mod_r2 = float:
    mod_r2 = "√",pow(x2,2) + pow(y2,2) + pow(z2,2)

print mod_r2
prjt = s_prdt/mod_r2

print ("Projection of r1 = %di + %dj + %dk on r2 = %di + %dj + %dk is: %d ") %(x1,y1,z1,x2,y2,z2,prjt)