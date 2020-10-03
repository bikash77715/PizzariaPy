
import logging

# logging.disable(logging.INFO)

logging.basicConfig(level = logging.INFO, format = '%(levelname)s-%(message)s')

class Order:

	def __init__(self):

		self.pizzaList = []
	
	
	def getPizzaList(self):
		return self.pizzaList;
	
	def addPizza(self, pizza):
		self.pizzaList.append(pizza);

	def setDeliveryType(self, deliver=False):
		self.deliver = deliver
		logging.info("in order deliver = "+str(deliver))
		
	def getDeliveryType(self):
		return self.deliver

	def setInfo(self, info):
		self.custInfo = info
	
	def getInfo(self):
		return self.custInfo
	
	def getCost(self):
		cost = 0

		for p in self.pizzaList:
			cost+= p.getPrice()
		
		if self.deliver:
			if(cost<30):
				cost += 8
						
		return cost


