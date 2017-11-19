#import pickle

class Customer:
	def __init__(self, name, password, balance):
		self.__name = name
		self.__password = password
		self.__balance = balance
	def setName(self, name):
		self.__name = name
	def setPassword(self, password):
		self.__password = password
	def setBalance(self, balance):
		self.__balance = balance
	def getName(self):
		return self.__name
	def getPassword(self):
		return self.__password
	def getBalance(self):
		return self.__balance
		
class Transaction:
	def __init__(self, custName, transType, amount, newBalance):
		self.__custName = custName
		self.__transType = transType
		self.__amount = amount
		self.__newBalance = newBalance
	def setCustName(self, custName):
		self.__custName = custName
	def setTransType(self, transType):
		self.__transType = transType
	def setAmount(self, amount):
		self.__amount = amount
	def setNewBalance(self, newBalance):
		self.__newBalance = newBalance
	def getCustName(self):
		return self.__custName
	def getTransType(self):
		return self.__transType
	def getAmount(self):
		return self.__amount
	def getNewBalance(self):
		return self.__newBalance
		

#c = Customer('Bob', 54)

#pickle.dump(c, open('yes.txt', 'wb'))
#umph = pickle.load(open('yes.txt', 'rb'))

#print(umph.getName())
