class Laptop:
	def __init__(self, name=None):
		self.name = name
		self.features = dict()
	def setName(self, name):
		self.name = name
	def addFeature(self, component, specs):
		if self.name == None:
			print("Feature can not be added without laptop name\n")
		else:
			self.features[component] = specs
	def printDetail(self):
		print(f"Laptop Name:{self.name}")
		for component, specs in self.features.items():
			print(f"{component}:{specs}")
	def giveDetail(self):
		feature_details = f"Laptop Name:{self.name}\n"
		for component, specs in self.features.items():
			feature_details += f"{component}:{specs}\n"
		return feature_details[:-1]


L1=Laptop()
print("=================")
L1.addFeature("Display","15.6 inch")
print("====================")
L1.setName("Asus Vivobook 15")
L1.addFeature("Display","15.6 inch")
L1.printDetail()
print("========================")
L2=Laptop("Lenovo IdeaPad 3")
L2.addFeature("Display","14 inch")
L2.addFeature("Ram","8 GB")
print("===================")
L2.printDetail()
L2.addFeature("CPU","Intel i5")
print("=========================")
print(L2.giveDetail())
print("=======================")


## ===================================================================================
## ===================================================================================

'''
EXPECTED OUTPUT:
>>> ========================
>>> Feature can not be added without laptop name
>>> 
>>> ======================================
>>> Laptop Name:Asus Vivobook 15
>>> Display:15.6 inch
>>> ====================================
>>> ======================================
>>> Laptop Name:Lenovo IdeaPad 3
>>> Display:14 inch
>>> Ram:8 GB
>>> ======================================
>>> Laptop Name:Lenovo IdeaPad 3
>>> Display:14 inch
>>> Ram: 8 GB
>>> CPU: Intel i5
>>> ================================
'''