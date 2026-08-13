# ============================================================
# Part A - Spot the Bug
# ============================================================

def add_item_bug(item, cart=[]):
    # BUG:
    # The default list is created only once.
    # Therefore, multiple calls share the same list.
    cart.append(item)
    return cart


print("PART A - Mutable Default Argument Bug")
print(add_item_bug("apple"))
print(add_item_bug("banana"))
print(add_item_bug("milk", cart=["bread"]))
print(add_item_bug("eggs"))


# ============================================================
# Part B - Correct Way
# ============================================================

def add_item(item, cart=None):
    # None is used as the default value.
    # A new list is created for every call when cart is None.
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print("\nPART B - Correct Function")
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))


# ============================================================
# Part C - Complete Shopping Cart
# ============================================================

def create_cart(owner, discount=0):
    """
    Creates a new shopping cart.

    discount=0 is safe because integers are immutable.
    """

    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):
    """
    Adds an item to the shopping cart.
    """

    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)


def update_price(price_tuple, new_price):
    """
    Attempts to modify a tuple element.

    Tuples are immutable, so their elements cannot be changed.
    This will raise a TypeError.
    """

    try:
        price_tuple[0] = new_price
    except TypeError as error:
        print("TypeError:", error)


def calculate_total(cart):
    """
    Calculates the total price of all items
    and applies the discount percentage.
    """

    total = 0

    # Loop through all items
    for item in cart["items"]:
        total += item["price"] * item["qty"]

    # Calculate discount
    discount_amount = total * cart["discount"] / 100

    # Calculate final amount
    final_total = total - discount_amount

    return final_total


# ============================================================
# Demonstration - Two Independent Customers
# ============================================================

print("\nPART C - Shopping Cart")

# Create two separate carts
cart1 = create_cart("Aarav", 10)
cart2 = create_cart("Rahul", 5)

# Add items to Aarav's cart
add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 1000, 2)

# Add items to Rahul's cart
add_to_cart(cart2, "Keyboard", 2000, 1)
add_to_cart(cart2, "Headphones", 3000, 2)

# Display both carts
print("\nCart 1:")
print(cart1)

print("\nCart 2:")
print(cart2)

# Calculate totals
print("\nAarav's Final Total:", calculate_total(cart1))
print("Rahul's Final Total:", calculate_total(cart2))


# ============================================================
# Demonstrate Tuple Immutability
# ============================================================

print("\nTuple Immutability")

price_tuple = (1000, "Mouse")

print("Original Tuple:", price_tuple)

update_price(price_tuple, 1500)

print("Tuple after attempted modification:", price_tuple)


# ============================================================
# Discussion Points
# ============================================================

# 1. Why is discount=0 safe but cart=[] dangerous?
#
# discount=0 is safe because an integer is immutable.
# The value 0 cannot be changed.
#
# cart=[] is dangerous because a list is mutable.
# The same default list can be shared between multiple
# function calls.


# 2. What is the difference between rebinding and mutating?
#
# Rebinding means assigning a variable to a new object.
#
# Example:
#
# x = [1, 2]
# x = [3, 4]
#
# Here, x is rebound to a new list.
#
# Mutating means changing the existing object.
#
# Example:
#
# x = [1, 2]
# x.append(3)
#
# Here, the original list is modified.


# 3. Which of these are mutable?
#
# list  -> Mutable
# tuple -> Immutable
# dict  -> Mutable
# set   -> Mutable
# str   -> Immutable
# int   -> Immutable


# 4. When you pass a list into a function and modify it,
#    do changes reflect outside? Why?
#
# Yes.
#
# Lists are mutable objects. When a list is passed to a function,
# the function receives a reference to the same list object.
# Therefore, if the function modifies the list using methods
# such as append(), remove(), or clear(), the changes are
# visible outside the function.
#
# Example:
#
# def add_number(numbers):
#     numbers.append(10)
#
# my_list = [1, 2]
# add_number(my_list)
# print(my_list)
#
# Output:
# [1, 2, 10]