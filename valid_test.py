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

    def test_response_code_happy(self):
        self.assertTrue(Valid.validate_response_code(200))

    def test_response_code_bad(self):
        f = open("blns.payloads", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Valid.validate_response_code(line))