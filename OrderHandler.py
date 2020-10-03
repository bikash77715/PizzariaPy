import Order, Pizza, logging

logging.disable(logging.INFO)

logging.basicConfig(level = logging.INFO, format = '%(levelname)s-%(message)s')

class OrderHandler:
	
	def __init__(self):
		self.newOrder = Order.Order()
		self.toppings = ["Bacon", "Olives", "Ham", "Mushrooms", "Pineapple", "Salami", "Anchovies"]

	
	# adds pizza to the orderlist
	def generateOrder(self, size):
		pizza = Pizza.Pizza(size)
		
		print(" Default toppings are: "+ str(pizza.getToppings()))
		self.printSeperator()		
		
		choice = input(" Default? (y/n): ")
		while(True):

			if choice.lower() == 'y':
				self.newOrder.addPizza(pizza)
				
				print(" Pizza is added. ")
				self.printSeperator()
				break
			
			elif choice.lower() == 'n':
				pizza.setToppings(self.getToppings(pizza))
				self.newOrder.addPizza(pizza)
				
				print(" Pizza is added. ")
				self.printSeperator()
				break
			
			else:
				choice = input(" PLEASE ENTER VALID INPUT: (Y/N) OR (y/n): ")
			
	# sets toppings for current pizza
	def getToppings(self, pizza):
		# TODO Auto-generated method stub
		
		addedToppings = set()
		print(" Topping options are: ")
		
		for i in range(len(self.toppings)):
			print(" (" + str(i+1) + ") "+ self.toppings[i])
		
		print (" enter 0 to finalize or the topping number to add: ")
		
		while(True):
			try:
				while(len(addedToppings)<4):
					logging.info(" len(addedToppings) = "+str(len(addedToppings)))
					choice = int(input())
					logging.info(" choice = "+ str(choice))

					if(choice > 0 and choice <= len(self.toppings)):
						addedToppings.add(self.toppings[choice-1])

					elif (choice == 0):
						if(len(addedToppings)==0):
							print(" Add at least one topping!")
							continue	
					
						break
									
					else:
						print(" PLEASE ENTER A VALID NUMBER: (0-"+ (len(self.toppings)+1)+")")
				
				print(" Toppings have been finalized.")

				break
				
			except:
				print(" Wrong inputs! Try again.");
				
		return addedToppings

	def deliveryOption(self):
		# TODO Auto-generated method stub
		loop = True
		print(" Delivery option: \n (1) Collected \n (2) Delivered \n")
		while(loop):
			try:
				choice = int(input())
				self.printSeperator()
				
				if choice == 1:
					print("")
					self.newOrder.setDeliveryType(False)
					loop = False
					break
					
				elif choice == 2:
					self.newOrder.setDeliveryType(True)
					loop = False
					break
					
				else:
					raise ValueError
			except:
				print(" Wrong input! try again ")		
		self.getCustInfo()

	def getCustInfo(self):
		name = input(" Enter name: ")
		
		while(True):
			try:
				phone = int(input(" Enter phone: "))
				if(self.newOrder.getDeliveryType()):
					address = input(" Enter address: ")
					self.newOrder.setInfo(" Name: "+ name+"\n Phone "+str(phone)+"\n Address: "+ address)
				
				
				else:
					self.newOrder.setInfo(" Name: "+ name+" \n Phone "+str(phone)+"");
					
				break			
			except:
				print(" Unexpected input. Try again")
				
			
			

	def generateReport(self):
		self.printSeperator()
		self.printSeperator()
		print("Order Report")
		self.printSeperator()
		self.printSeperator()

		print(" Customer info: \n"+ self.newOrder.getInfo())
		print(" Delivered: "+ str(self.newOrder.deliver))
		# print(" Delivered: "+ str(self.newOrder.getDeliveryType()))
		self.printSeperator()

		size = ["Small", "Medium", "Large"]
		print(" Pizza size \t\t Toppings \t \t \t\t Price ")
		for p in self.newOrder.getPizzaList():
			print(" "+size[p.getSize()-1]+" \t\t "+str(p.getToppings())+" \t "+ str(p.getPrice()))
		
		print(" Total cost: "+ str(self.newOrder.getCost()))
		self.printSeperator()
	
	def printSeperator(self):
		print("*"*100)
		
