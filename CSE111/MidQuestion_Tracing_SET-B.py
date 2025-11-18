class MidA:
	def __init__(self):
		self.x = 5
		self.y = 3
		self.sum = 0
	def MethodA(self, x):
		self.y = x + self.sum + self.x
		self.sum = self.y + x
		z = MidA()
		self.MethodB(z)
		print(self.x, self.y, self.sum)
	def MethodB(self, a):
		y = 4
		a.x = a.x + self.sum
		self.sum = a.x + a.y + y
		a.sum = self.sum + self.x
		print(a.x, a.y, a.sum)


a = MidA()
a.MethodA(6)

