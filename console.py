#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Holberton BNB THE CONSOLE App"""

    prompt = "(hbnb)"

    __classes={
        "BaseModel": BaseModel,
    }

    def do_exit(self, arg):
        """Exits the terminal"""
        return True
    
    def do_EOF(self, arg):
        """the end of file"""
        print("")
        return True

    def emptyline(self):
        """Prints an emptyline"""
        pass

    def d


    def default(self, arg):
        """if an argument is passed to console that is unknown, this function is called"""
        print(f"{arg} not found")






if __name__ == "__main__":
    HBNBCommand().cmdloop()
