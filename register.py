from tkinter import *
import pickle
import classes

def printSuccess():

	successFrame = Tk()
	successFrame.title('Success')
	
	w = 200
	h = 50

	ws = successFrame.winfo_screenwidth()
	hs = successFrame.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	successFrame.geometry('%dx%d+%d+%d' % (w, h, x, y))
	
	label = Label(successFrame, text='REGISTERED').pack()

def register(event, username, password):
	
	validUsername = True
	
	customers = open(b'customers.txt', 'rb')
	try:
		while (True):						#scan file
			c = pickle.load(customers)
			if (c.getName() == username):	#if username already exists
				validUsername = False		#then the username is not valid
	except:
		pass
	customers.close()
	
	if (validUsername):
		customers = open(b'customers.txt', 'ab')
		c = classes.Customer(username, password, 0.00)
		pickle.dump(c, customers)
		customers.close()
		print('registered')
		printSuccess()
	else:
		print('invalid username')

def doRegister(event):

	registerFrame = Tk()
	registerFrame.title('Register')

	w = 200
	h = 150

	ws = registerFrame.winfo_screenwidth()
	hs = registerFrame.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	registerFrame.geometry('%dx%d+%d+%d' % (w, h, x, y))

	label1 = Label(registerFrame, text = "username")
	label1.pack()
	u = Entry(registerFrame)
	u.pack()
	
	label2 = Label(registerFrame, text = "password")
	label2.pack()
	p = Entry(registerFrame)
	p.pack()

	registerButton = Button(registerFrame, text = "Create Account", height = 1, width = 10)
	registerButton.bind('<Button-1>',lambda event: register(event, u.get(), p.get()))
	registerButton.pack()
	
	registerFrame.mainloop()
