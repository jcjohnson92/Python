# commonwords.py
#!/bin/python

file = open('text.txt') # open a file
 
text_dict = dict() # create a new dictionary

for f in file: 
	words = f.split() #split the words in each line to a seperate value
	for word in words:
		# print(word)
		text_dict[word] = text_dict.get(word,0) +1 # add and count words

x = sorted( [(v,k) for k,v in text_dict.items()  ], reverse=True )
print(x[0])
# print(text_dict)
# sort_list = list() 
# for k,v in text_dict.items():
# 	sort_list.append((v,k))
# # print("\n\n\n\n\n")

# x = sorted(sort_list,reverse=True)
# print(x[0])