'''

Description:

Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array or list ( depending on language ).
Examples

count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]

'''

def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    c=list()
    for i in range(n):
    	c.append((i+1)*x)

    return c


print(count_by(1,10))