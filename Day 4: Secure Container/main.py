from secure_container import SecureContainer


def main():
    start = 387638
    end = 919123
    print(len(SecureContainer.password_finder(start, end)))


if __name__ == "__main__":
    main()
