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

    def test_with_12_and_additional_fuel(self):
        result = FuelCounterUpper.calc_total_fuel_for_module(12)
        self.assertEqual(2, result)

    def test_with_14_and_additional_fuel(self):
        result = FuelCounterUpper.calc_total_fuel_for_module(14)
        self.assertEqual(2, result)

    def test_with_1969_and_additional_fuel(self):
        result = FuelCounterUpper.calc_total_fuel_for_module(1969)
        self.assertEqual(966, result)

    def test_with_100756_and_additional_fuel(self):
        result = FuelCounterUpper.calc_total_fuel_for_module(100756)
        self.assertEqual(50346, result)
