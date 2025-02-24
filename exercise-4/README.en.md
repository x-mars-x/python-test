
# Shopping Cart System - Basic OOP Exercise

## Problem Description

Create a simple shopping cart system where users can add products, calculate totals, and apply discounts based on product type and total quantity.

### Required Classes

1. **Product Class**  
   - Properties: name, price  
   - Method: get_price()

2. **ElectronicProduct Class**  
   - Inherits from Product  
   - Additional property: warranty_years  
   - No additional methods required

3. **ShoppingCart Class**  
   - Should store products and their quantities  
   - Required methods:  
     - add_item(product, quantity) - Add a product  
     - remove_item(product) - Remove a product  
     - get_total() - Calculate the total (including discounts)  
     - calculate_discount() - Calculate the discount based on rules  
     - search_product(search_term) - Search for products in the cart by name (case-insensitive)  

### Requirements

1. **Basic Error Handling**  
   - Handle negative quantities  
   - Handle negative prices  
   - Handle removing non-existent items  

2. **Discount System (Logical Calculations)**  
   - If the total quantity of items in the cart exceeds 5, apply a 10% discount on the total.  
   - If there are at least 2 electronic products (ElectronicProduct), apply an additional 5% discount on the total (after the 10% discount, if applicable).  
   - The calculate_discount() method should return the discount amount, and get_total() should subtract this amount from the original total.

3. **Product Search**  
   - The search_product(search_term) method searches for products in the cart whose names contain the provided search term.  
   - Search must be case-insensitive (e.g., "laptop" matches "Laptop" or "LAPTOP").  
   - Returns a list of (product, quantity) pairs for matching products.

### Example Usage

```python
# Create products
laptop = ElectronicProduct("Gaming Laptop", 999.99, 2)  # 2-year warranty
phone = ElectronicProduct("Smartphone", 599.99, 1)      # 1-year warranty
notebook = Product("Notebook", 4.99)

# Use shopping cart
cart = ShoppingCart()
cart.add_item(laptop, 2)    # 2 laptops
cart.add_item(phone, 1)     # 1 phone
cart.add_item(notebook, 3)  # 3 notebooks

# Search for products
results = cart.search_product("laptop")
for product, quantity in results:
    print(f"Found: {product.name} - Quantity: {quantity}")

# Print information
discount = cart.calculate_discount()
total = cart.get_total()
print(f"Discount: ${discount:.2f}")
print(f"Cart total: ${total:.2f}")
```

**Expected Output (Manual Calculation):**  

- Original total: (2 × 999.99) + (1 × 599.99) + (3 × 4.99) = 1999.98 + 599.99 + 14.97 = 2614.94  
- Total quantity = 6 (> 5) → 10% discount = 261.494  
- 3 ElectronicProducts (> 2) → Additional 5% discount on (2614.94 - 261.494) = 117.6723  
- Total discount = 261.494 + 117.6723 = 379.1663  
- Final total = 2614.94 - 379.1663 = 2235.7737  

**Printed Result:**  

```
Found: Gaming Laptop - Quantity: 2
Discount: $379.17
Cart total: $2235.77
```
