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


class potions:
    def __init__(self, x, y, dungeon_level=1):
        self.dungeon_level = dungeon_level

    def return_potions(self, x, y):
        item_chances = {
            'a': 10,
            'b': from_dungeon_level([[2, 4]], self.dungeon_level),
            'c': from_dungeon_level([[3, 4]], self.dungeon_level),
            'd': from_dungeon_level([[4, 4]], self.dungeon_level),
            'e': from_dungeon_level([[5, 4]], self.dungeon_level),
            'f': from_dungeon_level([[6, 4]], self.dungeon_level),
            'g': from_dungeon_level([[6, 4]], self.dungeon_level),
            'h': from_dungeon_level([[2, 4]], self.dungeon_level),
            'i': from_dungeon_level([[2, 4]], self.dungeon_level),
            'j': from_dungeon_level([[3, 4]], self.dungeon_level),
            'k': from_dungeon_level([[3, 4]], self.dungeon_level)
            }

        item_choice = random_choice_from_dict(item_chances)

        if item_choice == 'a':
            item_component = Item(use_function=heal, amount=20)
            item = Entity(x, y, '!', libtcod.violet, 'Lesser Healing Potion', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'b':
            item_component = Item(use_function=heal, amount=40)
            item = Entity(x, y, '!', libtcod.violet, 'Healing Potion', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'c':
            item_component = Item(use_function=heal, amount=60)
            item = Entity(x, y, '!', libtcod.violet, 'Large Healing Potion', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'd':
            item_component = Item(use_function=flood, amount=20)
            item = Entity(x, y, '!', libtcod.violet, 'Lesser Blud Potion', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'e':
            item_component = Item(use_function=seal, amount=20)
            item = Entity(x, y, '!', libtcod.violet, 'Lesser Bottle of Blud Storage', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'f':
            item_component = Item(use_function=flood, amount=40)
            item = Entity(x, y, '!', libtcod.violet, 'Blud Potion', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'g':
            item_component = Item(use_function=seal, amount=40)
            item = Entity(x, y, '!', libtcod.violet, 'Bottle of Blud Storage', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'h':
            item_component = Item(use_function=flood, amount=60)
            item = Entity(x, y, '!', libtcod.violet, 'Large Blud Potion', render_order=RenderOrder.ITEM, item=item_component)
        elif item_choice == 'i':
            item_component = Item(use_function=seal, amount=60)
            item = Entity(x, y, '!', libtcod.violet, 'Large Bottle of Blud Storage', render_order=RenderOrder.ITEM, item=item_component)

        # Return the glass material so we get broken shards out of use
        item.material = 'glass'

        return item
