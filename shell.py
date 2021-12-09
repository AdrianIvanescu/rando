from cmd import Cmd
from magic_number import magic_number_auto
from magic_number import magic_number_user
 
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
        magic_number_auto.guess_number_auto()

    def help_guess_auto(self):
        print('generate random number and let the "machine" to guess it')

    def do_guess_user(self, inp):
        magic_number_user.guess_number_user()

    def help_guess_user(self):
        print('generate random number and let the "user" to guess it')    

    def emptyline(self):
         pass

    do_EOF = do_exit
    help_EOF = help_exit
 
if __name__ == '__main__':
    MyPrompt().cmdloop()