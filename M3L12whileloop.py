# prints out 0,1,2,3,4
'''while loop simply repeats as long as a certain
boolean condition is met'''

count = 0
while count < 5:
    print (count)
    count += 1 #This is the same as count = count + 1

# This is how you would break a loop

'''
break is used to exit a for loop or a while loop'''

# prints out 0,1,2,3,4

count = 0
while True:
    print (count)
    count += 1
    if count >= 5:
        break
