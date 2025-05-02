from valid import Valid
import unittest

class Test_TestValid(unittest.TestCase):
    
    def test_zip_happy(self):
        self.assertTrue(Valid.validate_zip("17701"))

    def test_zip_bad(self):
        f = open("blns.payloads", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Valid.validate_zip(str(line)))