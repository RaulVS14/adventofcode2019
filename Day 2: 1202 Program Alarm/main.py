from int_code import IntCode

from utils.read_file import Utils


def main():
    file = Utils.read_file("input.txt")

    int_code_program = file[0].split(',')
    int_code_program[1] = 12
    int_code_program[2] = 2
    print(IntCode.process_code(int_code_program)[0])

    int_code_program = file[0].split(',')
    noun, verb = IntCode.find_inputs(int_code_program, 19690720)
    if noun and verb:
        print(100 * noun + verb)


if __name__ == "__main__":
    main()
