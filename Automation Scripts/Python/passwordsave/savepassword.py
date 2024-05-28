# use to retrieve passwords for webnsites and such
# use a database or text file
# will need to be encrypted so outside use cant view
# strong password for the file
# use of dictionary / JSON file possibly

# Use will be to retrieve password by giving the website or nicname for that site
# Example : input > google > output : PASSWORD!123



pass_dict = {
	"gmail" : "password1",
	"bank" : "password2",
	"yahoo" : "password3"

}

def get_password(user_input):
	if user_input in pass_dict:
		return pass_dict[user_input]
	else:
		return False


user_input = input("Which password: ")

x = get_password(user_input)
print(x)
