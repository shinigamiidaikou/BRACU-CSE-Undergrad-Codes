class Student:
	def __init__(self, n, id, dep):
		self.name = n
		self.ID = id
		self.dept = dep
		self.courses = list()
		print(f"{n} has been created")
	def printDetails(self):
		print(f"Name: {self.name}")
		print(f"ID: {self.ID}")
		print(f"Dept: {self.dept}")
		print("Courses:")
		for i in range(len(self.courses)):
			print(self.courses[i])
	def addCourse(self, *course_tuple):
		self.courses = list(course_tuple)


#Driver Code:
st1  = Student('Farah', 22101185, 'CSE')
st2 = Student('Sreshtho', 21101235, 'CSE ')
print('1. ---------------------------------------')
st1.addCourse('CSE111', 'STA201', 'ENG101', 'MAT110')
st2.addCourse('CSE111', 'CSE260', 'MAT120')
print('2. ---------------------------------------')
st1.printDetails()
print('3. ---------------------------------------')
st2.printDetails()
print('4. ---------------------------------------')
