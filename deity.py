from random import randint

class deity:
    """This is the thing your programming teacher told you never to do.... a god class."""

    def __init__ (self):
        self.entity = []
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

