class Coffee:
    def __init__(self, name, description, base_price):
        self.name = name
        self.description = description
        self.base_price = base_price
    
    def __str__(self):
        return f"{self.name:<12} | {self.description:<50} | ${self.base_price:.2f}"

# test_coffee = Coffee("Latte", "Creamy espresso with steamed milk", 3.50)
# print(test_coffee)

class Order:
    def __init__(self, coffee, size):
        self.coffee = coffee
        self.size = size
        self.price = self.calculate_price()

    def calculate_price(self):
        extra_cost = 0.0
        if self.size == "Medium":
            extra_cost = 0.50
        elif self.size == "Large":
            extra_cost = 1.00
        
        return self.coffee.base_price + extra_cost
    
    def __str__(self):
        return f"{self.size} {self.coffee.name} - ${self.price:.2f}"
    

class Cafe:
    def __init__(self, name, tax_rate=0.08):
        self.name = name
        self.menu = []
        self.orders = []
        self.tax_rate = tax_rate

    def add_to_menu(self, coffee):
        """Add a Coffee object to the menu list."""
        self.menu.append(coffee)

    def display_menu(self):
        """Print the full menu with numbers so the customer can pick."""
        print(f"\n=== {self.name.upper()} MENU ===")
        for i, coffee in enumerate(self.menu, 1):
            print(f"{i}. {coffee}")

    def display_sizes(self):
        """Print the available sizes."""
        print("1. Small (+$0.00)")
        print("2. Medium (+$0.50)")
        print("3. Large (+$1.00)")

    def add_order(self, coffee, size):
        """Create a new Order and add it to the orders list."""
        new_order = Order(coffee, size)
        self.orders.append(new_order)
        print(f"\n✅ Added: {new_order}")

    def calculate_subtotal(self):
        """Add up the price of every order and return the total."""
        total = 0
        for item in self.orders:
            total += item.price
        return total

    def print_bill(self, tip_percent):
        """Print a formatted receipt with subtotal, tax, tip, and grand total."""
        subtotal = self.calculate_subtotal()
        tax = subtotal * self.tax_rate
        tip = subtotal * (tip_percent / 100)
        total = subtotal + tax + tip

        print("\n" + "="*42)
        print(f"{self.name.upper()} - YOUR BILL")
        print("="*42)

        for item in self.orders:
            item_dispaly = f"{item.size} {item.coffee.name}"
            print(f" {item_dispaly:<30} ${item.price:>6.2f}")
        
        print("-"*42)
        print(f" {'Subtotal:':<30} ${subtotal:>6.2f}")
        print(f" {f'Tax ({self.tax_rate*100:.0f}%):':<30} ${tax:>6.2f}")
        print(f" {f'Tip ({tip_percent}%):':<30} ${tip:>6.2f}")
        print("="*42)
        print(f" {'TOTAL:':<30} ${total:>6.2f}")
        print("="*42)


# --- SETUP ---
cafe = Cafe("Sunny Bean Café", tax_rate=0.08)

# Create Coffee objects and add them to the menu
cafe.add_to_menu(Coffee("Espresso",    "Strong and bold shot of coffee",           2.50))
cafe.add_to_menu(Coffee("Americano",   "Espresso diluted with hot water",          3.00))
cafe.add_to_menu(Coffee("Cappuccino",  "Equal parts espresso, foam, and milk",     3.75))
cafe.add_to_menu(Coffee("Latte",       "Creamy espresso with lots of steamed milk",3.50))
cafe.add_to_menu(Coffee("Flat White",  "Velvety milk with a double espresso shot", 4.00))
cafe.add_to_menu(Coffee("Macchiato",   "Espresso 'stained' with a touch of foam",  3.25))
cafe.add_to_menu(Coffee("Mocha",       "Espresso with chocolate and steamed milk", 4.25))
cafe.add_to_menu(Coffee("Cold Brew",   "Slow-steeped coffee served cold",          4.00))


SIZES = ["Small", "Medium", "Large"]

print(f"\nWelcome to {cafe.name}! ☕")

while True:
    print("\n" + "="*40)
    print("What would you like to do?")
    print("1. View menu and order a drink")
    print("2. View current order")
    print("3. Checkout and pay")
    print("="*40)

    choice = input("Enter your choice (1/2/3): ").strip()

    match choice:
        case "1":
                # Show menu
            cafe.display_menu()

            # Ask the customer to pick a drink (validate input!)
            drink_input = input("\nEnter the number of the drink you want (or 0 to cancel): ").strip()

            if drink_input == "0":
                continue   # go back to the top of the while loop

            # Check that the input is a valid number
            if not drink_input.isdigit():
                print("❌ Please enter a number.")
                continue

            drink_index = int(drink_input) - 1   # subtract 1 because lists start at 0

            if drink_index < 0 or drink_index >= len(cafe.menu):
                print("❌ That number is not on the menu. Try again.")
                continue

            selected_coffee = cafe.menu[drink_index]

            # Show sizes
            cafe.display_sizes()
            size_input = input("Enter the number of the size you want: ").strip()

            if not size_input.isdigit():
                print("❌ Please enter a number.")
                continue

            size_index = int(size_input) - 1

            if size_index < 0 or size_index >= len(SIZES):
                print("❌ Invalid size. Try again.")
                continue

            selected_size = SIZES[size_index]

            # Add the order
            cafe.add_order(selected_coffee, selected_size)

        case "2":
            if not cafe.orders:
                print("\n🛒 Your order is empty.")
            else:
                print("\n--- Your Current Order ---")
                for i, order in enumerate(cafe.orders, start=1):
                  print(f"  {i}. {order}")
            print(f"  Subtotal so far: ${cafe.calculate_subtotal():.2f}")

        case "3":
            if not cafe.orders:
                print("\n❌ You have not ordered anything yet!")
                continue
            # Ask for tip percentage
            print("\nHow much would you like to tip?")
            print("1. 10%    2. 15%    3. 20%    4. No tip")
            tip_choice = input("Enter your choice (1/2/3/4): ").strip()

            tip_map = {"1": 10, "2": 15, "3": 20, "4": 0}
            tip_percent = tip_map.get(tip_choice, 0)

            cafe.print_bill(tip_percent)
            print("\nThank you for visiting! Have a great day! ☕\n")
            break   # Exit the while loop — we are done!

        case __:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")