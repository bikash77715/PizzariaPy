import OrderHandler, logging

logging.disable(logging.INFO)
logging.basicConfig(level = logging.INFO, format = '%(levelname)s-%(message)s')

orderHandler = OrderHandler.OrderHandler()
	
def menu():
	logging.info("inside menu")
	printSeperator()
	addNewPizza = True
	while(addNewPizza):
		print(" Pizza Menu:")
		print(" (1) Small \n (2) Medium \n (3) Large \n (0) Finish order");
		printSeperator()
		loop = True
		while (loop):
			try:
				choice  = int(input(" Select pizza size: "))
				if choice not in range(0, 4):
					raise ValueError

				elif choice == 0:
					addNewPizza = False
					print(" Finalizing order ")
					printSeperator()

				else:
					logging.info(" processing selection")
					processSelection(choice)
				loop = False

			except:
				wrapMessage(" Unexpected input! Enter a number from the menu. ")		

	orderHandler.deliveryOption()
	orderHandler.generateReport()

def processSelection(choice):
	logging.info("inside processSelection()")
	if choice == 1:
		print(" Small pizza selected. ")

	elif choice == 2:
		print(" Medium pizza is selected")

	elif choice == 3:
		print(" Large pizza is selected")

	orderHandler.generateOrder(choice)

def printSeperator():
	print("*"*100)

def wrapMessage(msg):
	print('+'*(len(msg)+2))
	print('+' + msg+'+')
	print('+'*(len(msg)+2))