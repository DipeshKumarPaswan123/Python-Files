class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""Hello, how would you like to proceed?
            1. Enter 1 to create a PIN
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to check balance
            5. Enter 5 to exit
        """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        elif user_input == '5':
            print("Bye")
        else:
            print("Invalid input. Please try again.")
            self.menu()

    def create_pin(self):
        self.pin = input("Enter your PIN: ")
        print("PIN created successfully.")
        self.menu()

    def deposit(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            amount = int(input("Enter the amount to deposit: "))
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Invalid PIN.")
        self.menu()

    def withdraw(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid PIN.")
        self.menu()

    def check_balance(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            print("Your balance is", self.balance)
        else:
            print("Invalid PIN.")
        self.menu()


# Example usage
atm = Atm()
