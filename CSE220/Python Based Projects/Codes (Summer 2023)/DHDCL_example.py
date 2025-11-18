class DoublyNode:
    def __init__(self, elem, next=None, prev=None):
        self.elem = elem
        self.next = next
        self.prev = prev


class Patient:
    def __init__(self, id, name, age, bloodgroup):
        self.id = id
        self.name = name
        self.age = age
        self.bloodgroup = bloodgroup


class WRM:
    def __init__(self):
        self.head = DoublyNode(None)
        self.head.next = self.head
        self.head.prev = self.head

    def registerPatient(self, id, name, age, bloodgroup):
        patient = Patient(id, name, age, bloodgroup)
        new_node = DoublyNode(patient)
        last_node = self.head.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.head
        self.head.prev = new_node
        print("New Patient Registered Successfully")

    def servePatient(self):
        if self.head.next == self.head:  # If the list is empty
            return None
        first_node = self.head.next
        second_node = first_node.next
        patient = first_node.elem
        self.head.next = second_node
        second_node.prev = self.head
        return patient

    def cancelAll(self):
        if self.head.next == self.head:  # If the list is empty
            print("Nothing to cancel.")
        else:
            self.head.next = self.head
            self.head.prev = self.head
            print("Canceled All!")

    def canDoctorGoHome(self):
        return self.head.next == self.head

    def showAllPatients(self):
        if self.head.next == self.head:  # If the list is empty
            print("No patients in the waiting room.")
        else:
            current_node = self.head.next
            while current_node != self.head:
                print("Patient ID:", current_node.elem.id)
                current_node = current_node.next



wrm1 = WRM()
print("=========================")
wrm1.registerPatient(234, "Shakil Rahman", 24, "O+")
wrm1.registerPatient(142, "Zayma Zaman", 21, "A+")
wrm1.registerPatient(475, "Fardin Mashrafi", 34, "AB-")
wrm1.registerPatient(901, "Aysha Mumtaz", 27, "B-")
print("=========================")
current_patient = wrm1.servePatient()
print(current_patient.name)
print("=========================")
wrm1.showAllPatients()
print("=========================")
print(wrm1.canDoctorGoHome())
print("=========================")
wrm1.cancelAll()
print("=========================")
print(wrm1.canDoctorGoHome())
print("=========================")
wrm1.cancelAll()