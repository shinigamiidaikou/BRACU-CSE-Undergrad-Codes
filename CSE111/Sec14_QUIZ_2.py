class Customer:
	def __init__(self, name, password=None):
		self.name = name
		self.password = password
		if self.password == None:
			print(f"{self.name}, password set to default. Needs to be changed.")
		else:
			print(f"{self.name} Alice has been created.")
		self.item_count = 0
		self.total_cost = 0
		self.item_dict = dict()
	def addToCart(self, *cart):
		global product_list
		if self.password == None:
			print(f"{self.name}, password needs to be changed first.")
		else:
			for i in range(0, len(cart), 2):
				if cart[i] in product_list.keys():
					if cart[i] in self.item_dict.keys():
						self.item_dict[cart[i]] += cart[i+1]
					else:
						self.item_dict[cart[i]] = cart[i+1]
						self.item_count += 1
					self.total_cost += product_list[cart[i]]*cart[i+1]
					print(f"{cart[i]} added to {self.name}'s cart.")
				else:
					print(f"Sorry! {cart[i]} is not available in the product list.")
	def setPassword(self, password):
		self.password = password
	def printDetails(self):
		global product_list
		print(f"Customer Name:{self.name}")
		if self.password == None:
			print(f"Password:****")
		else:
			print(f"Password:{'*'*len(self.password)}")
		print(f"Cart Details:")
		print(F"Total Items: {self.item_count}")
		for item, quantity in self.item_dict.items():
			print(f"Item:{item}, Units:{quantity}, Per unit price:{product_list[item]} tk, Total price:{product_list[item]*quantity} tk")
		print(f"Total Cost:{self.total_cost} taka.")


product_list={"Mango":100,"Ego Icecream":60,"Chocobar":25}
product_list["Beef"] = 650
product_list["Chicken"] = 250
product_list["Apple"] = 150
print("1.--------------------------------")
customer1 = Customer("Alice", "asdzxc1234")
print("2.--------------------------------")
customer2 = Customer("Bob")
print("3.--------------------------------")
customer1.addToCart("Mango",10,"Ego Icecream",4)
print("4.--------------------------------")
customer2.addToCart("Beef",3,"Chicken",5)
print("5.--------------------------------")
customer1.printDetails()
print("6.--------------------------------")
customer2.printDetails()
print("7.--------------------------------")
customer2.setPassword("qwerty12")
customer2.addToCart("Beef",3,"Chicken",5)
print("8.--------------------------------")
customer2.addToCart("Lichi",100,"Apple",3)
print("9.--------------------------------")
customer1.addToCart("Beef",4)
print("10.--------------------------------")
customer1.printDetails()
print("11.--------------------------------")
customer2.printDetails()


'''
Expected OUTPUT:
>>> 1.--------------------------------
>>> User Alice has been created.
>>> 2.--------------------------------
>>> Bob, password set to default. Needs to be changed.
>>> 3.--------------------------------
>>> Mango added to Alice's cart.
>>> Ego Icecream added to Alice's cart.
>>> 4.--------------------------------
>>> Bob, password needs to be changed first.
>>> 5.--------------------------------
>>> Customer Name:Alice
>>> Password:**********
>>> Cart Details:
>>> Total Items: 2
>>> Item:Mango, Units:10, Per unit price:100 tk, Total price:1000 tk
>>> Item:Ego Icecream, Units:4, Per unit price:60 tk, Total price:240 tk
>>> Total Cost:1240 taka.
>>> 6.--------------------------------
>>> Customer Name:Bob
>>> Password:****
>>> Cart Details:
>>> Total Items: 0
>>> Total Cost:0 taka.
>>> 7.--------------------------------
>>> Beef added to Bob's cart.
>>> Chicken added to Bob's cart.
>>> 8.--------------------------------
>>> Sorry! Lichi is not available in the product list.
>>> Apple added to Bob's cart.
>>> 9.--------------------------------
>>> Beef added to Alice's cart.
>>> 10.--------------------------------
>>> Customer Name:Alice
>>> Password:**********
>>> Cart Details:
>>> Total Items: 3
>>> Item:Mango, Units:10, Per unit price:100 tk, Total price:1000 tk
>>> Item:Ego Icecream, Units:4, Per unit price:60 tk, Total price:240 tk
>>> Item:Beef, Units:4, Per unit price:650 tk, Total price:2600 tk
>>> Total Cost:3840 taka.
>>> 11.--------------------------------
>>> Customer Name:Bob
>>> Password:********
>>> Cart Details:
>>> Total Items: 3
>>> Item:Beef, Units:3, Per unit price:650 tk, Total price:1950 tk
>>> Item:Chicken, Units:5, Per unit price:250 tk, Total price:1250 tk
>>> Item:Apple, Units:3, Per unit price:150 tk, Total price:450 tk
>>> Total Cost:3650 taka.
'''