"""
-- Created by: Ashok Kumar Pant
-- Created on: 4/5/21
"""
from unittest.case import TestCase

from ml_training.main import print_hi


class MLTrainingMainModuleTest(TestCase):
    def test_print_name(self):
        output = print_hi("Ashok")
        self.assertEqual("Hi, Ashok", output)
