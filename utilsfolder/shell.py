'''
creates a magic_number shell
'''
from cmd import Cmd

from db_layer.create_table import MagicTable
from magic_number.magic_number_auto import MagicNumberAuto
from magic_number.magic_number_user import MagicNumberUser
from utilsfolder import version


toolversion = f"v{version.__version__}"


class MyPrompt(Cmd):
    prompt = 'magic> '
    intro = f" {toolversion} Type (?) or (help) - to list commands"

    def do_exit(self, inp):
        print("bye")
        return True

    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
        print(self.intro)

    def do_guess_auto(self, inp):
        number = MagicNumberAuto(1, 100)
        number.guess_number_auto()

    def help_guess_auto(self) -> str:
        message = ('generate random number and let the "machine" to guess it')
        print(message)
        return message

    def do_guess_user(self, inp):
        number = MagicNumberUser(1, 100)
        number.guess_number_user()

    def help_guess_user(self) -> str:
        message = ('generate random number and let the "user" to guess it')
        print(message)
        return message

    def do_create_table(self, inp):
        table = MagicTable('magic_number', 'run_times')
        table.open_db_connection()
        table.create_table()
        table.commit_db_change()
        table.close_db_connection()

    def help_create_table(self):
        print('create a sqlite3 table: magic_db.run_times')

    def do_drop_table(self, inp):
        table = MagicTable('magic_number', 'run_times')
        table.open_db_connection()
        table.drop_table()
        table.close_db_connection()

    def help_drop_table(self):
        print('drop a sqlite3 table: magic_db.run_times')

    def emptyline(self):
        pass

    do_EOF = do_exit
    help_EOF = help_exit


if __name__ == '__main__':
    MyPrompt().cmdloop()
