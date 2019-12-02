class Utils:
    @staticmethod
    def read_file(filename):
        lines_array = []
        with open(filename, 'r') as file:
            for line in file:
                lines_array.append(line.strip())
        return lines_array
