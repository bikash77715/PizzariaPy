
class Pizza:
	def __init__(self, size):
		self.size = size
		if size == 1:
			self.toppings = {"Salami", "Ham", "Mushrooms", "Olives"}
			self.basePrice = 5

		elif size == 2:
			self.toppings = {"Salami", "Bacon", "Mushrooms", "Olives"}
			self.basePrice = 8

		elif size == 3:
			self.toppings = {"Salami", "Ham", "Anchovies", "Olives"}
			self.basePrice = 12

	def setToppings(self, toppings):
		self.toppings = toppings

	def getSize(self):
		return self.size

	def getToppings(self):
		return self.toppings

	def getPrice(self):
		
		return self.basePrice + len(self.toppings)
		# return (self.basePrice += len(self.toppings))


