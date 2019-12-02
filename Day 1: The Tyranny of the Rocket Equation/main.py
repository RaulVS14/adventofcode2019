from fuel_counter_upper import FuelCounterUpper
def main():
    fuel_counter_upper = FuelCounterUpper().read_file("input.txt")
    print(fuel_counter_upper.sum)

if __name__ == "__main__":
    main()