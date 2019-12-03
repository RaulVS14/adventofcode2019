import re


class ManhattanDistance:
    @staticmethod
    def calculate_distance(wire1, wire2):
        path_wire1 = ManhattanDistance.trace_path(wire1)
        path_wire2 = ManhattanDistance.trace_path(wire2)

        intersections = set(path_wire1.keys()) & set(path_wire2.keys())
        distance = min([abs(x) + abs(y) for (x, y) in intersections])
        return distance

    @staticmethod
    def trace_path(wire):
        path = {}
        coords = (0, 0)
        num_of_steps = 0
        for i in wire:
            direction, distance = re.match("([RULD])(\d*)", i).groups()
            for _ in range(int(distance)):
                coords = ManhattanDistance.move(direction, coords)
                num_of_steps += 1
                if coords not in path:
                    path[coords] = num_of_steps
        return path

    @staticmethod
    def move(direction, coords):
        coord_x = coords[0]
        coord_y = coords[1]
        amount = 1
        if direction == "R":
            coord_x += amount

        if direction == "L":
            coord_x -= amount

        if direction == "U":
            coord_y += amount

        if direction == "D":
            coord_y -= amount

        return (coord_x, coord_y)
