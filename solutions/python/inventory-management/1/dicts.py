"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """

    unique_items = set(items)
    inventory = {}
    for item in unique_items:
        inventory.update({item: items.count(item)})
    return inventory



def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """
    items_to_add = create_inventory(items)
    for item in inventory:
        if item in items_to_add:
            items_to_add[item] += inventory[item]
        else:
            items_to_add.update({item: inventory[item]})
    return items_to_add



def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """
    # decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"])
    # {"coal":2, "diamond":0, "iron":3}

    items_to_decrement = create_inventory(items)
    print(inventory)
    print("\n\n\n")
    print(items_to_decrement)
    for item in inventory:
        if item in items_to_decrement:
            if items_to_decrement[item] > inventory[item]:
                inventory[item] = 0
            else:
                inventory[item] -= items_to_decrement[item]
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """

    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """
    inventory_list = []
    for item in inventory:
        if not inventory[item]:
            continue
        else:
            inventory_list.append((item, inventory[item]))
    return inventory_list
