class Employee:
    id = 10
    name = "John"

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))

    # Creating an emp instance of Employee class


emp = Employee()

# Deleting the id property of emp object
del emp.id

# Deleting the emp object itself
del emp

# This will raise a NameError because emp no longer exists
try:
    emp.display()
except NameError as e:
    print("An error occurred:", e)
