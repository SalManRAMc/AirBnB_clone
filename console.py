#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Holberton BNB THE CONSOLE App"""

    prompt = "$ "

    __classes={
        "Sss"
    }

    def emptyline(self):
        """Prints an emptyline"""
        pass

    def default(self, arg):
        """if an argument is passed to console that is unknown, this function is called"""
        print(f"{arg} not found")
    
    def do_name(self, arg):
        """split string of arguments and finds words that are commands"""
        if arg:
            print(arg.split()[0] in HBNBCommand.__classes)
        
    def do_exit(self, arg):
        """Exits the terminal"""
        return True
    
    def do_EOF(self, arg):
        """the end of file"""
        print("")
        return True






if __name__ == "__main__":
    HBNBCommand().cmdloop()
