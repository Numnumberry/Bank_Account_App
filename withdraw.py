from tkinter import *
import os
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
	
	label = Label(successFrame, text='SUCCESS').pack()

def withdraw(event, username, amount):
	
	balanceFound = False
	
	customers = open(b'customers.txt', 'rb')
	try:
		while not (balanceFound):						#find users current balance
			c = pickle.load(customers)
			if (c.getName() == username):
				balance = c.getBalance()
				balanceFound = True
	except:
		pass
	customers.close()
	
	balance = balance - float(amount)			#get new balance
	
	if (balance < 0):
		print('not enough funds')
	else:
		customers = open(b'customers.txt', 'rb')
		temp = open(b'temp.txt', 'wb')
		try:
			while (True):						#write updated balance to temp file
				c = pickle.load(customers)
				if (c.getName() == username):	#see if new or old balance to write
					c.setBalance(balance)
					pickle.dump(c, temp)
				else:
					pickle.dump(c, temp)
		except:
			pass
		customers.close()
		temp.close()
	
		customers = open(b'customers.txt', 'wb')
		temp = open(b'temp.txt', 'rb')
		try:
			while (True):						#update customers file
				pickle.dump(pickle.load(temp), customers)
		except:
			pass
		customers.close()
		temp.close()
		
		printSuccess()
		
		transFile = open(b'transactions.txt', 'ab')
		t = classes.Transaction(username, 'W', float(amount), balance)
		pickle.dump(t, transFile)
		transFile.close()
		
		print('successful withdraw')
	
		os.remove('temp.txt')

def doWithdraw(event, username):
	withdrawFrame = Tk()
	withdrawFrame.title('Withdraw')

	w = 200
	h = 200

	ws = withdrawFrame.winfo_screenwidth()
	hs = withdrawFrame.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	withdrawFrame.geometry('%dx%d+%d+%d' % (w, h, x, y))

	amountLabel = Label(withdrawFrame, text = "Amount:")
	amountLabel.pack()
	
	a = Entry(withdrawFrame)
	a.pack()
	
	button = Button(withdrawFrame, text = "Withdraw", height = 2, width = 20)
	button.bind('<Button-1>',lambda event: withdraw(event, username, a.get()))
	button.pack()
