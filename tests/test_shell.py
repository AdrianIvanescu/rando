import unittest

from utilsfolder.magic_shell import MyPrompt

message_auto = 'generate random number and let the "machine" to guess it'
message_user = 'generate random number and let the "user" to guess it'


class TestShell(unittest.TestCase):
    def test_help_guess_auto(self):
        result = MyPrompt().help_guess_auto()
        self.assertEqual(result, message_auto)

    def test_help_guess_user(self):
        result = MyPrompt().help_guess_user()
        self.assertEqual(result, message_user)


if __name__ == '__main__':
    unittest.main()
