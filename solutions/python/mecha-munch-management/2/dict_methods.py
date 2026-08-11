"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """

    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart.update({item: 1})
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    user_cart = {}
    return user_cart.fromkeys(notes,1)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """
    for item in recipe_updates:
        if item[0] in ideas:
            ideas[item[0]] = item[1]
        else:
            ideas.update({item[0]: item[1]})
    return ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """
    combined = {order: (cart[order], *aisle_mapping[k]) for order in cart}
    sorted_items = sort_entries(combined)
    reversed_cart = reversed(sorted_items.items())
    fullfillment_cart = {}
    for item in reversed_cart:
        fullfillment_cart.update({item[0]: list(item[1])})
    return fullfillment_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """

    for item in store_inventory:
        if item in fulfillment_cart:
            store_inventory[item][0] -= fulfillment_cart[item][0]
            if not store_inventory[item][0]:
                store_inventory[item][0] = 'Out of Stock'
    return store_inventory
