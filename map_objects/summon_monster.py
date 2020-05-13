import libtcodpy as libtcod
from random import randint

from components.ai import BasicMonster
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

class monster_all(ENUM):
    KOBOLD = 20,
    GOBLIN = 20,
    C_GOBLIN = 20,
    CB_GOBLIN = 20,
    CO_GOBLIN = 20,
    CS_GOBLIN = 20,
    ORC = 20,
    TROLL = from_dungeon_level([[15, 3], [30, 5], [60, 7]], self.dungeon_level)

class monster_stats(monster):
    selector = 1 #add all enum numbers

    if selector == KOBOLD:
        monster = Entity(x, y, 'k', libtcod.desaturated_green, 'Kobold', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=10, defense=0, power=1, xp=35), ai=BasicMonster(), inventory=Inventory(5))
    elif selector == GOBLIN:
        monster = Entity(x, y, 'g', libtcod.green, 'Goblin', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=15, defense=0, power=2, xp=40), ai=BasicMonster(), inventory=Inventory(5))
    elif selector == C_GOBLIN:
        monster = Entity(x, y, 'g', libtcod.green, 'Clanfear Goblin', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=15, defense=1, power=2, xp=45), ai=BasicMonster(), inventory=Inventory(5))
    elif selector == CB_GOBLIN:
        monster = Entity(x, y, 'g', libtcod.green, 'Clanfear Goblin Brawler', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=15, defense=2, power=3, xp=60), ai=BasicMonster(), inventory=Inventory(5))
        monster.inventory.add_item(Entity(0, 0, '-', libtcod.sky, 'Rusty Dagger', equippable=Equippable(EquipmentSlots.MAIN_HAND, power_bonus=2)))
        monster.inventory.add_item(Entity(0, 0, '#', libtcod.brown, 'Ratty Peasant Shirt', equippable=Equippable(EquipmentSlots.CHEST, defense_bonus=1)))
    elif selector == CO_GOBLIN:
        monster = Entity(x, y, 'g', libtcod.green, 'Clanfear Goblin Organizer', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=25, defense=2, power=3, xp=80), ai=BasicMonster(), inventory=Inventory(5))
        monster.inventory.add_item(Entity(0, 0, '-', libtcod.sky, 'Rusty Dagger', equippable=Equippable(EquipmentSlots.MAIN_HAND, power_bonus=2)))
        monster.inventory.add_item(Entity(0, 0, '#', libtcod.brown, 'Ratty Peasant Shirt', equippable=Equippable(EquipmentSlots.CHEST, defense_bonus=1)))
        monster.inventory.add_item(Entity(0, 0, '#', libtcod.brown, 'Ratty Cloth Toque', equippable=Equippable(EquipmentSlots.HELMET, max_hp_bonus=10)))
        monster.inventory.add_item(Entity(0, 0, '#', libtcod.grey, 'Rusty Iron Ring', equippable=Equippable(EquipmentSlots.RING_R, max_blood_bonus=10)))
    elif selector == CS_GOBLIN:
        monster = Entity(x, y, 'g', libtcod.light_green, 'Clanfear Goblin Shaman', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=25, defense=2, power=3, xp=80), ai=BasicMonster(), inventory=Inventory(5))
        monster.inventory.add_item(Entity(0, 0, '-', libtcod.sky, 'Staff of Impovrished Lightning', item=Item(use_function=cast_lightning_chance, damage=20, maximum_range=6)))
        monster.inventory.add_item(Entity(0, 0, '#', libtcod.brown, 'Ratty Peasant Shirt', equippable=Equippable(EquipmentSlots.CHEST, defense_bonus=1)))
        monster.inventory.add_item(Entity(0, 0, '#', libtcod.brown, 'Ratty Cloth Toque', equippable=Equippable(EquipmentSlots.HELMET, max_hp_bonus=10)))
        monster.inventory.add_item(Entity(0, 0, '#', libtcod.grey, 'Rusty Iron Ring', equippable=Equippable(EquipmentSlots.RING_R, max_blood_bonus=10)))
    elif selector == ORC:
        monster = Entity(x, y, 'o', libtcod.desaturated_green, 'Orc', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=25, defense=1, power=2, xp=45), ai=BasicMonster(), inventory=Inventory(5))
    elif selector == TROLL:
        monster = Entity(x, y, 'T', libtcod.green, 'Troll', blocks=True, render_order=RenderOrder.ACTOR, fighter=Fighter(hp=30, defense=2, power=6, xp=80), ai=BasicMonster(), inventory=Inventory(5))