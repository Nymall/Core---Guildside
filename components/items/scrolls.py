import libtcodpy as libtcod
from random import randint

from components.ai import BasicMonster
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from components.fighter import Fighter
from components.item import Item

from entity import Entity

from game_messages import Message

from item_functions import cast_confuse, cast_fireball, cast_lightning, heal

from map_objects.rectangle import Rect
from map_objects.tile import Tile

from random_utils import from_dungeon_level, random_choice_from_dict

from render_functions import RenderOrder


class scrolls:
    def __init__(self, x, y, dungeon_level=1):
        self.dungeon_level = dungeon_level

    def return_scrolls(self, x, y):
        item_chances = {
            'a': 10,
            'b': from_dungeon_level([[2, 4]], self.dungeon_level),
            'c': from_dungeon_level([[3, 4]], self.dungeon_level),
            'd': from_dungeon_level([[4, 4]], self.dungeon_level),
            'e': from_dungeon_level([[5, 4]], self.dungeon_level),
            'f': from_dungeon_level([[6, 4]], self.dungeon_level),
            'g': from_dungeon_level([[6, 4]], self.dungeon_level),
            'h': 10,
            'i': from_dungeon_level([[2, 4]], self.dungeon_level),
            'j': from_dungeon_level([[3, 4]], self.dungeon_level),
            'k': from_dungeon_level([[4, 4]], self.dungeon_level),
            'l': from_dungeon_level([[5, 4]], self.dungeon_level),
            'm': from_dungeon_level([[6, 4]], self.dungeon_level)
            }

        item_choice = random_choice_from_dict(item_chances)

        if item_choice == 'a':
            item_component = Item(use_function=cast_fireball, targeting=True, targeting_message=Message( 'Left-click a target tile for the fireball, or right-click to cancel.', libtcod.light_cyan), damage=12, radius=2)
            item = Entity(x, y, '#', libtcod.red, 'Smudged Burnt Fireball Scroll', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'b':
            item_component = Item(use_function=cast_fireball, targeting=True, targeting_message=Message( 'Left-click a target tile for the fireball, or right-click to cancel.', libtcod.light_cyan), damage=15, radius=2)
            item = Entity(x, y, '#', libtcod.red, 'Burnt Fireball Scroll', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'c':
            item_component = Item(use_function=cast_fireball, targeting=True, targeting_message=Message( 'Left-click a target tile for the fireball, or right-click to cancel.', libtcod.light_cyan), damage=17, radius=3)
            item = Entity(x, y, '#', libtcod.red, 'Smudged Fireball Scroll', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'd':
            item_component = Item(use_function=cast_fireball, targeting=True, targeting_message=Message( 'Left-click a target tile for the fireball, or right-click to cancel.', libtcod.light_cyan), damage=25, radius=3)
            item = Entity(x, y, '#', libtcod.red, 'Fireball Scroll', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'e':
            item_component = Item(use_function=cast_fireball, targeting=True, targeting_message=Message( 'Left-click a target tile for the fireball, or right-click to cancel.', libtcod.light_cyan), damage=35, radius=3)
            item = Entity(x, y, '#', libtcod.red, 'Calculated Fireball Scroll', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'f':
            item_component = Item(use_function=cast_fireball, targeting=True, targeting_message=Message( 'Left-click a target tile for the fireball, or right-click to cancel.', libtcod.light_cyan), damage=50, radius=5)
            item = Entity(x, y, '#', libtcod.red, 'Bloodfeud Fireball Scroll', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'g':
            item_component = Item(use_function=cast_confuse, targeting=True, targeting_message=Message('Left-click an enemy to confuse it, or right-click to cancel.', libtcod.light_cyan))
            item = Entity(x, y, '#', libtcod.light_pink, 'Confusion Scroll', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'h':
            item_component = Item(use_function=cast_lightning, damage=15, maximum_range=4)
            item = Entity(x, y, '#', libtcod.yellow, 'Smudged Burnt Lightning Scroll', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'i':
            item_component = Item(use_function=cast_lightning, damage=20, maximum_range=4)
            item = Entity(x, y, '#', libtcod.yellow, 'Burnt Lightning Scroll', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'j':
            item_component = Item(use_function=cast_lightning, damage=25, maximum_range=5)
            item = Entity(x, y, '#', libtcod.yellow, 'Smudged Lightning Scroll', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'k':
            item_component = Item(use_function=cast_lightning, damage=40, maximum_range=5)
            item = Entity(x, y, '#', libtcod.yellow, 'Lightning Scroll', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'l':
            item_component = Item(use_function=cast_lightning, damage=60, maximum_range=5)
            item = Entity(x, y, '#', libtcod.yellow, 'Calculated Lightning Scroll', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'm':
            item_component = Item(use_function=cast_lightning, damage=80, maximum_range=7)
            item = Entity(x, y, '#', libtcod.yellow, 'Bloodfeud Lightning Scroll', render_order=RenderOrder.ITEM, item=item_component)

        return item
