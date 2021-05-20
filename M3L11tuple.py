# This is our first Tuple

'''
Tuples are immutable which means you cannot update or change
the values of tuple elements.
However, you can change the values of tuple elements to
create a new tuple.
'''

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

#Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows:

tup3 = tup1 + tup2
print (tup3)

#This is how you would delete a tuple

del tup3




