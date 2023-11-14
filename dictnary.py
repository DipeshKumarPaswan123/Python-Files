'''Dict = {"Name": "Ayush", "Age": 25 }
print(type(Dict))
print("prirnting employee data...")
print(Dict)'''


# Accessing the dictionary value

'''Employee = {"Name": "John", "Age": 30, "Salary": 35000, "Company": "GOOGLE"}
print(type(Employee))
print("Printing thw employee data...")
print(Employee)
print("Name : %s" % Employee["Name"])
print("Age : %d" % Employee["Age"])
print("Salary : %d" % Employee["Salary"])
print("Company : %s" % Employee["Company"])'''

# Updating Dictionary Value
Employee = {}
Employee["Name"] = input("Name")
Employee["Age"] = int(input("Age"))
Employee["Salary"] = int(input("Salary"))
Employee["Company"] = (input("Company"))
print("Name :%s" % Employee["Name"])
print("Age : %d" % Employee["Age"])
print("Salary: %d" % Employee["Salary"])
print("Company : %s" % Employee["Company"])
