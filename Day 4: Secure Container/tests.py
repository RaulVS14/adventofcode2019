from unittest import TestCase
from secure_container import SecureContainer


class SecureContainerTestCase(TestCase):
    def test_1(self):
        result = SecureContainer.criteria_check(111111)
        self.assertTrue(result)

    def test_2(self):
        result = SecureContainer.criteria_check(223450)
        self.assertFalse(result)

    def test_3(self):
        result = SecureContainer.criteria_check(123789)
        self.assertFalse(result)

    def test_4(self):
        result = SecureContainer.advance_criteria_check(112233)
        self.assertTrue(result)

    def test_5(self):
        result = SecureContainer.advance_criteria_check(123444)
        self.assertFalse(result)

    def test_6(self):
        result = SecureContainer.advance_criteria_check(111122)
        self.assertTrue(result)
