from tkinter import *
import pickle

def doTransactions(event, username):
	transactionsFrame = Tk()
	transactionsFrame.title('Transactions')

	w = 200
	h = 200

	ws = transactionsFrame.winfo_screenwidth()
	hs = transactionsFrame.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	transactionsFrame.geometry('%dx%d+%d+%d' % (w, h, x, y))

	l = Listbox(transactionsFrame)
	
	knt = 0
	transactions = open(b'transactions.txt', 'rb')
	try:
		while (True):
			t = pickle.load(transactions)
			if (t.getCustName() == username):
				l.insert(knt, t.getTransType() +' | '+ \
				format(t.getAmount(), '8.2f') +' | '+ \
				format(t.getNewBalance(), '8.2f'))
	except:
		pass
	
	l.pack()


 
