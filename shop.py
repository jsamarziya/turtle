from typing import List


class Item:
    """
    An item that has been selected for purchase.
    """

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def total(self) -> float:
        """
        Returns the total amount for this item.
        """
        return self.price * self.quantity


class Cart:
    """
    A shopping cart.
    """

    def __init__(self):
        self.items: List[Item] = []

    def add_item(self, item: Item):
        """
        Adds an item to the cart.
        """
        self.items.append(item)

    @property
    def item_count(self) -> int:
        """
        Returns the number of items in this cart.
        """
        return len(self.items)

    @property
    def total(self) -> float:
        """
        Returns the total amount for all items.
        """
        return sum((item.total for item in self.items))


def get_number(message, func):
    """
    Prompts for input of a number.
    """
    while True:
        value = input(message)
        try:
            return func(value)
        except ValueError:
            print(f"'{value}' is not a valid number")


def get_order() -> Cart:
    """
    Takes a customer's order.

    :return: the order
    """
    print("Welcome to the store!")
    cart = Cart()
    while True:
        name = input("What would you like to buy? (Enter to quit): ")
        if not name:
            break
        quantity = get_number(f"Enter the quantity of {name} you wish to purchase: ", int)
        price = get_number(f"Enter the price of {name}: ", float)
        item = Item(name, price, quantity)
        cart.add_item(item)
    print(f"\nYour cart contains {cart.item_count:,} item{'' if cart.item_count == 1 else 's'}:")
    for item in cart.items:
        print(f"\t{item.name} ({item.quantity:,} x ${item.price:,.2f} = ${item.total:,.2f})")
    print(f"\nYour total is ${cart.total:,.2f}")
    print("Thank you for shopping!")
    return cart


if __name__ == "__main__":
    while True:
        order = get_order()
        if order.item_count == 0:
            break
        print()
