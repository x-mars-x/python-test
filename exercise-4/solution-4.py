import unittest

# Placeholder for classes to be tested


class Product:
    def __init__(self, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years


class ShoppingCart:
    def __init__(self):
        self.items = {}  # product: quantity

    def add_item(self, product, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if quantity > 0:
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity

    def remove_item(self, product):
        if product not in self.items:
            raise ValueError("Product not in cart")
        del self.items[product]

    def get_total(self):
        original_total = sum(p.get_price() * q for p, q in self.items.items())
        discount = self.calculate_discount()
        return original_total - discount

    def calculate_discount(self):
        total_quantity = sum(self.items.values())
        original_total = sum(p.get_price() * q for p, q in self.items.items())

        discount = 0
        if total_quantity > 5:
            discount += original_total * 0.10

        electronic_count = sum(q for p, q in self.items.items()
                               if isinstance(p, ElectronicProduct))
        if electronic_count >= 2:
            after_first_discount = original_total - discount
            discount += after_first_discount * 0.05

        return discount


class TestShoppingCartSystem(unittest.TestCase):
    def setUp(self):
        # Initialize test objects before each test
        self.laptop = ElectronicProduct("Gaming Laptop", 999.99, 2)
        self.phone = ElectronicProduct("Smartphone", 599.99, 1)
        self.notebook = Product("Notebook", 4.99)
        self.cart = ShoppingCart()

    # Test Product class
    def test_product_creation(self):
        product = Product("Test", 10.99)
        self.assertEqual(product.name, "Test")
        self.assertEqual(product.get_price(), 10.99)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            Product("Test", -1.00)

    # Test ElectronicProduct class
    def test_electronic_product_creation(self):
        self.assertEqual(self.laptop.warranty_years, 2)
        self.assertEqual(self.laptop.get_price(), 999.99)

    # Test ShoppingCart basic operations
    def test_add_item(self):
        self.cart.add_item(self.laptop, 2)
        self.assertEqual(self.cart.items[self.laptop], 2)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add_item(self.laptop, -1)

    def test_remove_item(self):
        self.cart.add_item(self.laptop, 1)
        self.cart.remove_item(self.laptop)
        self.assertNotIn(self.laptop, self.cart.items)

    def test_remove_nonexistent_item(self):
        with self.assertRaises(ValueError):
            self.cart.remove_item(self.laptop)

    # Test discount calculations
    def test_no_discount(self):
        self.cart.add_item(self.notebook, 2)  # qty < 5, no electronics
        self.assertEqual(self.cart.calculate_discount(), 0)
        self.assertAlmostEqual(self.cart.get_total(), 4.99 * 2)

    def test_quantity_discount(self):
        self.cart.add_item(self.notebook, 6)  # qty > 5
        expected_total = (4.99 * 6)
        expected_discount = expected_total * 0.10
        self.assertAlmostEqual(
            self.cart.calculate_discount(), expected_discount)
        self.assertAlmostEqual(self.cart.get_total(),
                               expected_total - expected_discount)

    def test_electronic_discount(self):
        self.cart.add_item(self.laptop, 2)  # 2 electronic items
        expected_total = (999.99 * 2)
        expected_discount = expected_total * 0.05
        self.assertAlmostEqual(
            self.cart.calculate_discount(), expected_discount)
        self.assertAlmostEqual(self.cart.get_total(),
                               expected_total - expected_discount)

    def test_combined_discount(self):
        # Test the example scenario
        self.cart.add_item(self.laptop, 2)    # 2 laptops
        self.cart.add_item(self.phone, 1)     # 1 phone
        self.cart.add_item(self.notebook, 3)  # 3 notebooks

        original_total = (999.99 * 2) + (599.99 * 1) + (4.99 * 3)
        first_discount = original_total * 0.10  # qty = 6 > 5
        after_first = original_total - first_discount
        second_discount = after_first * 0.05    # 3 electronics > 2

        expected_discount = first_discount + second_discount
        expected_total = original_total - expected_discount

        self.assertAlmostEqual(
            self.cart.calculate_discount(), expected_discount, places=2)
        self.assertAlmostEqual(self.cart.get_total(), expected_total, places=2)


if __name__ == '__main__':
    unittest.main()
