from utils.read_file import Utils
from upgraded_int_code import UpgradedIntCode

def main():
    input = Utils.read_file("input.txt")
    result = UpgradedIntCode.process_code(input)
    print(result)

if __name__ == "__main__":
    main()
