from fuel_counter_upper import FuelCounterUpper
def main():
    fuel_requirement = FuelCounterUpper().read_file("input.txt")
    print(fuel_requirement.sum)

if __name__ == "__main__":
    main()