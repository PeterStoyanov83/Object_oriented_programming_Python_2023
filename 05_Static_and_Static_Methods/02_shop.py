from typing import Dict, TypeVar, Type

T = TypeVar('T', bound='TrivialClass')


class Shop:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items: Dict[str, int] = {}

    @classmethod
    def small_shop(cls: Type[T], name: str, type: str) -> T:
        return cls(name, type, 10)

    def add_item(self, item_name: str) -> str:
        if self.capacity > len(self.items.values()):
            if item_name not in self.items:
                self.items[item_name] = 0
            self.items[item_name] += 1
            return f"{item_name} added to the shop"
        return "Not enough capacity in the shop"

    def remove_item(self, item_name: str, amount: int) -> str:
        if item_name not in self.items:
            return f"Cannot remove {amount} {item_name}"

        if self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount

        if self.items[item_name] == 0:
            del self.items[item_name]
            return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


def test_shop():
    # Create a small shop using the class method
    small_shop = Shop.small_shop("Small Shop", "Grocery")

    # Test adding items to the shop
    assert small_shop.add_item("Apple") == "Apple added to the shop"
    assert small_shop.add_item("Banana") == "Banana added to the shop"
    assert small_shop.add_item("Apple") == "Apple added to the shop"
    assert small_shop.add_item("Orange") == "Orange added to the shop"

    # Attempt to add an item beyond the shop's capacity
    assert small_shop.add_item("Grapes") == "Not enough capacity in the shop"

    # Test removing items from the shop
    assert small_shop.remove_item("Apple", 2) == "2 Apple removed from the shop"
    assert small_shop.remove_item("Banana", 1) == "1 Banana removed from the shop"
    assert small_shop.remove_item("Grapes", 1) == "Cannot remove 1 Grapes"

    # Test shop representation
    assert repr(small_shop) == "Small Shop of type Grocery with capacity 10"

    print("All test cases pass")


test_shop()
