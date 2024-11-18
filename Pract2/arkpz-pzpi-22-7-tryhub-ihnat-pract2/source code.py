def is_item_available(item):
    pass
# Extract Method

# Код до рефакторингу
def process_order(order):
    # Перевірка наявності товару
    for item in order["items"]:
        if not is_item_available(item):
            print(f"Товар {item['name']} недоступний на складі.")
            return

    for item in order["items"]:  # Повторний цикл для підрахунку ціни
        print(f"Товар: {item['name']}, Кількість: {item['quantity']}")

    # Підрахунок вартості замовлення
    total = 0
    for item in order["items"]:
        total += item["price"] * item["quantity"]
    print(f"Загальна сума: {total}")

    # Оформлення доставки
    print(f"Доставка до {order['customer']['address']}")
    print("Замовлення оброблено успішно!")



# Код після рефакторингу:
def process_order(order):
    if not check_items_availability(order["items"]):
        return

    display_items(order["items"])  # Новий метод для виводу інформації про товари
    total = calculate_total(order["items"])
    print(f"Загальна сума: {total}")

    arrange_shipping(order["customer"]["address"])
    print("Замовлення оброблено успішно!")

def check_items_availability(items):
    for item in items:
        if not is_item_available(item):
            print(f"Товар {item['name']} недоступний на складі.")
            return False
    return True

def display_items(items):
    for item in items:
        print(f"Товар: {item['name']}, Кількість: {item['quantity']}")

def calculate_total(items):
    return sum(item["price"] * item["quantity"] for item in items)

def arrange_shipping(address):
    print(f"Доставка до {address}")









# Inline method

# Код до рефакторингу
def calculate_final_price(price, discount):
    #Обчислення кінцевої ціни із застосуванням знижки.
    discounted_price = apply_discount(price, discount)
    tax = calculate_tax(discounted_price)
    final_price = discounted_price + tax
    return final_price

def apply_discount(price, discount):
    #Застосування знижки до початкової ціни.
    if discount > 0.5:  # Перевірка, чи не надто велика знижка
        print("Знижка надто велика!")
        return price
    return price - (price * discount)

def calculate_tax(price):
    #Обчислення податку на основі ціни після знижки.
    tax_rate = 0.2  # 20% податку
    return price * tax_rate

# Виклик функції
final_price = calculate_final_price(100, 0.3)
print(f"Кінцева ціна: {final_price}")



# Код після рефакторингу:
def calculate_final_price(price, discount):
    # Обчислення кінцевої ціни із застосуванням знижки та податків.

    # Застосування знижки
    if discount > 0.5:  # Перевірка, чи не надто велика знижка
        print("Знижка надто велика!")
        discounted_price = price
    else:
        discounted_price = price - (price * discount)

    # Обчислення податку
    tax_rate = 0.2  # 20% податку
    tax = discounted_price * tax_rate

    # Розрахунок кінцевої ціни
    final_price = discounted_price + tax
    return final_price

# Виклик функції
final_price = calculate_final_price(100, 0.3)
print(f"Кінцева ціна: {final_price}")

import random
import string

# Replace Array with Object
# Код до рефакторингу 
class Order:
    def __init__(self, id=None, customer=None, amount=None, date=None, status=None):
        # Генерація ID, якщо не передано
        if not id:
            id = self.generate_order_id()
        
        # Перевірка, чи є необхідні дані для замовлення
        if not customer or not amount:
            raise ValueError("Клієнт і сума обов'язкові для створення замовлення")
        
        # Встановлення значень
        self.id = id
        self.customer = customer
        self.amount = amount
        self.date = date if date else self.generate_order_date()
        self.status = status if status else "Pending"
        
        # Логіка для різних статусів замовлення
        if self.status == "Pending":
            self.process_pending_order()
        elif self.status == "Shipped":
            self.process_shipped_order()
        elif self.status == "Cancelled":
            self.process_cancelled_order()

    def generate_order_id(self):
        """Генерація унікального ID для замовлення"""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    
    def generate_order_date(self):
        """Генерація випадкової дати"""
        return "2024-11-18"  # Статична дата для прикладу

    def process_pending_order(self):
        """Обробка очікуючого замовлення"""
        print("Обробка очікуючого замовлення...")
    
    def process_shipped_order(self):
        """Обробка відправленого замовлення"""
        print("Обробка відправленого замовлення...")
    
    def process_cancelled_order(self):
        """Обробка скасованого замовлення"""
        print("Обробка скасованого замовлення...")

# Приклад створення замовлень
order1 = Order(customer="Іван Іванов", amount=100.0)
order2 = Order(id="ORD12345", customer="Марія Петрівна", amount=200.0, status="Shipped")
order3 = Order(customer="Олексій Козак", amount=300.0, status="Cancelled")

# Виведення для демонстрації
print(f"Замовлення1: {order1.id}, {order1.customer}, {order1.status}")
print(f"Замовлення2: {order2.id}, {order2.customer}, {order2.status}")
print(f"Замовлення3: {order3.id}, {order3.customer}, {order3.status}")


# Код после рефакторинга
class Order:
    def __init__(self, id, customer, amount, date, status):
        self.id = id
        self.customer = customer
        self.amount = amount
        self.date = date
        self.status = status

    @staticmethod
    def create_order(customer, amount, status="Pending"):
        """Фабричный метод для создания заказа"""
        id = Order.generate_order_id()
        date = Order.generate_order_date()
        order = Order(id, customer, amount, date, status)
        
        # Обработка статуса через отдельные методы
        order.process_order_status()
        return order
    @staticmethod
    def generate_order_id():
        """Генерация уникального ID для заказа"""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    @staticmethod
    def generate_order_date():
        """Генерация случайной даты"""
        return "2024-11-18"  # Для примера просто статическая дат
    def process_order_status(self):
        """Метод обработки статуса заказа"""
        if self.status == "Pending":
            self.process_pending_order()
        elif self.status == "Shipped":
            self.process_shipped_order()
        elif self.status == "Cancelled":
            self.process_cancelled_order()

    def process_pending_order(self):
        """Логика для обработки ожидающего заказа"""
        print(f"Order {self.id}: Processing pending order...")
    
    def process_shipped_order(self):
        """Логика для обработки отправленного заказа"""
        print(f"Order {self.id}: Processing shipped order...")
    
    def process_cancelled_order(self):
        """Логика для обработки отмененного заказа"""
        print(f"Order {self.id}: Processing cancelled order...")

# Пример создания заказа с использованием фабричного метода
order1 = Order.create_order(customer="John Doe", amount=100.0)
order2 = Order.create_order(customer="Jane Smith", amount=200.0, status="Shipped")
order3 = Order.create_order(customer="Alice Cooper", amount=300.0, status="Cancelled")

# Вывод для демонстрации
print(f"Order1: {order1.id}, {order1.customer}, {order1.status}")
print(f"Order2: {order2.id}, {order2.customer}, {order2.status}")
print(f"Order3: {order3.id}, {order3.customer}, {order3.status}")


