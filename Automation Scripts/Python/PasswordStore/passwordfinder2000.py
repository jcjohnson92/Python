import csv
from csv import writer

# filename = 'test.csv'


def newPassowrdfile():
	new_filename = input("Filename: ")
	with open(new_filename,'r') as csvfile:
		csvfile.close()

	addnew = input("Would you like to add new password [y/n]: ")

	if addnew =='y':
		addPassword(new_filename)
		exit()


def getPassword(f):
	inp = input(": ")

	with open(f, 'r') as csvfile:
		csvreader = csv.reader(csvfile)


		for row in csvreader:
			if row[0] == inp:
				print(row[1])
				exit()
		csvfile.close()
		print("Does not exist")
		exit()


def addPassword(f):
	with open(f, 'a', newline='') as csvfile:

		writer_object = writer(csvfile)
		csvreader=csv.reader(csvfile)

		account_add = input("Account: ")
		checkAccount(f,account_add)
		password_add = input("Password: ")

		add = list()
		add.append(account_add)
		add.append(password_add)
		writer_object.writerow(add)
		csvfile.close()
		exit()

def checkAccount(f,inp):
	with open(f, 'r', newline='') as csvfile:
		csvreader=csv.reader(csvfile)

		for row in csvreader:
			if row[0] == inp:
				print("Already exits")
				main()


def main():
	menu_dict = {'1':'New Passowrd File', '2':'Add Password', '3':'Get Password'}

	for k,v in menu_dict.items():
		print(k,v)
	
	user_input = input("Select Option : ")

	if user_input == '1':
		newPassowrdfile()
	elif user_input == '2':
		filename = input("Filename: ")
		addPassword(filename)
	elif user_input== '3':
		filename = input("Filename: ")
		getPassword(filename)
	else:
		print("INVALID Choice")
		exit()


main()