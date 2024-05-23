# Create a password generater for a fixed length
# Save to a file that is encrypted
# use random number and use that for ascii characters


import random
import sys


def password_creator(length):
	pass_lst = []
	for x in range(length):
		ran = random.randint(33,126)
		pass_lst.append(chr(ran))

	return pass_lst


pc = password_creator(int(sys.argv[1]))
t="".join(pc)
print(f"Password: {t}")