#Using default parameters to do method overloading 
class Calculator:
    def add(self, a, b=None, c=None):
        if b is None and c is None:
            return a
        elif c is None:
            return a + b
        else:
            return a + b + c

# Usage
calc = Calculator()
print(calc.add(5))          # 5
print(calc.add(5, 3))       # 8
print(calc.add(5, 3, 2))    # 10




#Using *args to do method overloading
class ShoppingCart:
    def add_items(self, *args):
        """Add multiple items to the cart using variable arguments"""
        if not args:
            print("No items added to cart")
        else:
            print(f"Added {len(args)} items to cart: {', '.join(args)}")

# Usage
cart = ShoppingCart()

cart.add_items()                     # No items added to cart
cart.add_items("Shirt")              # Added 1 items to cart: Shirt
cart.add_items("Shoes", "Hat")       # Added 2 items to cart: Shoes, Hat
cart.add_items("Book", "Pen", "Bag") # Added 3 items to cart: Book, Pen, Bag