# 🚗 Car Dealership Manager (Class 18)

A command-line interface (CLI) application built with **Python OOP** and **SQLite** to manage a vehicle inventory system. This project demonstrates how to integrate object-oriented programming with a persistent database.

---

## 📂 Project Structure

```text
car_dealership/
│
├── main.py          # Entry point, CLI menu loop, and user flow
├── car.py           # Car class definition (OOP)
├── database.py      # SQLite logic and database interactions (Provided)
└── dealership.db    # SQLite database file (Auto-generated)
```

---

## ✅ Project Checklist

### 1. (`car.py`) Part 1. The `Car` Class
- [x] **Task 1.1:** Define Class and Constructor (`__init__`)
- [x] **Task 1.2:** Add a `__str__` method
- [x] **Task 1.3:** Add a `to_tuple` method
- [x] **Task 1.4:** Add Input Validation (Optional Challenge)

### 2. (`database.py`) Part 2. The Database Layer (fully provied)

- **DATABASE SETUP**
- **CREATE**
- **READ**
- **UPDATE**
- **DELETE**
- **SEARCH**

### 3. (`main.py`) Part 3. The Main Program
- [x] **Task 3.1:** The `show_menu()` function
- [x] **Task 3.2:** The `add_car_flow()` function
- [x] **Task 3.3:** The `view_all_cars_flow()` function
- [x] **Task 3.4:** The `update_car_flow()` function
- [x] **Task 3.5:** The `delete_car_flow()` function
- [x] **Task 3.6:** The `search_cars_flow()` function
- [x] **Task 3.7:** The `main loop` (while True: loop)

### 4. Testing Checklist
|  | Test | Expected Result |
|:---:| :--- | :--- |
|✅| Add a car with valid data | **Car appears in "View All"** |
|✅| Add a car with letters in the year field | **Error message, no crash** |
|✅| View all cars when inventory is empty | **"No cars in inventory" message** |
|✅| Update a car — press Enter to skip a field | **That field stays unchanged** |
|✅| Update a car with an ID that doesn't exist | **"Car not found" message** |
|✅| Delete a car, confirm with 'y' | **Car no longer appears in listing** |
|✅| Delete a car, cancel with 'n' | **Car still exists** |
|✅| Search "toyota" | **All Toyotas appear (any case)** |
|✅| Search "2020" | **All 2020 model year cars appear** |
|✅| Search "zzz" | **"Found 0 car(s)" message** |

### 5. Extension Challenges
- [] (⏳ In Progress)**1** Sorting
- [] (⏳ In Progress)**2** Statistics
- [] (⏳ In Progress)**3** Price filter
- [] (⏳ In Progress)**4** Export
- [] (⏳ In Progress)**5** Multiple tables

---

## 🔗 Project Links

- **Repository:** [https://github.com/lazy-h-null/my-exercise-archive/tree/main/18-mar30]