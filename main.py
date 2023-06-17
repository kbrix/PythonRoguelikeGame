#!/usr/bin/env python3
import tcod

from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

def main() -> None:
    screen_width: int = 80
    screen_height: int = 50

    map_width = 80
    map_height = 45

    tileset: tileset = tcod.tileset.load_tilesheet(
        path="dejavu10x10_gs_tc.png", columns=32, rows=8, charmap=tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(x=int(screen_width / 2), y=int(screen_height / 2), char="@", color=(255, 255, 255))
    npc = Entity(x=int(screen_width / 2 - 5), y=int(screen_height / 2), char="@", color=(255, 255, 0))
    entities = { npc, player }

    game_map = GameMap(map_width, map_height)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title="Kristoffer's Amazing Roguelike Game",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:

            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)

    print("Hello!")

if __name__ == "__main__":
    main()