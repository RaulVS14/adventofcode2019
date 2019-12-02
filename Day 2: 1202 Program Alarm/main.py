from int_code import IntCode
def main():
    read_code = IntCode().read_file("input.txt")
    read_code.code_array[1] = 12
    read_code.code_array[2] = 2
    print(read_code.process_code(read_code.code_array))

if __name__ == "__main__":
    main()