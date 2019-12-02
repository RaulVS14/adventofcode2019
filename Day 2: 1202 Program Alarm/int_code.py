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

    @staticmethod
    def find_inputs(input, output):
        for noun in range(100):
            for verb in range(100):
                initial_input = input[:]
                initial_input[1] = noun
                initial_input[2] = verb
                IntCode.process_code(initial_input)
                if initial_input[0] == output:
                    return noun, verb
        return None, None
