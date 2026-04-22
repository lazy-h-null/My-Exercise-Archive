from car import Car
from database import (initialize_database, import_cars, add_car, get_all_cars, get_car_by_id, update_car, delete_car, search_cars)

def show_menu():
    print("\n" + "="*40)
    print("   🚗  CAR DEALERSHIP MANAGER")
    print("="*40)
    print("1. Add Car")
    print("2. View All Cars")
    print("3. Update Car")
    print("4. Delete Car")
    print("5. Search Cars")
    print("6. Exit")
    print("="*40)

    choice = input("Enter your choice (1-6): ")
    return choice

def add_car_flow():
    try:
        make = input("Make: ")
        model = input("Model: ")
        year = int(input("Year: "))
        price = float(input("Prices: "))
        mileage = int(input("Mileage: "))

        car = Car(make, model, year, price, mileage)

        add_car(car)

        print("Success! Car ID is:", car.id)
    except ValueError:
        print("Error: Please use numbers for Year, Price, and Mileage.`")

def view_all_cars_flow():
    cars = get_all_cars()
    
    if not cars:
        print("No cars in inventory.")
    else:
        for car in cars:
            print(car)

def update_car_flow():
    try:
        car_id = int(input("Enter ID: "))
        
        car = get_car_by_id(car_id)

        if car is None:
            print("Car not found.")
            return
        
        print(car)

        new_make = input(f"New Make [{car.make}]: ")
        if new_make != "":
            car.make = new_make
        
        new_model = input(f"New Model [{car.model}]: ")
        if new_model != "":
            car.model = new_model
        
        new_year = input(f"New Year [{car.year}]: ")
        if new_year != "":
            car.year = int(new_year)
        
        new_price = input(f"New Price [{car.price}]: ")
        if new_price != "":
            car.price = float(new_price)
        
        new_mileage = input(f"New Mileage [{car.mileage}]: ")
        if new_mileage != "":
            car.mileage = float(new_mileage)

        update_car(car)
    
    except ValueError:
        print("Invalid input.")

def delete_car_flow():
    try:
        car_id = int(input("Enter Car ID to delete: "))

        car = get_car_by_id(car_id)

        if car is None:
            print("Car not found.")
            return
        
        print(car)
        
        confirm = input("Are you sure? (y/n): ")
        if confirm == 'y':
            delete_car(car_id)
            print("Car deleted.")
        else:
            print("Delete canceled.")

    except ValueError:
        print("Invalid input.")

def search_cars_flow():
    keyword = input("Enter search term: ")
    results = search_cars(keyword)

    print(f"Found {len(results)} cars")

    if not results:
        print("No cars found.")
    else:
        for car in results:
            print(car)

def main():
    initialize_database()
    import_cars()

    while True:
        choice = show_menu()

        if choice == "1":
            add_car_flow()
        elif choice == "2":
            view_all_cars_flow()
        elif choice == "3":
            update_car_flow()
        elif choice == "4":
            delete_car_flow()
        elif choice == "5":
            search_cars_flow()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()