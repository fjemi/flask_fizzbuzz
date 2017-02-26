
# coding: utf-8

# In[13]:

#
# FizzBuzz program
# Print the number 1 through 100. 
# If the number is a multiple of 3 print Fizz
# if it is a multiple of 5 print print Buzz
# If it is a multiple of both 3 and 5 print Fizz Buzz
#

count = 0

while  (count < 100):
    count += 1
    
    # number multiple of 5 and 3
    if ((count % 15 == 0)):
        print("FizzBuzz")
    # number is a multiple of 3
    elif (count % 3 == 0):
        print ("Fizz")
    # number multiple of 5
    elif (count % 5 == 0):
        print ("Buzz")
    # number is a multiple of neither 3 nor 5
    else:
        print (count)
