# Класс ShoppingCart представляет корзину покупок в интернет-магазине спортивного оборудования.
# Этот класс отвечает за управление товарами в корзине, такими как добавление, удаление,
# очистка и расчет общей стоимости. Он является частью системы интернет-магазина. Класс ShoppingCart обеспечивает базовую
# функциональность для управления корзиной и может быть интегрирован в общую структуру интернет-магазина для обеспечения процесса покупок.
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity=1):
        """
        Добавляет товар в корзину.

        """
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_item(self, product, quantity=1):
        """
        Удаляет указанное количество товара из корзины.

        """
        if product in self.items:
            self.items[product] = max(0, self.items[product] - quantity)
            if self.items[product] == 0:
                del self.items[product]

    def clear(self):
        """Очищает корзину, удаляя все товары."""
        self.items = {}

    def get_total_price(self):
        """Возвращает общую стоимость товаров в корзине."""
        total_price = 0
        for product, quantity in self.items.items():
            total_price += product.price * quantity
        return total_price

    def view_cart(self):
        """Выводит содержимое корзины."""
        for product, quantity in self.items.items():
            print(f"{product.name} - {quantity} шт.")


