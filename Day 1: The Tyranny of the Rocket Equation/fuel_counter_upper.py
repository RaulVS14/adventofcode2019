from math import floor


class FuelCounterUpper:
    sum = 0

    def read_file(self, input):
        with open(input, 'r') as file:
            for line in file:
                self.sum += self.calc_total_fuel_for_module(int(line.strip()))
        return self

    @staticmethod
    def calc_fuel_requirement(mass):
        return floor(mass / 3.0) - 2

    @staticmethod
    def calc_total_fuel_for_module(mass):
        additional_fuel_sum = 0
        mass_for_fuel = mass
        while ((mass_for_fuel := FuelCounterUpper.calc_fuel_requirement(mass_for_fuel)) > 0):
            additional_fuel_sum += mass_for_fuel
        return additional_fuel_sum
