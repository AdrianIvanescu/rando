from cmd import Cmd
import unittest
from utilsfolder.shell import MyPrompt

class TestShell(unittest.TestCase):
    def test_help_guess_auto(self):
        result = MyPrompt().help_guess_auto()
        self.assertEqual(result,'generate random number and let the "machine" to guess it')

    def test_help_guess_user(self):
        result = MyPrompt().help_guess_user()
        self.assertEqual(result,'generate random number and let the "user" to guess it')

if __name__ == '__main__':
    unittest.main()
