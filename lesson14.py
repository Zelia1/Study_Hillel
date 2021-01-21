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
        if "intelligence" in self.data:
            if self.data["intelligence"] < 10:
                self.data["intelligence"] += 1
        if "agility" in self.data:
            if self.data["agility"] < 10:
                self.data["agility"] += 1
        if "strength" in self.data:
            if self.data["strength"] < 10:
                self.data["strength"] += 1


class Mage(UnitReader):
    def to_heal(self):
        if self.data["health"] < 100:
            self.data["health"] += 10
            if self.data["health"] > 100:
                self.data["health"] -= self.data["health"] % 10
        return self.data["health"]


class Archer(UnitReader):
    def to_heal(self):
        if self.data["health"] < 100:
            self.data["health"] += 10
            if self.data["health"] > 100:
                self.data["health"] -= self.data["health"] % 10
        return self.data["health"]


class Knight(UnitReader):
    def to_heal(self):
        if self.data["health"] < 100:
            self.data["health"] += 10
            if self.data["health"] > 100:
                self.data["health"] -= self.data["health"] % 10
        return self.data["health"]


folder = "Unit_data"
filename_mage = "Mage.json"
filename_archer = "Archer.json"
filename_knight = "Knight.json"

mage_worker = Mage(os.path.join(folder, filename_mage))
archer_worker = Archer(os.path.join(folder, filename_archer))
knight_worker = Knight(os.path.join(folder, filename_knight))

mage_worker.read_unit()
mage_worker.to_heal()
mage_worker.to_heal()
mage_worker.to_heal()
mage_worker.to_heal()
mage_worker.to_heal()
mage_worker.to_heal()
mage_worker.to_heal()
mage_worker.to_heal()
mage_worker.to_heal()
mage_worker.to_heal()

print(mage_worker.data)


