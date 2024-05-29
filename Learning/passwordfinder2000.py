import csv
from csv import writer

filename = 'test.csv'


def netPassowrdfile():
	pass


def getPassword():
	inp = input(": ")

	with open(filename, 'r') as csvfile:
		csvreader = csv.reader(csvfile)


		for row in csvreader:
			if row[0] == inp:
				print(row[1])
	csvfile.close()


def addPassword():
	with open(filename, 'a', newline='') as csvfile:

		writer_object = writer(csvfile)

		account_add = input("Account: ")
		password_add = input("Password: ")
		add = list()
		add.append(account_add)
		add.append(password_add)
		writer_object.writerow(add)
		csvfile.close()

addPassword()

getPassword()
