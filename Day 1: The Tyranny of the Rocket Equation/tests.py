from unittest import TestCase
from fuel_counter_upper import FuelCounterUpper
class FuelCounterUpperTestCase(TestCase):
    def test_with_12(self):
        result = FuelCounterUpper.calc_fuel_requirement(12)
        self.assertEqual(2, result)

    def test_with_14(self):
        result = FuelCounterUpper.calc_fuel_requirement(14)
        self.assertEqual(2, result)

    def test_with_1969(self):
        result = FuelCounterUpper.calc_fuel_requirement(1969)
        self.assertEqual(654, result)

    def test_with_100756(self):
        result = FuelCounterUpper.calc_fuel_requirement(100756)
        self.assertEqual(33583, result)