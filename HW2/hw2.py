# Name: Cardin Nguyen (Trong)
# Evergreen Login: ngutro25
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###


# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

# x = 1 + 2 + 3 + . . . + 100

import math


# import hw2test & define variables
from hw2_test import n
x = 0
result =0

#start while statements

while (x < n):
    x = x+1
    result = result + x

print ("Example 1: The Total of of 1 to 100 is: " +str(result)) 
    
    
###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

# ... write your code and comments here (and remove this line)


b = 1.0
a = 0.0

for a in range(2, 11):
    a = (b)/a
    print(a)


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0

for i in range(n+1):
# add i to triangular looping n times.
    triangular += i

# Printing the answer    
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

#Variables for P4
# result must be viariable 1 and not 0 because of mutiplication rule
result = 1

#for looping using range n viarable
for i in range(n):
    #i looping plus 1
    result *= i+1

#print result
print "The Factorial of", n, "is = ", result
    
#Example 2
#defining a function

def factorial(n):
    fac = 1
    for i in range(n):
        #takes previous i to get fac and loops
        fac *= i+1
    return fac

#print result
print "The factorial function is:", factorial(n)
###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"


#variables
n = 10
fac=1
for i in range(n):
    #reset fact to 1 after n - previous n
    fac=1
    # Takes n minus the remaining [i] in range
    x = n-i 
    # new if in rage of x 9 8 7 6 5 4 3 2 1
    for j in range(x):
         #takes remaining j in x range multiply it
         fac= fac*(j+1) 
    #print fac after each loop
    print fac
    

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

#variables
n = 10
fac=1
fac2 = 1
for i in range(n):

    #add previous fact to new one
    fac2 = fac2 + (1/fac)
    #reset fact to 1 after n - previous n
    fac=1
    # Takes n minus the remaining [i] in range
    x = n-i 
    # new if in rage of x 9 8 7 6 5 4 3 2 1
    for j in range(x):
         #takes remaining j in x range multiply it
         fac= fac*(j+1)/1.0
    #print fac after each loop
    print fac2

###
### 
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").
# https://wiki.python.org/moin/ForLoop
# Chapter 7 and 10 helped a bit.


###
### Reflection
###
# what took me long was the decimal places. I didn't know that by adding .0 will give you decimal places
# or you can use the float function as well. All the looping function can be found in chapter 7.
# It took me 2-3 hours figuring out the order of python. Most of the examples we got in class was short and easy.
# These problems too longer to do since it require some backtrack reading. There wasn't any tutorials links at homepage
# that I find useful. Most of it was through classmates examples they got so far then fiddling around with it. 
# Everything in this assignment is in the lecture which is why its easy to understand. What took long was learning to
# be neat with codes.


# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
