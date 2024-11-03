class CoffeeMachine:
    def __init__(self) -> None:
        self.water = 500  # ml
        self.milk = 200
        self.coffee_beans = 100  # grams
        self.cups = 10
        self.money = 0  # initial

    def display_menu(self):
        print("Welcome to my Coffee Machine!") 
        print("1. Espresso - ksh 300")
        print("2. Latte - ksh 400")
        print("3. Cappuccino - ksh 500")
        print("4. Check inventory")
        print("5. Exit")

    def check_inventory(self, water_needed, milk_needed, coffee_needed):
        if self.water < water_needed:
            print("Not enough water!")
            return False
        if self.milk < milk_needed:
            print("Not enough milk!")
            return False
        if self.coffee_beans < coffee_needed:
            print("Not enough coffee beans!")
            return False
        if self.cups < 1:
            print("Not enough cups!")
            return False
        return True

    def make_coffee(self, coffee_type):
        if coffee_type == "espresso":
            if self.check_inventory(50, 0, 18):
                self.water -= 50
                self.coffee_beans -= 18
                self.cups -= 1
                self.money += 300
                print("Your Espresso is ready!")
        elif coffee_type == "latte":
            if self.check_inventory(200, 150, 24):
                self.water -= 200
                self.milk -= 150
                self.coffee_beans -= 24
                self.cups -= 1
                self.money += 400
                print("Your Latte is ready!")
        elif coffee_type == "cappuccino":
            if self.check_inventory(250, 100, 24):
                self.water -= 250
                self.milk -= 100
                self.coffee_beans -= 24
                self.cups -= 1
                self.money += 500
                print("Your Cappuccino is ready!")

    def show_inventory(self):
        print("Current inventory:")
        print(f"Water: {self.water} ml")
        print(f"Milk: {self.milk} ml")
        print(f"Coffee beans: {self.coffee_beans} g")
        print(f"Cups: {self.cups}")
        print(f"Money: ksh {self.money}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option (1-5): ")

            if choice == '1':
                self.make_coffee("espresso")
            elif choice == '2':
                self.make_coffee("latte")
            elif choice == '3':
                self.make_coffee("cappuccino")
            elif choice == '4':
                self.show_inventory()
            elif choice == '5':
                print("Coffee Machine turned off!")
                break
            else:
                print("Invalid choice. Please try again.")

# Running the coffee machine
coffee_machine = CoffeeMachine()
coffee_machine.run()
