class IntCode:
    @staticmethod
    def process_code(instructions):
        for i in range(0, len(instructions) - 4, 4):
            opcode = int(instructions[i])
            if opcode == 99:
                break
            var1 = int(instructions[int(instructions[i + 1])])
            var2 = int(instructions[int(instructions[i + 2])])
            loc = int(instructions[i + 3])

            value = 0
            if opcode == 2:
                value = var1 * var2
            elif opcode == 1:
                value = var1 + var2

            instructions[loc] = value
        return instructions
