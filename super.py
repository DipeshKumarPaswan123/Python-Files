class Parent:
    def show(self):
        print("This is from Parent Class")

class Child(Parent):
    def show(self):
        super().show()
        print("This is Child Class")
