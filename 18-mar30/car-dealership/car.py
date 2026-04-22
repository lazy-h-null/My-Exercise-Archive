class Car:
    def __init__(self, make, model, year, price, mileage, id=None):
        self.id = id
        self.make = make
        self.model = model        
        self.year = year       
        self.price = price        
        self.mileage = mileage

    def __str__(self):
        return f"[ID: {self.id}] {self.year} {self.make} {self.model} | ${self.price:,.2f} | {self.mileage:,} km"

    def to_tuple(self):
        return(self.make, self.model, self.year, self.price, self.mileage)
    
