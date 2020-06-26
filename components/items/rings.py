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


class rings:
    def __init__(self, x, y, dungeon_level=1):
        self.dungeon_level = dungeon_level

    def return_rings(self, x, y):
        choice = randint(1, 2)
        if choice == 1:
            return self.return_rings_left(x, y)
        else:
            return self.return_rings_right(x, y)

    def return_rings_left(self, x, y):
        item_chances = {
            'a': 10,
            'b': from_dungeon_level([[2, 4]], self.dungeon_level),
            'c': from_dungeon_level([[2, 4]], self.dungeon_level),
            'd': from_dungeon_level([[2, 4]], self.dungeon_level),
            'e': from_dungeon_level([[4, 4]], self.dungeon_level),
            'f': from_dungeon_level([[4, 4]], self.dungeon_level),
            'g': from_dungeon_level([[4, 4]], self.dungeon_level),
            'h': from_dungeon_level([[6, 4]], self.dungeon_level),
            'i': from_dungeon_level([[6, 4]], self.dungeon_level),
            'j': from_dungeon_level([[6, 4]], self.dungeon_level),
            'k': from_dungeon_level([[8, 4]], self.dungeon_level)
            }

        item_choice = random_choice_from_dict(item_chances)

        if item_choice == 'a':
            equippable_component = Equippable(EquipmentSlots.RING_L, max_blood_bonus=50)
            item = Entity(x, y, '/', libtcod.sky, 'Left Handed Iron Greatblud Ring', equippable=equippable_component)
        elif item_choice == 'b':
            equippable_component = Equippable(EquipmentSlots.RING_L, max_blood_bonus=50, power_bonus=1)
            item = Entity(x, y, '/', libtcod.sky, 'Left Handed Iron Greatblud Ring with Rubies', equippable=equippable_component)
        elif item_choice == 'c':
            equippable_component = Equippable(EquipmentSlots.RING_L,  max_blood_bonus=50, max_hp_bonus=25)
            item = Entity(x, y, '/', libtcod.sky, 'Left Handed Iron Greatblud Ring with Emeralds', equippable=equippable_component)
        elif item_choice == 'd':
            equippable_component = Equippable(EquipmentSlots.RING_L, max_blood_bonus=50, defense_bonus=1)
            item = Entity(x, y, '/', libtcod.sky, 'Left Handed Iron Greatblud Ring with Diamonds', equippable=equippable_component)
        elif item_choice == 'e':
            equippable_component = Equippable(EquipmentSlots.RING_L, max_blood_bonus=100, power_bonus=2)
            item = Entity(x, y, '/', libtcod.sky, 'Left Handed Silver Greatblud Ring with Rubies', equippable=equippable_component)
        elif item_choice == 'f':
            equippable_component = Equippable(EquipmentSlots.RING_L, max_blood_bonus=100, max_hp_bonus=50)
            item = Entity(x, y, '/', libtcod.sky, 'Left Handed Silver Greatblud Ring with Emeralds', equippable=equippable_component)
        elif item_choice == 'g':
            equippable_component = Equippable(EquipmentSlots.RING_L, max_blood_bonus=100, defense_bonus=2)
            item = Entity(x, y, '/', libtcod.sky, 'Left Handed Silver Greatblud Ring with Diamonds', equippable=equippable_component)
        elif item_choice == 'h':
            equippable_component = Equippable(EquipmentSlots.RING_L, max_blood_bonus=200, power_bonus=4)
            item = Entity(x, y, '/', libtcod.sky, 'Left Handed Gold Greatblud Ring with Rubies', equippable=equippable_component)
        elif item_choice == 'i':
            equippable_component = Equippable(EquipmentSlots.RING_L, max_blood_bonus=200, max_hp_bonus=100)
            item = Entity(x, y, '/', libtcod.sky, 'Left Handed Gold Greatblud Ring with Emeralds', equippable=equippable_component)
        elif item_choice == 'j':
            equippable_component = Equippable(EquipmentSlots.RING_L, max_blood_bonus=200, defense_bonus=4)
            item = Entity(x, y, '/', libtcod.sky, 'Left Handed Gold Greatblud Ring with Diamonds', equippable=equippable_component)
        elif item_choice == 'k':
            equippable_component = Equippable(EquipmentSlots.RING_L, max_blood_bonus=200, defense_bonus=4, max_hp_bonus=100, power_bonus=4)
            item = Entity(x, y, '/', libtcod.blue, 'Left Handed Lesser Ring of the Allfather', equippable=equippable_component)

        return item

    def return_rings_right(self, x, y):
        item_chances = {
            'a': 10,
            'b': from_dungeon_level([[2, 4]], self.dungeon_level),
            'c': from_dungeon_level([[2, 4]], self.dungeon_level),
            'd': from_dungeon_level([[2, 4]], self.dungeon_level),
            'e': from_dungeon_level([[4, 4]], self.dungeon_level),
            'f': from_dungeon_level([[4, 4]], self.dungeon_level),
            'g': from_dungeon_level([[4, 4]], self.dungeon_level),
            'h': from_dungeon_level([[6, 4]], self.dungeon_level),
            'i': from_dungeon_level([[6, 4]], self.dungeon_level),
            'j': from_dungeon_level([[6, 4]], self.dungeon_level),
            'k': from_dungeon_level([[8, 4]], self.dungeon_level)
            }

        item_choice = random_choice_from_dict(item_chances)

        if item_choice == 'a':
            equippable_component = Equippable(EquipmentSlots.RING_R, max_blood_bonus=50)
            item = Entity(x, y, '/', libtcod.sky, 'Right Handed Iron Greatblud Ring', equippable=equippable_component)
        elif item_choice == 'b':
            equippable_component = Equippable(EquipmentSlots.RING_R, max_blood_bonus=50, power_bonus=1)
            item = Entity(x, y, '/', libtcod.sky, 'Right Handed Iron Greatblud Ring with Rubies', equippable=equippable_component)
        elif item_choice == 'c':
            equippable_component = Equippable(EquipmentSlots.RING_R,  max_blood_bonus=50, max_hp_bonus=25)
            item = Entity(x, y, '/', libtcod.sky, 'Right Handed Iron Greatblud Ring with Emeralds', equippable=equippable_component)
        elif item_choice == 'd':
            equippable_component = Equippable(EquipmentSlots.RING_R, max_blood_bonus=50, defense_bonus=1)
            item = Entity(x, y, '/', libtcod.sky, 'Right Handed Iron Greatblud Ring with Diamonds', equippable=equippable_component)
        elif item_choice == 'e':
            equippable_component = Equippable(EquipmentSlots.RING_R, max_blood_bonus=100, power_bonus=2)
            item = Entity(x, y, '/', libtcod.sky, 'Right Handed Silver Greatblud Ring with Rubies', equippable=equippable_component)
        elif item_choice == 'f':
            equippable_component = Equippable(EquipmentSlots.RING_R, max_blood_bonus=100, max_hp_bonus=50)
            item = Entity(x, y, '/', libtcod.sky, 'Right Handed Silver Greatblud Ring with Emeralds', equippable=equippable_component)
        elif item_choice == 'g':
            equippable_component = Equippable(EquipmentSlots.RING_R, max_blood_bonus=100, defense_bonus=2)
            item = Entity(x, y, '/', libtcod.sky, 'Right Handed Silver Greatblud Ring with Diamonds', equippable=equippable_component)
        elif item_choice == 'h':
            equippable_component = Equippable(EquipmentSlots.RING_R, max_blood_bonus=200, power_bonus=4)
            item = Entity(x, y, '/', libtcod.sky, 'Right Handed Gold Greatblud Ring with Rubies', equippable=equippable_component)
        elif item_choice == 'i':
            equippable_component = Equippable(EquipmentSlots.RING_R, max_blood_bonus=200, max_hp_bonus=100)
            item = Entity(x, y, '/', libtcod.sky, 'Right Handed Gold Greatblud Ring with Emeralds', equippable=equippable_component)
        elif item_choice == 'j':
            equippable_component = Equippable(EquipmentSlots.RING_R, max_blood_bonus=200, defense_bonus=4)
            item = Entity(x, y, '/', libtcod.sky, 'Right Handed Gold Greatblud Ring with Diamonds', equippable=equippable_component)
        elif item_choice == 'k':
            equippable_component = Equippable(EquipmentSlots.RING_R, max_blood_bonus=200, defense_bonus=4, max_hp_bonus=100, power_bonus=4)
            item = Entity(x, y, '/', libtcod.blue, 'Right Handed Lesser Ring of the Allfather', equippable=equippable_component)

        return item