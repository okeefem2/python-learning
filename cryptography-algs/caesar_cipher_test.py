import unittest
import caesar_cipher


class GenerateKeyTest(unittest.TestCase):
    def test_should_create_key_properly(self):
        result = caesar_cipher.generate_key(3)
        self.assertEqual(''.join(result.values()), "DEFGHIJKLMNOPQRSTUVWXYZABC")

        result = caesar_cipher.generate_key(9)
        self.assertEqual(''.join(result.values()), "JKLMNOPQRSTUVWXYZABCDEFGHI")


class EncryptTest(unittest.TestCase):
    def test_should_create_cipher_properly(self):
        key = caesar_cipher.generate_key(3)
        result = caesar_cipher.encrypt(key, "YOU ARE AWESOME")
        self.assertEqual(result, "BRX DUH DZHVRPH")


class DecryptTest(unittest.TestCase):
    def test_should_create_message_properly(self):
        key = caesar_cipher.generate_key(3)
        result = caesar_cipher.decrypt(key, "BRX DUH DZHVRPH")
        self.assertEqual(result, "YOU ARE AWESOME")


class CalculateKeyRotation(unittest.TestCase):
    def test_should_calculate_rotation_value(self):
        cnt = 0
        while cnt <= 26:
            key = caesar_cipher.generate_key(cnt)
            result = caesar_cipher.calculate_rotation_value(key)
            self.assertEqual(result, cnt % 26)
            cnt += 1


class DecryptReverseKeyTest(unittest.TestCase):
    def test_should_create_message_properly(self):
        key = caesar_cipher.generate_key(3)
        result = caesar_cipher.decrypt_reverse_key(key, "BRX DUH DZHVRPH")
        self.assertEqual(result, "YOU ARE AWESOME")


class DecryptReverseKeyRotationTest(unittest.TestCase):
    def test_should_create_message_properly(self):
        key = caesar_cipher.generate_key(3)
        result = caesar_cipher.decrypt_reverse_key_rotation(key, "BRX DUH DZHVRPH")
        self.assertEqual(result, "YOU ARE AWESOME")


if __name__ == '__main__':
    unittest.main()
