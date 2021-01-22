import json
import os


class UnitReader:
    def __init__(self, path_file):
        self._path_file = path_file
        self.data = None

    def __repr__(self):
        return self._path_file

    def read_unit(self):
        with open(self._path_file, "r") as file:
            self.data = json.load(file)

    def skill_increase(self):
        if self.data["name"] == "Mage":
            self.data["skills"][0]["intelligence"] += 1
        elif self.data["name"] == "Archer":
            self.data["skills"][0]["agility"] += 1
        elif self.data["name"] == "Knight":
            self.data["skills"][0]["strength"] += 1
        return self.data

    def to_heal(self):
        if self.data["health"] < 100:
            self.data["health"] += 10
            if self.data["health"] > 100:
                self.data["health"] = 100
        return self.data["health"]


class Mage(UnitReader):
    def increase_skill(self):
        if self.data["skills"][0]["intelligence"] < 10:
            return mage_worker.skill_increase()


class Archer(UnitReader):
    def increase_skill(self):
        if self.data["skills"][0]["agility"] < 10:
            return archer_worker.skill_increase()


class Knight(UnitReader):
    def increase_skill(self):
        if self.data["skills"][0]["strength"] < 10:
            return knight_worker.skill_increase()


folder = "Unit_data"
filename_mage = "Mage.json"
filename_archer = "Archer.json"
filename_knight = "Knight.json"

mage_worker = Mage(os.path.join(folder, filename_mage))
archer_worker = Archer(os.path.join(folder, filename_archer))
knight_worker = Knight(os.path.join(folder, filename_knight))

mage_worker.read_unit()
archer_worker.read_unit()
knight_worker.read_unit()
knight_worker.increase_skill()
knight_worker.increase_skill()
archer_worker.increase_skill()
print(archer_worker.data)
print(mage_worker.data)
print(knight_worker.data)
# print(mage_worker.data)
