from unittest import TestCase
from int_code import IntCode


class IntCodeTestCase(TestCase):

    def test_process_code_1(self):
        result = IntCode.process_code([1, 0, 0, 0, 99])
        self.assertEqual([2, 0, 0, 0, 99], result)

    def test_process_code_2(self):
        result = IntCode.process_code([2,3,0,3,99])
        self.assertEqual([2,3,0,6,99], result)

    def test_process_code_3(self):
        result = IntCode.process_code([2,4,4,5,99,0])
        self.assertEqual([2,4,4,5,99,9801], result)

    def test_process_code_4(self):
        result = IntCode.process_code([1,1,1,4,99,5,6,0,99])
        self.assertEqual([30,1,1,4,2,5,6,0,99], result)