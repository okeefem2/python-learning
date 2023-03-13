import unittest
import substitution_cipher


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class EncryptTest(unittest.TestCase):
    def test_should_not_encrypt_same_twice(self):
        key = substitution_cipher.generate_key()
        result1 = substitution_cipher.encrypt(key, "YOU ARE AWESOME")
        key = substitution_cipher.generate_key()
        result2 = substitution_cipher.encrypt(key, "YOU ARE AWESOME")
        self.assertNotEquals(result1, result2)


class DecryptTest(unittest.TestCase):
    def test_should_create_message_properly(self):
        key = substitution_cipher.generate_key()
        cipher = substitution_cipher.encrypt(key, "YOU ARE AWESOME")
        result = substitution_cipher.decrypt(key, cipher)
        self.assertEqual(result, "YOU ARE AWESOME")



if __name__ == '__main__':
    unittest.main()
