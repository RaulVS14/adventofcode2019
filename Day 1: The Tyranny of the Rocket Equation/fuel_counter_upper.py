from math import floor


class FuelCounterUpper:
    sum = 0

    def read_file(self, input):
        with open(input, 'r') as file:
            for line in file:
                self.sum += self.calc_fuel_requirement(int(line.strip()))
        return self

    @staticmethod
    def calc_fuel_requirement(mass):
        return floor(mass / 3.0) - 2
