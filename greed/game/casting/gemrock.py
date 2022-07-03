from game.casting.item import Item


class Gemrock(Item):
    """
    Either a gem or a rock
    
    The responsibility of Gemrock is generate a gem or a rock

    """
    def __init__(self):
        super().__init__()
        self._points = 0


    def get_points(self):
        """Gets the points of the gemrock item
        
        Returns:
            Points: the points of the gemrock item
        """
        return self._points

    def set_points(self, points):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._points = points