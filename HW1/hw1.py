# Name: Cardin Nguyen (Trong)
# Evergreen Login: ngutro25
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1: Roots - solution follows:"

## Compute and print both roots of the quadratic equation (x*x)-5.86 x+ 8.5408
## 

# Define Variables
a = 1
b = -5.86
c = 8.5408

# rootadd
rootadd = (-(b) + ((b**2) - (4 * a * c)) ) / (2* a)

# rootsubt
rootsubt = (-(b) - ((b**2) - (4 * a * c)) ) / (2* a)

print("The add-quadratic: " +str(rootadd))
print("The sub-quadratic: " +str(rootsubt)) 


###
### Problem 2
###

print "Problem 2: Importing -  solution follows:"

# import file and variables
from hw1_test import a,b,c,d,e,f
# print out the result abcdef
print("a = " +str(a))
print("b = " +str(b))
print("c = " +str(c))
print("d = " +str(d))
print("e = " +str(e))
print("f = " +str(f))


###
### Problem 3
###

print "Problem 3 solution follows:"

# ... write your code and comments here (and remove this line)

print "The Boolean Expression: ((a and b) or (not c) and not (d or e or f))"

print((a and b) or (not c) and not (d or e or f))        

###
### Micah, Jason, Alex 
###

# ... List your collaborators here, as a comment (on a line starting with "#").
