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


class weapons:
    def __init__(self, x, y, dungeon_level=1):
        self.dungeon_level = dungeon_level

    def return_weapons(self, x, y):
        item_chances = {
            'a': 10,
            'b': from_dungeon_level([[2, 4]], self.dungeon_level),
            'c': from_dungeon_level([[3, 4]], self.dungeon_level),
            'd': from_dungeon_level([[5, 4]], self.dungeon_level),
            'e': from_dungeon_level([[6, 4]], self.dungeon_level),
            'f': from_dungeon_level([[4, 4]], self.dungeon_level),
            'g': from_dungeon_level([[7, 4]], self.dungeon_level),
            'h': from_dungeon_level([[8, 4]], self.dungeon_level),
            'i': from_dungeon_level([[9, 4]], self.dungeon_level),
            'j': from_dungeon_level([[10, 4]], self.dungeon_level)
            }

        item_choice = random_choice_from_dict(item_chances)

        if item_choice == 'a':
            equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=3)
            item = Entity(x, y, '/', libtcod.sky, 'Rusty Sword', equippable=equippable_component)
        elif item_choice == 'b':
            equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=2)
            item = Entity(x, y, '/', libtcod.sky, 'Rusty Dagger', equippable=equippable_component)
        elif item_choice == 'c':
            equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=5)
            item = Entity(x, y, '/', libtcod.sky, 'Chipped Dagger', equippable=equippable_component)
        elif item_choice == 'd':
            equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=7)
            item = Entity(x, y, '/', libtcod.sky, 'Broken Sword', equippable=equippable_component)
        elif item_choice == 'e':
            equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=8)
            item = Entity(x, y, '/', libtcod.sky, 'Chipped Sword', equippable=equippable_component)
        elif item_choice == 'f':
            equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=4)
            item = Entity(x, y, '/', libtcod.sky, 'Broken Dagger', equippable=equippable_component)
        elif item_choice == 'g':
            equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=9)
            item = Entity(x, y, '/', libtcod.sky, 'Bent Dagger', equippable=equippable_component)
        elif item_choice == 'h':
            equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=10)
            item = Entity(x, y, '/', libtcod.sky, 'Bent Sword', equippable=equippable_component)
        elif item_choice == 'i':
            equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=11)
            item = Entity(x, y, '/', libtcod.sky, 'Unwieldy Dagger', equippable=equippable_component)
        elif item_choice == 'j':
            equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=12)
            item = Entity(x, y, '/', libtcod.sky, 'Unwieldy Sword', equippable=equippable_component)

        return item