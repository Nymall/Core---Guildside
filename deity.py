from random import randint
import xml.dom.minidom

from components.ai import BasicMonster
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from components.fighter import Fighter
from components.item import Item

from entity import Entity

class deity:
    """This is the thing your programming teacher told you never to do.... a god class."""

    def __init__ (self):
        self.entity = []
        self.itemlist = []
        self.max_depth = randint(4, 10)

    def add_new_entity(self, entity):
        self.entity.append(entity)

    def get_entity(self, entity):
        return self.entity[entity]

    def remove_entity(self, entity):
        self.entity.remove(entity)

    def set_player(self, entity):
        self.player = entity

    def get_player(self, entity):
        return self.player

    def generate_item_list(self):
        # https://www.guru99.com/manipulating-xml-with-python.html
        # Browse through the item list, and enumerate items by cycling through all xml files
        print()

    def readlist(self, file):
        doc = xml.dom.minidom.parse(file)
        items = doc.getElementsByTagName("item")
        for ind_items in items:
            name = ind_items.getElementsByTagName("name")
            if self.itemlist[name] == name:
                #do nothing
                print()
            else:
                # item_component = Item(use_function=heal, amount=20)
                # item = Entity(x, y, '!', libtcod.violet, 'Lesser Healing Potion', render_order=RenderOrder.ITEM, item=item_component)
                self.itemlist[name] = Entity(0, 0, ind_items.getElementsByTagName("symbol"), ind_items.getElementsByTagName("color"), ind_items.getElementsByTagName("name"), ind_items.getElementsByTagName("rorder"), item=Item(ind_items.getElementsByTagName("use")))


    def generate_monster_lists(self):
        print()

    def generate_level_lists(self):
        print()


