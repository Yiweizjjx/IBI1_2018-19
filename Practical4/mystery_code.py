# What does this piece of code do?
# Answer: output all prime numbers between 1 and 100 (may output 1)

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil
# make a Boolean variable
p=False
# loop
while p==False:
    p=True
# draw random integer from 1 to 100    
    n = randint(1,100)
# take the ceiling of √n
    u = ceil(n**(0.5))
# loop   
    for i in range(2,u+1):
# test if n is a prime number        
        if n%i == 0:
# n is not a prime number, continue the loop            
            p=False


 # output the prime number    
print(n)
