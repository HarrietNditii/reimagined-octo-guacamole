class CoffeeMachine:
    def __init__(self) -> None:
        #resources in the machine
        self.resources ={
            "water": 1000, #ml
            "milk": 500, #ml
            "coffee": 200, #g
        }

        self.menu = {
            "espresso":{"water":50, "milk": 0, "coffee":18},
            "latte":{"water": 200, "milk": 150, "coffee": 24},
            "cappuccino":{"water": 250,"milk": 100,"coffee":24},

        }
        self.money = 0

    def display_menu(self):
        print("Menu:")
        for drink, ingredients in self.menu.items():
            print(f" - {drink.capitalize()}:")
            for ingredient, amount in ingredients.items():
                print(f"  {ingredient}: {amount}ml")


    def check_resources(self, drink):
        """Check if there are enough resources for the selected drink."""
        for ingredient, amount in self.menu[drink].items():
            if self.resources[ingredient] < amount:
                print(f"Sorry, not enough {ingredient}.")
                return False
        return True
    
    def make_drink(self, drink):
        """Deduct resources and make the drink if resources are sufficient."""
        if self.check_resources(drink):
            for ingredient, amount in self.menu[drink].items():
                self.resources[ingredient] -= amount
            self.money += 2.5  # Adding price for simplicity
            print(f"Here is your {drink}! Enjoy!")
        else:
            print("Cannot make the drink due to insufficient resources.")

    def display_resources(self):
        print("Current resources:")
        for resource, amount in self.resources.items():
            print(f" - {resource.capitalize()}: {amount}ml")

# Example usage
coffee_machine = CoffeeMachine()
coffee_machine.display_menu()
coffee_machine.make_drink("latte")
coffee_machine.display_resources()