#dict.py




# jjj = {'k': 1, 'l':2, 'g':3}

# for i in jjj:
# 	print(i ," :", jjj[i])


# for k,v in jjj.items():
# 	print(k,v)


text = "What is Lorem Ipsum? Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

texts = text.split()
print(texts)

empty= dict()

for x in texts:
	empty[x] = empty.get(x,0) + 1

print(empty)