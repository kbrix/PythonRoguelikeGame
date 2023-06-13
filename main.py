#!/usr/bin/env python3
import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    screen_width: int = 80
    screen_height: int = 50

    player_x: int = int(screen_width / 2)
    player_y: int = int(screen_height / 2)

    tileset: tileset = tcod.tileset.load_tilesheet(
        path="dejavu10x10_gs_tc.png", columns=32, rows=8, charmap=tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    with tcod.context.new_terminal(
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title="Kristoffer's Amazing Roguelike Game",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)

            root_console.clear()

            for event in tcod.event.wait():

                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()

    print("Hello World!")


if __name__ == "__main__":
    main()