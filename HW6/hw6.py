
#problem 3
a = 5
b = 5
c = 2
#assert a == b and b == c


#problem 4

def dv(x, y, z):
    total = x+y
    dv = total/z
    return dv
    
    
print dv(a, b, c)

#problem 5

child = ['alex', 'brandon', 'carla', 'jake']
ages = ('12', '10', '13', '25')
mother = {'julie':1234, 'jessica':12345, 'monica':0011, 'michelle':911}

#problem 6

#create A List and B list with differnt numbers
#create a new list wit the sum of list A and List B

list_a = [2, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]

#create a function that adds the sum of list_a and list_b
# to get list_c

list_c = []


a = len(list_a)
b = int(0)
while True:
    ans = list_b[b] + list_a[b]
    list_c.append(ans)
    b = b + 1
    if b == a:
        break

print list_c
    
#problem 7

#create a dictionary from mother with child using for loop

parent = {}


for k in mother:
    parent = {k:ages}
    
    
print parent
    
    
    
    
ages = ('12', '10', '13', '25')
mother = {'julie':1234, 'jessica':12345, 'monica':0011, 'michelle':911}



for i in mother:
    parent = ((zip(mother, ages))
parent = dict(zip(mother, ages))
        
    
    
print parent


    

        
        

        