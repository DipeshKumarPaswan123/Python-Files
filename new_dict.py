worker = {"Name": "Michle", "Age": "25", "Salary": 40000, "Company": "Linux", "Gender": "Male"}
print(type(worker))
print("Printing the worker data...")
print(worker)

print("Enter the new worker details...")


worker["Name"] = input("Name")
worker["Age"] = int(input("Age"))
worker["Salary"] = int(input("Salary"))
worker["Company"] = (input("Company"))
worker["Gender"] = (input("Gender"))
print("printing new worker data...")
print(worker)
