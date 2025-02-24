# Tạo sản phẩm

laptop = ElectronicProduct("Gaming Laptop", 999.99, 2)  # Bảo hành 2 năm
phone = ElectronicProduct("Smartphone", 599.99, 1)      # Bảo hành 1 năm
notebook = Product("Notebook", 4.99)

# Sử dụng giỏ hàng

cart = ShoppingCart()
cart.add_item(laptop, 2)    # 2 laptop
cart.add_item(phone, 1)     # 1 điện thoại
cart.add_item(notebook, 3)  # 3 sổ tay

# In thông tin

```
discount = cart.calculate_discount()
total = cart.get_total()
print(f"Giảm giá: ${discount:.2f}")
print(f"Tổng tiền giỏ hàng: ${total:.2f}")
```
