from fuel_counter_upper import FuelCounterUpper

from utils.read_file import Utils


def main():
    file = Utils.read_file('input.txt')
    fuel_counter = FuelCounterUpper()
    sum = 0
    total_fuel_sum = 0
    for line in file:
        module_mass = int(line)
        sum += fuel_counter.calc_fuel_requirement(module_mass)
        total_fuel_sum += fuel_counter.calc_total_fuel_for_module(module_mass)
    print(sum)
    print(total_fuel_sum)


if __name__ == "__main__":
    main()
