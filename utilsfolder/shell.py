'''
creates a magic_number shell
'''
from cmd import Cmd
from magic_number.magic_number_auto import MagicNumberAuto
from magic_number.magic_number_user import MagicNumberUser
 
# this needs to be taken from somewhere - maybe from github
toolversion = "v0.1.0."

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
        print("Type (?) or (help) - to list commands")
    
    def do_guess_auto(self, inp):
        number = MagicNumberAuto(1,100)
        number.guess_number_auto()

    def help_guess_auto(self) -> str:
        message = ('generate random number and let the "machine" to guess it')
        print(message)
        return message

    def do_guess_user(self, inp):
        number = MagicNumberUser(1,100)
        number.guess_number_user()

    def help_guess_user(self) -> str:
        message =  ('generate random number and let the "user" to guess it')
        print(message)
        return message   

    def emptyline(self):
         pass

    do_EOF = do_exit
    help_EOF = help_exit
 
if __name__ == '__main__':
    MyPrompt().cmdloop()