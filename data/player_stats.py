from data.dice import Dice
from data.level_chart import level_chart
class Stats():
    def __init__(self, strength, constitution, intelligence, wisdom, charisma, dexterity, hp, base_damage, xp):
        self.strength = strength
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.dexterity = dexterity
        self.hp = hp
        self.level = 1
        self.base_damage = base_damage
        self.xp = xp
        proficiency = 0
        level = self.level
        if level_chart[1] > self.xp > level_chart[0]:
            level = 1
            proficiency += 2
        if level_chart[2] > self.xp > level_chart[1]:
            level = 2
            proficiency += 2
        if level_chart[3] > self.xp > level_chart[2]:
            level = 3
            proficiency += 2
        if level_chart[4] > self.xp > level_chart[3]:
            level = 4
            proficiency += 2
        if level_chart[5] > self.xp > level_chart[4]:
            level = 5
            proficiency += 3
        if level_chart[6] > self.xp > level_chart[5]:
            level = 6
            proficiency += 3
        if level_chart[7] > self.xp > level_chart[6]:
            level = 7
            proficiency += 3
        if level_chart[8] > self.xp > level_chart[7]:
            level = 8
            proficiency += 3
        if level_chart[9] > self.xp > level_chart[8]:
            level = 9
            proficiency += 4
        if level_chart[10] > self.xp > level_chart[9]:
            level = 10
            proficiency += 4
        if level_chart[11] > self.xp > level_chart[10]:
            level = 11
            proficiency += 4
        if level_chart[12] > self.xp > level_chart[11]:
            level = 12
            proficiency += 4
        if level_chart[13] > self.xp > level_chart[12]:
            level = 13
            proficiency += 5
        if level_chart[14] > self.xp > level_chart[13]:
            level = 14
            proficiency += 5
        if level_chart[15] > self.xp > level_chart[14]:
            level = 15
            proficiency += 5
        if level_chart[16] > self.xp > level_chart[15]:
            level = 16
            proficiency += 5
        if level_chart[17] > self.xp > level_chart[16]:
            level = 17
            proficiency += 6
        if level_chart[18] > self.xp > level_chart[17]:
            level = 18
            proficiency += 6
        if level_chart[19] > self.xp > level_chart[18]:
            level = 19
            proficiency += 6
        if self.xp >= level_chart[19]:
            level = 20
            proficiency += 6
        self.chance = Dice.d20_rolled()
        print('D20: ' + str(self.chance))
        self.crit_damage = self.base_damage
        if self.chance >= 18:
            self.crit_damage = self.base_damage * 2
            print('Critical!')
        self.dice_bonus = 0
        dice_bonus = self.dice_bonus
        if self.chance >= 5:
            dice_bonus = -int(self.chance)
        elif self.chance <= 6:
            dice_bonus = int(self.chance)
        self.total_damage = self.crit_damage + (level * 2) + dice_bonus
