class SecureContainer:
    @staticmethod
    def criteria_check(password):
        pass_as_list = [int(x) for x in str(password)]
        length = len(pass_as_list)
        if length > 6:
            return False

        pairs = {}
        for i in range(length - 1):
            if pass_as_list[i] == pass_as_list[i + 1]:
                if pass_as_list[i] not in pairs:
                    pairs[pass_as_list[i]] = 1
                pairs[pass_as_list[i + 1]] += 1
            if pass_as_list[i] > pass_as_list[i + 1]:
                return False
        return pairs

    @staticmethod
    def advance_criteria_check(password):
        pairs = SecureContainer.criteria_check(password)
        if pairs:
            for key, value in pairs.items():
                if value == 2:
                    return True

        return False

    @staticmethod
    def password_finder(start, end):
        result = []
        for i in range(start, end):
            if SecureContainer.criteria_check(i):
                result.append(i)
        return result

    @staticmethod
    def advanced_password_finder(start, end):
        result = []
        for i in range(start, end):
            if SecureContainer.advance_criteria_check(i):
                result.append(i)
        return result
