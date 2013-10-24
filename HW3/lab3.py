#variables
n = 7
series = "fibonacci"


if series == "fibonacci":
    #variable
    a = 1
    b = 1
    for i in range(n-2):
        c = a + b
        a = b 
        b = c
    print "The "  +str(n) + "th is " +str(c)
elif series == "sum":
    sums = 0
    number = 0
    for i in range(n):
       number = 3*(i+1) 
       sums = number + sums
    print sums
    
else:
    print "invalid string"
        
    


# this lab I found that the variable that I define are import since thats what 
# will affect my i in range. If the variables of A & B are 1 then n-2 is the range

#Collaborators
#Brandon
#Mica