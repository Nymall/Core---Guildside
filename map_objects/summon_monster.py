import libtcodpy as libtcod
import random

from components.ai import BasicMonster, BasicShaman
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from components.fighter import Fighter
from components.item import Item
from components.stairs import Stairs
from components.inventory import Inventory

from equipment_slots import EquipmentSlots

from entity import Entity

from game_messages import Message

from random_utils import from_dungeon_level, random_choice_from_dict

from render_functions import RenderOrder

from enum import *

class gen_monsters:
    def monster_all(Enum):
        KOBOLD = auto()
        RAZORTOOTH = auto()
        KHUNTER = auto()
        KGLASSMITH = auto()
        GOBLIN = auto()
        C_GOBLIN = auto()
        CB_GOBLIN = auto()
        CO_GOBLIN = auto()
        CS_GOBLIN = auto()
        ORC = auto()
        TROLL = auto()

        def ret_mon():
            mon = random.choice(list(monster_all))
            return mon

    def monster_goblin(Enum):
        GOBLIN = auto()
        C_GOBLIN = auto()
        CB_GOBLIN = auto()
        CO_GOBLIN = auto()
        CS_GOBLIN = auto()
    
        def ret_mon():
            mon = random.choice(list(monster_goblin))
            return mon

    def monster_kobold(Enum):
        KOBOLD = auto()
        RAZORTOOTH = auto()
        KHUNTER = auto()
        KGLASSMITH = auto()
    
        def ret_mon():
            mon = random.choice(list(monster_kobold))
            return mon

    def monster_orc(Enum):
        ORC = auto()
        TROLL = auto()

        def ret_mon():
            mon = random.choice(list(monster_orc))
            return mon

    def monster_stats(x, y, sect=monster_all):
        selector = sect.ret_mon()

        if selector == monster_all.KOBOLD:
            monster = Entity(x, y, 'k', libtcod.desaturated_green, 'Kobold', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=10, defense=0, power=1, xp=35), ai=BasicMonster(), inventory=Inventory(5))
        if selector == monster_all.RAZORTOOTH:
            monster = Entity(x, y, 'k', libtcod.desaturated_green, 'Kolbold Razortooth', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=20, defense=0, power=2, xp=45), ai=BasicMonster(), inventory=Inventory(5))
        if selector == monster_all.KHUNTER:
            monster = Entity(x, y, 'k', libtcod.desaturated_green, 'Kolbold Hunter', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=25, defense=1, power=3, xp=50), ai=BasicMonster(), inventory=Inventory(5))
        if selector == monster_all.KGLASSMITH:
            monster = Entity(x, y, 'k', libtcod.desaturated_green, 'Kolbold Glasssmith', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=30, defense=1, power=2, xp=50), ai=BasicMonster(), inventory=Inventory(5))
            monster.inventory.add_item(Entity(0, 0, '/', libtcod.sky, 'Handfull of glass shards', equippable=Equippable(EquipmentSlots.MAIN_HAND, power_bonus=2)))
        elif selector == monster_all.GOBLIN:
            monster = Entity(x, y, 'g', libtcod.green, 'Goblin', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=15, defense=0, power=2, xp=40), ai=BasicMonster(), inventory=Inventory(5))
        elif selector == monster_all.C_GOBLIN:
            monster = Entity(x, y, 'g', libtcod.green, 'Clanfear Goblin', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=15, defense=1, power=2, xp=45), ai=BasicMonster(), inventory=Inventory(5))
        elif selector == monster_all.CB_GOBLIN:
            monster = Entity(x, y, 'g', libtcod.green, 'Clanfear Goblin Brawler', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=15, defense=2, power=3, xp=60), ai=BasicMonster(), inventory=Inventory(5))
            monster.inventory.add_item(Entity(0, 0, '-', libtcod.sky, 'Rusty Dagger', equippable=Equippable(EquipmentSlots.MAIN_HAND, power_bonus=2)))
            monster.inventory.add_item(Entity(0, 0, '#', libtcod.brown, 'Ratty Peasant Shirt', equippable=Equippable(EquipmentSlots.CHEST, defense_bonus=1)))
        elif selector == monster_all.CO_GOBLIN:
            monster = Entity(x, y, 'g', libtcod.green, 'Clanfear Goblin Organizer', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=25, defense=2, power=3, xp=80), ai=BasicMonster(), inventory=Inventory(5))
            monster.inventory.add_item(Entity(0, 0, '-', libtcod.sky, 'Rusty Dagger', equippable=Equippable(EquipmentSlots.MAIN_HAND, power_bonus=2)))
            monster.inventory.add_item(Entity(0, 0, '#', libtcod.brown, 'Ratty Peasant Shirt', equippable=Equippable(EquipmentSlots.CHEST, defense_bonus=1)))
            monster.inventory.add_item(Entity(0, 0, '#', libtcod.brown, 'Ratty Cloth Toque', equippable=Equippable(EquipmentSlots.HELMET, max_hp_bonus=10)))
            monster.inventory.add_item(Entity(0, 0, '#', libtcod.grey, 'Rusty Iron Ring', equippable=Equippable(EquipmentSlots.RING_R, max_blood_bonus=10)))
        elif selector == monster_all.CS_GOBLIN:
            monster = Entity(x, y, 'g', libtcod.light_green, 'Clanfear Goblin Shaman', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=45, defense=2, power=3, xp=100), ai=BasicShaman(), inventory=Inventory(5))
            monster.inventory.add_item(Entity(0, 0, '-', libtcod.sky, 'Staff of Impovrished Lightning', item=Item(use_function=cast_lightning_chance, damage=20, maximum_range=6)))
            monster.inventory.add_item(Entity(0, 0, '#', libtcod.brown, 'Ratty Peasant Shirt', equippable=Equippable(EquipmentSlots.CHEST, defense_bonus=1)))
            monster.inventory.add_item(Entity(0, 0, '#', libtcod.brown, 'Ratty Cloth Toque', equippable=Equippable(EquipmentSlots.HELMET, max_hp_bonus=10)))
            monster.inventory.add_item(Entity(0, 0, '#', libtcod.grey, 'Rusty Iron Ring', equippable=Equippable(EquipmentSlots.RING_R, max_blood_bonus=10)))
        elif selector == monster_all.ORC:
            monster = Entity(x, y, 'o', libtcod.desaturated_green, 'Orc', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=25, defense=1, power=2, xp=45), ai=BasicMonster(), inventory=Inventory(5))
        elif selector == monster_all.TROLL:
            monster = Entity(x, y, 'T', libtcod.green, 'Troll', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=30, defense=2, power=6, xp=80), ai=BasicMonster(), inventory=Inventory(5))