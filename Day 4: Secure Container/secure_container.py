class SecureContainer:
    @staticmethod
    def criteria_check(password):
        pass_as_list = [int(x) for x in str(password)]
        length = len(pass_as_list)
        if length > 6:
            return False

        pair = False
        growing = True

        for i in range(length - 1):
            if pass_as_list[i] == pass_as_list[i + 1]:
                pair = True

            if pass_as_list[i] > pass_as_list[i + 1]:
                growing = False
        return pair and growing

    @staticmethod
    def password_finder(start, end):
        result = []
        for i in range(start, end):
            if SecureContainer.criteria_check(i):
                result.append(i)
        return result