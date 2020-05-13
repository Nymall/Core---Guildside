from equipment_slots import EquipmentSlots


class Equipment:
    def __init__(self, main_hand=None, off_hand=None, chest=None, ring_r=None, ring_l=None, Helmet=None, Greaves=None):
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.chest = chest
        self.ring_r = ring_r
        self.ring_l = ring_l
        self.helmet = Helmet
        self.greaves = Greaves

    @property
    def max_hp_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable: bonus += self.main_hand.equippable.max_hp_bonus
        if self.off_hand and self.off_hand.equippable: bonus += self.off_hand.equippable.max_hp_bonus
        if self.chest and self.chest.equippable: bonus += self.chest.equippable.max_hp_bonus
        if self.ring_r and self.ring_r.equippable: bonus += self.ring_r.equippable.max_hp_bonus
        if self.ring_l and self.ring_l.equippable: bonus += self.ring_l.equippable.max_hp_bonus
        if self.helmet and self.helmet.equippable: bonus += self.helmet.equippable.max_hp_bonus
        if self.greaves and self.greaves.equippable: bonus += self.greaves.equippable.max_hp_bonus

        return bonus

    @property
    def max_blood_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable: bonus += self.main_hand.equippable.max_blood_bonus
        if self.off_hand and self.off_hand.equippable: bonus += self.off_hand.equippable.max_blood_bonus
        if self.chest and self.chest.equippable: bonus += self.chest.equippable.max_blood_bonus
        if self.ring_r and self.ring_r.equippable: bonus += self.ring_r.equippable.max_blood_bonus
        if self.ring_l and self.ring_l.equippable: bonus += self.ring_l.equippable.max_blood_bonus
        if self.helmet and self.helmet.equippable: bonus += self.helmet.equippable.max_blood_bonus
        if self.greaves and self.greaves.equippable: bonus += self.greaves.equippable.max_blood_bonus

        return bonus

    @property
    def power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable: bonus += self.main_hand.equippable.power_bonus
        if self.off_hand and self.off_hand.equippable: bonus += self.off_hand.equippable.power_bonus
        if self.chest and self.chest.equippable: bonus += self.chest.equippable.power_bonus
        if self.ring_r and self.ring_r.equippable: bonus += self.ring_r.equippable.power_bonus
        if self.ring_l and self.ring_l.equippable: bonus += self.ring_l.equippable.power_bonus
        if self.helmet and self.helmet.equippable: bonus += self.helmet.equippable.power_bonus
        if self.greaves and self.greaves.equippable: bonus += self.greaves.equippable.power_bonus

        return bonus

    @property
    def defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable: bonus += self.main_hand.equippable.defense_bonus
        if self.off_hand and self.off_hand.equippable: bonus += self.off_hand.equippable.defense_bonus
        if self.chest and self.chest.equippable: bonus += self.chest.equippable.defense_bonus
        if self.ring_r and self.ring_r.equippable: bonus += self.ring_r.equippable.defense_bonus
        if self.ring_l and self.ring_l.equippable: bonus += self.ring_l.equippable.defense_bonus
        if self.helmet and self.helmet.equippable: bonus += self.helmet.equippable.defense_bonus
        if self.greaves and self.greaves.equippable: bonus += self.greaves.equippable.defense_bonus

        return bonus

    def toggle_equip(self, equippable_entity):
        results = []

        slot = equippable_entity.equippable.slot

        if slot == EquipmentSlots.MAIN_HAND:
            if self.main_hand == equippable_entity:
                self.main_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.main_hand:
                    results.append({'dequipped': self.main_hand})

                self.main_hand = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.OFF_HAND:
            if self.off_hand == equippable_entity:
                self.off_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.off_hand:
                    results.append({'dequipped': self.off_hand})

                self.off_hand = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.CHEST:
            if self.chest == equippable_entity:
                self.chest = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.chest:
                    results.append({'dequipped': self.chest})

                self.chest = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.RING_L:
            if self.ring_l == equippable_entity:
                self.ring_l = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.ring_l:
                    results.append({'dequipped': self.ring_l})

                self.ring_l = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.RING_R:
            if self.ring_r == equippable_entity:
                self.ring_r = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.ring_r:
                    results.append({'dequipped': self.ring_r})

                self.ring_r = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.HELMET:
            if self.helmet == equippable_entity:
                self.helmet = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.helmet:
                    results.append({'dequipped': self.helmet})

                self.helmet = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.GREAVES:
            if self.greaves == equippable_entity:
                self.greaves = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.greaves:
                    results.append({'dequipped': self.greaves})

                self.greaves = equippable_entity
                results.append({'equipped': equippable_entity})

        return results
