# URL: https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
# The main idea is to count all the occurring characters in a string. If you have a string 
# like aba, then the result should be {'a': 2, 'b': 1}.
# What if the string is empty? Then the result should be empty object literal, {}.

def count(s):
    # The function code should be here
    re = {}
    for a in s:
        re[a]= re.get(a,0) + 1
    return re

print(count('assbs'))


# another solution from site
# def count(s):
#     return {i: s.count(i) for i in s}
# seems about the same speed
