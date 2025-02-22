class MenuItem:
    def __init__(self, name: str,price: float):
        self.name = name
        self.price = price
    
    def calculate_total(self, quantity: int=1):
        """Calculate the total price for a given quantity of the item."""
        return self.price*quantity
    
class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size_ml: int, container: str):
        super().__init__(name, price)
        self.size_ml = size_ml 
        self.container = container  
        
    def __str__(self):
        return f"{self.name} ({self.size_ml}ml, {self.container}): ${self.price:.3f} COP"
        
class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, portion_size: str, sauses:bool):
        super().__init__(name, price)
        self.portion_size = portion_size
        self.sauses = sauses
    
    def __str__(self):
        return f"{self.name} ({self.portion_size}): ${self.price:.3f} COP"
        
class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, porcion_sinze: str, spiciness:bool, sauses:bool):
        super().__init__(name, price)
        self.sinze_portion = porcion_sinze
        self.spicinesss = spiciness
        self.spiciness = sauses
        
    def __str__(self):
        return f"{self.name} ({self.sinze_portion}): ${self.price:.3f} COP"
    
class Order:
    def __init__(self):
        self.items = []
    
    def add_item(self, item: MenuItem, quantity: int=1):
        """Add an item to the order."""
        self.items.append((item, quantity))
        
    def total_invoice(self):
        """Calculate the total amount for the order."""
        self.total = 0
        self.total += sum(item.calculate_total(quantity) for item, quantity in self.items)        
        return self.total
    
    def discount(self):
        """
        Applies a discount based on the total number of items in the order.
        Discounts:
        - 5% if there are between 3 and 5 items.
        - 10% if there are between 6 and 10 items.
        - 15% if there are more than 10 items.
        """ 
        amount = sum(quantity for _, quantity in self.items)
        if 3 <= amount <= 5:
            self.discount = 0.05
        elif 6 <= amount <= 10:
            self.discount = 0.10
        elif 10 < amount:
            self.discount = 0.15
            
        self.reduction = (self.total*self.discount)
    
    def __str__(self):
        return (f"The total of the invoice is: ${self.total:.3f} COP\n"
                f"The total bill to pay with a discount of {self.discount*100}% is: ${(self.total - self.reduction):.3f} COP\n")

class IterOrder:
    def __init__(self, order: Order):
        self.order = order
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.order.items):
            item, cant  = self.order.items[self.index]
            self.index += 1
            return f"{item.name} x {cant} = ${item.calculate_total(cant):.3f} COP" 
        else:
            raise StopIteration
        
# Create menu items
coca_cola = Beverage("Coca Cola", 3.200, 500, "Bottle")
lemon_juice = Beverage("Lemon Juice", 2.000, 300, "Glass")
nachos = Appetizer("Nachos", 5.000, "Medium", True)
french_fries = Appetizer("French Fries", 4.300, "Small", False)
salad = Appetizer("Fruit Salad", 6.000, "Medium", False)
hamburguer = MainCourse("Hambuerger", 14.000, "Medium", False, True)
pizza = MainCourse("Pizza", 10.000, "Family", False, True)
sushi = MainCourse("Sushi", 13.500, "Large", True, True)
tacos = MainCourse("Tacos", 11.300, "Medium", True, True)

print("MENU:")

# Print each menu item
print(coca_cola)
print(lemon_juice)
print(nachos)
print(hamburguer)
print(pizza)
print(salad)
print(sushi)
print(tacos)

# Create an order
order1 = Order()
order1.add_item(coca_cola, 2)
order1.add_item(french_fries)
order1.add_item(hamburguer)
order1.total_invoice()
order1.discount()
print(f"\nORDER 1: \n{order1}\n")

# Create another order
order2 = Order()
order2.add_item(lemon_juice, 3)
order2.add_item(nachos, 2)
order2.add_item(pizza)
order2.add_item(salad)
order2.total_invoice()
order2.discount()
print(f"ORDER 2: \n{order2}\n")

# Create another order
order3 = Order()
order3.add_item(lemon_juice)
order3.add_item(coca_cola, 3)
order3.add_item(sushi, 2)
order3.add_item(tacos, 3)
order3.add_item(salad)
order3.total_invoice()
order3.discount()
print(f"ORDER 3: \n{order3}\n")

print("\nORDER 1:")
for item in IterOrder(order1):
    print(item)
  
print("\nORDER 2:")  
for item in IterOrder(order2):
    print(item)
   
print("\nORDER 3:") 
for item in IterOrder(order3):
    print(item)