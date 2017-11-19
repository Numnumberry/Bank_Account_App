from tkinter import *

import withdraw
import deposit
import transactions

def doChoice(username, balance):

	choiceFrame = Tk()
	choiceFrame.title('Options')

	w = 200
	h = 200

	ws = choiceFrame.winfo_screenwidth()
	hs = choiceFrame.winfo_screenheight()

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	choiceFrame.geometry('%dx%d+%d+%d' % (w, h, x, y))
	
	balanceLabel = Label(choiceFrame, text = "Balance:")						#create balance label
	balanceLabel.pack()
	
	amountLabel = Label(choiceFrame, text = '$' + format(balance, '.2f'))		#create amount label
	amountLabel.pack()

	button1 = Button(choiceFrame, text = "Withdraw", height = 2, width = 20)
	button1.bind('<Button-1>',lambda event: withdraw.doWithdraw(event, username))
	button1.pack()

	button2 = Button(choiceFrame, text = "Deposit", height = 2, width = 20)
	button2.bind("<Button-1>",lambda event: deposit.doDeposit(event, username))
	button2.pack()

	button3 = Button(choiceFrame, text = "Transactions", height = 2, width = 20)
	button3.bind("<Button-1>",lambda event: transactions.doTransactions(event, username))
	button3.pack()

    #choiceFrame.mainloop()
