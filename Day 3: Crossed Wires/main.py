from manhattan_distance import ManhattanDistance
from utils.read_file import Utils


def main():
    file = Utils.read_file("input.txt")
    wire1 = file[0].split(',')
    wire2 = file[1].split(',')
    print(ManhattanDistance.calculate_distance(wire1, wire2))

    print(ManhattanDistance.intersection_of_least_amount_of_steps(wire1, wire2))


if __name__ == "__main__":
    main()
