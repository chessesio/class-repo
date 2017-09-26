#MEST is throwing a crazy networking party.
# They need us to write software to register guests.
# A. Store guests (name, email) in a dictionary
# B. Given a name, output an email

# _________________________________________________

# C. Send an email to all guests thanking them for showing
# D. If the guest has an odd number of letters in their name, send them a different email, telling them they are unwellcome at future events

from smtplib import SMTP

guests={}

def add_guests(name,email):
	guests[name] = email

def list_guests():
	for guest,email in guests.items():
		print(guest,email)

def say_thankyou():
	for guest_name, guest_email in guests.items():

		host = "smtp.gmail.com"
		port = 587
		username = "chessmestclass@gmail.com"
		password = "weakpassword"

		email_connection = SMTP(host, port)
		email_connection.ehlo()
		email_connection.starttls()
		email_connection.login(username,password)
		
		if len(guest_name) % 2 == 0:
			email_connection.sendmail(username, guest_email,"Thank you {} for showing up. Come again next time".format(guest_name))

		else:
			email_connection.sendmail(username, guest_email,"Thank you {} for showing up but you are unwelcom at future events!".format(guest_name))

		email_connection.quit()

a = 0

while a != 3:

	a = 0
	choice = input("Make a choice:\n1 to add guest\n2 to list guestss\n3 to send thank you email\n4 to exit\n")
	
	if choice == "1":
		name = input("Enter guest's name:\n")
		email = input("Enter guest's email:\n")
		add_guests(name,email)

	elif choice == "2":
		list_guests()

	elif choice == "3":
		say_thankyou()

	elif choice == "4":
		a = 3

	else:
		print("Choose wisely! Invalid choice!!!")