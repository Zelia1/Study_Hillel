# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здаровья.
#
# Есть три типа юнитов - маги, лучники и рыцари.
# У магов есть дополнительная характеристика - тип магии (воздух, огонь, вода)
# У лучников есть дополнительная характеристика - тип лука (лук, арбалет)
# У рыцарей есть дополнительная характеристика - тип оружия (меч, топор, пика)

# Каждый юнит может увеличить свой базовый навык на 1 пункт, максимум 10.
# Маг увеличивает интелект.
# Лучник увеличивает ловкость.
# Рыцарь увеличивает силу.
# Написать метод увеличения базового навыка (в родительском классе).

# Предложить свою реализацию классов Unit, Mage, Archer, Knight.

class Unit:

    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.hp = 100
        self.intellect = 1
        self.agility = 1
        self.strength = 1
        self.class_unit = ""
        self.damage_type = ""

    @property
    def type_damage(self):
        return self.damage_type

    def __repr__(self):
        if self.class_unit == "mage":
            return f"Класс игрока: {self.class_unit}, имя: {self.name}, клан: {self.clan}, " \
                   f"жизни: {self.hp}, интелект: {self.intellect}, вид урона: {self.damage_type}"
        if self.class_unit == "archer":
            return f"Класс игрока: {self.class_unit}, имя: {self.name}, клан: {self.clan}, " \
                   f"жизни: {self.hp}, ловкость: {self.agility}, вид урона: {self.damage_type}"
        if self.class_unit == "knight":
            return f"Класс игрока: {self.class_unit}, имя: {self.name}, клан: {self.clan}, " \
                   f"жизни: {self.hp}, сила: {self.strength}, вид урона: {self.damage_type}"

    def to_heal(self):
        if self.hp < 100:
            self.hp += 10
            if self.hp > 100:
                self.hp = 100
        return self.hp

    def skill_increase(self):
        if self.class_unit == "mage":
            if self.intellect < 10:
                self.intellect += 1
        if self.class_unit == "archer":
            if self.agility < 10:
                self.agility += 1
        if self.class_unit == "knight":
            if self.strength < 10:
                self.strength += 1


class Mage(Unit):
    def __init__(self, name, clan, damage_type):
        super().__init__(name, clan)
        self.name = name
        self.damage_type = damage_type
        self.class_unit = "mage"

    @property
    def type_damage(self):
        return self.damage_type


class Archer(Unit):
    def __init__(self, name, clan, damage_type):
        super().__init__(name, clan)
        self.name = name
        self.damage_type = damage_type
        self.class_unit = "archer"

    @property
    def type_damage(self):
        return self.damage_type


class Knight(Unit):
    def __init__(self, name, clan, damage_type):
        super().__init__(name, clan)
        self.name = name
        self.damage_type = damage_type
        self.class_unit = "knight"

    @property
    def type_damage(self):
        return self.damage_type


Mage_1 = Mage("Toombli", "Idiots", "Fire")
Archer_1 = Archer("Legolas", "Сross-eyed", "Bow")
Knight_1 = Knight("Aragorn", "Сrooked", "Sword")
