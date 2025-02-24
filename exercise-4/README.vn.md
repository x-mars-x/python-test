
# Hệ Thống Giỏ Hàng - Bài Tập OOP Cơ Bản

## Mô Tả Bài Toán

Tạo một hệ thống giỏ hàng đơn giản nơi người dùng có thể thêm sản phẩm, tính tổng tiền và áp dụng giảm giá dựa trên loại sản phẩm và tổng số lượng.

### Các Lớp Yêu Cầu

1. **Lớp Product (Sản Phẩm)**  
   - Thuộc tính: tên (name), giá (price)  
   - Phương thức: get_price() (lấy giá)

2. **Lớp ElectronicProduct (Sản Phẩm Điện Tử)**  
   - Kế thừa từ lớp Product  
   - Thuộc tính bổ sung: số năm bảo hành (warranty_years)  
   - Không yêu cầu phương thức bổ sung

3. **Lớp ShoppingCart (Giỏ Hàng)**  
   - Lưu trữ sản phẩm và số lượng của chúng  
   - Các phương thức yêu cầu:  
     - add_item(product, quantity) - Thêm một sản phẩm  
     - remove_item(product) - Xóa một sản phẩm  
     - get_total() - Tính tổng tiền (bao gồm giảm giá)  
     - calculate_discount() - Tính toán giảm giá dựa trên quy tắc  

### Yêu Cầu

1. **Xử Lý Lỗi Cơ Bản**  
   - Xử lý số lượng âm  
   - Xử lý giá âm  
   - Xử lý việc xóa các mặt hàng không tồn tại  

2. **Hệ Thống Giảm Giá (Tính Toán Logic)**  
   - Nếu tổng số lượng mặt hàng trong giỏ vượt quá 5, áp dụng giảm giá 10% trên tổng tiền.  
   - Nếu có ít nhất 2 sản phẩm điện tử (ElectronicProduct), áp dụng thêm 5% giảm giá trên tổng tiền (sau khi đã giảm 10%, nếu có).  
   - Phương thức calculate_discount() trả về số tiền giảm giá, và get_total() sẽ trừ số tiền này khỏi tổng tiền ban đầu.

### Ví Dụ Sử Dụng

```python
# Tạo sản phẩm
laptop = ElectronicProduct("Laptop Chơi Game", 999.99, 2)  # Bảo hành 2 năm
phone = ElectronicProduct("Điện Thoại Thông Minh", 599.99, 1)  # Bảo hành 1 năm
notebook = Product("Sổ Tay", 4.99)

# Sử dụng giỏ hàng
cart = ShoppingCart()
cart.add_item(laptop, 2)    # 2 laptop
cart.add_item(phone, 1)     # 1 điện thoại
cart.add_item(notebook, 3)  # 3 sổ tay

# In thông tin
discount = cart.calculate_discount()
total = cart.get_total()
print(f"Giảm giá: ${discount:.2f}")
print(f"Tổng tiền giỏ hàng: ${total:.2f}")
```

**Kết Quả Dự Kiến (Tính Toán Thủ Công):**  

- Tổng tiền ban đầu: (2 × 999.99) + (1 × 599.99) + (3 × 4.99) = 1999.98 + 599.99 + 14.97 = 2614.94  
- Tổng số lượng = 6 (> 5) → Giảm giá 10% = 261.494  
- 3 sản phẩm điện tử (> 2) → Giảm thêm 5% trên (2614.94 - 261.494) = 117.6723  
- Tổng giảm giá = 261.494 + 117.6723 = 379.1663  
- Tổng tiền cuối cùng = 2614.94 - 379.1663 = 2235.7737  

**Kết Quả In Ra:**  

```
Giảm giá: $379.17
Tổng tiền giỏ hàng: $2235.77
```
