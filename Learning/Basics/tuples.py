#!/bin/python

# Tuples
# immutable, cant moddified once created

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

d = {'a':10, 'c':22, 'd': 1}
print(d)
# dict_itmes = d.items()
# print(type(dict_itmes))
# t = sorted(d.items())
# print(t)

# for k,v in sorted(d.items()):
# 	print(k,v)

# tmp = list()

# for k,v in d.items():
# 	tmp.append((v,k))

# print(tmp)
# print(sorted(tmp, reverse=False))

# print(sorted(tmp, reverse=True))


print(sorted([(v,k) for k,v in d.items()])) # combined and better looking list comprehinsion

