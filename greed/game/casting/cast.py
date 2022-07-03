import random
from game.shared.point import Point

class Cast:
    """A collection of items.

    The responsibility of a cast is to keep track of a collection of items. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _items (dict): A dictionary of items { key: group_name, value: a list of items }
    """

    def __init__(self, cols, rows, cell_size):
        """Constructs a new item."""
        self._items = {}
        self._cols = cols
        self._rows = rows
        self._cell_size = cell_size
        
    def add_item(self, group, item):
        """Adds an item to the given group.
        
        Args:
            group (string): The name of the group.
            item (item): The item to add.
        """
        if not group in self._items.keys():
            self._items[group] = []
            
        if not item in self._items[group]:
            self._items[group].append(item)

    def get_items(self, group):
        """Gets the items in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The items in the group.
        """
        results = []
        if group in self._items.keys():
            results = self._items[group].copy()
        return results
    
    def get_all_items(self):
        """Gets all of the items in the cast.
        
        Returns:
            List: All of the items in the cast.
        """
        results = []
        for group in self._items:
            results.extend(self._items[group])
        return results

    def get_first_item(self, group):
        """Gets the first item in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first item in the group.
        """
        result = None
        if group in self._items.keys():
            result = self._items[group][0]
        return result

    def reset_item(self, item):
        """Resets item's position
        
        Args:
            item (str): The type of item (gem/rock)

        """
        x = random.randint(1, self._cols - 1)
        y = random.randint(1, self._rows - 1)

        position = Point(x, y)
        position = position.scale(self._cell_size)
        item.set_position(position)