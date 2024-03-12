#!/usr/bin/python3
import cmd
import re
import shlex
from models.base_model import BaseModel
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User
import models

classes = {
        "BaseModel": BaseModel,
        "State": State,
        "Review": Review,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "User": User
    }


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for HBNB"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates an instance of whatever class
        user inputs if it's valid"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show user what data of a class exists"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Destroy all data about a class"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """Do everything """
        args = arg.split()
        if args and args[0] not in classes:
            print("** class doesn't exist **")
            return
        print([str(v) for k, v in models.storage.all().items()
               if not args or v.__class__.__name__ == args[0]])

    def do_update(self, arg):
        """Update the user"""
        if not arg:
            print("** class name missing **")
            return
        args = parse_argument(arg)
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(models.storage.all()[key], args[2], args[3])
        models.storage.save()

    def do_quit(self, arg):
        """Quit"""
        return True

    def do_EOF(self, arg):
        """Similiar to quit"""
        print("")
        return True

    def emptyline(self):
        """emptyline.."""
        pass

    def default(self, arg):
        """If all else fails, refer to this method"""
        args = arg.split(".")
        if len(args) < 2:
            print("** command not found **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if args[1] == "all()":
            self.do_all(args[0])
        elif args[1] == "create()":
            self.do_create(arg[0])
        elif args[1] == "count()":
            print(len([v for k, v in models.storage.all().items()
                       if v.__class__.__name__ == args[0]]))
        elif args[1].startswith("show("):
            self.do_show(args[0] + " " + args[1][6:-2])
        elif args[1].startswith("destroy("):
            self.do_destroy(args[0] + " " + args[1][9:-2])
        elif args[1].startswith("update("):
            self.do_update(args[0] + " " + args[1][7:-1])
        else:
            print("** command not found **")

def parse_argument(args):
    """Parses an argument"""
    data = None
    match = re.search(r'{(.*?)}', args)  # Match the shortest sequence enclosed in {}
    if match:
        try:
            data = json.loads(match.group(1))  # Load the matched content as JSON
            args = re.sub(r'{(.*?)}', '', args)  # Remove the JSON content from args
        except json.JSONDecodeError:
            print("Invalid JSON format")

    args = shlex.split(args)
    if data is not None:
        args.append(data)
    else:
        # Convert numeric strings to integers if possible
        args = [int(arg) if arg.isdigit() else arg for arg in args]
    return args


if __name__ == '__main__':
    HBNBCommand().cmdloop()