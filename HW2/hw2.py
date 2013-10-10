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
    triangular = triangular + i

# Printing the answer    
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

#Variables for P4
n = 10
result = 0
#for looping using range n viarable
for i in range(n):
    #n looping to get result
    result = result * i

#print result
print "The Factorial of", n, "is = ", result
    

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

# ... write your code and comments here (and remove this line)

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

# ... write your code and comments here (and remove this line)

###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").
# https://wiki.python.org/moin/ForLoop


###
### Reflection
###
# what took me long was the decimal places. I didn't know that by adding .0 will give you decimal places
# or you can use the float function as well. All the looping function can be found in chapter 7.

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
