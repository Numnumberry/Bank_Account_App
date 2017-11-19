from tkinter import *
import pickle
import choice
import register

def checkLogin(event, username, password):
	
	customerFound = False
	
	customers = open(b'customers.txt', 'rb')	#open customer records file
	try:
		while not (customerFound):				#loop until found or eof
			c = pickle.load(customers)
			if (c.getName() == username and c.getPassword() == password):	#if matching pair, then found
				customerFound = True
				balance = c.getBalance()		#if exists, get customer balance
	except:
		pass
	customers.close()

	if (username == '' or password == ''):		#make sure not empty strings
		customerFound = False
				
	if (customerFound == True):					#if found, go to new choice frame
		print('valid login')
		choice.doChoice(username, balance)
	else:
		print('invalid login')

def login():
	
	loginFrame = Tk()
	loginFrame.title('Login')

	w = 200												#beginning of frame config
	h = 150

	ws = loginFrame.winfo_screenwidth()
	hs = loginFrame.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	loginFrame.geometry('%dx%d+%d+%d' % (w, h, x, y))	#end frame config
	
	label1 = Label(loginFrame, text = "username")		#create username label
	label1.pack()
	u = Entry(loginFrame)
	u.pack()

	label2 = Label(loginFrame, text = "password")		#create password label
	label2.pack()
	p = Entry(loginFrame)
	p.pack()

	loginButton = Button(loginFrame, text = "Login", height = 1, width = 10)			#create login button
	loginButton.bind('<Button-1>',lambda event: checkLogin(event, u.get(), p.get()))	#check the login info
	loginButton.pack()

	registerButton = Button(loginFrame, text = "Register", height = 1, width = 10)		#create register button
	registerButton.bind("<Button-1>", register.doRegister)								#go to register frame
	registerButton.pack()

	loginFrame.mainloop()
	
login()
