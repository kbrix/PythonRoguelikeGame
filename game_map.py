import numpy as np
from tcod.console import Console

import tile_types

class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

        self.visible = np.full((width, height), fill_value=False, order="F") # Tiles the player can current see.
        self.explored = np.full((width, height), fill_value=False, order="F") # Tiles the plater has seen before.

    def in_bound(self, x: int, y: int) -> bool:
        """Return true if 'x' and 'y' are inside the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console):
        """
        Renders the map.

        If a tile is in the "visible" array, then draw it with the "light" colors.
        If it is not, but it is in the "explored" array, then draw it with the "dark" colors.
        Otherwise, the default is "SHOURD".
        """
        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD
        )