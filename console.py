#!/usr/bin/env python3
"""program called console.py that contains
the entry point of the command interpreter"""
import cmd

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import models


class HBNBCommand(cmd.Cmd):
    """program called console.py that contains
    the entry point of the command interpreter"""

    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_quit(self, arg):
        """exit thr program"""
        print("bay bay -From Rayane")
        return True

    def do_EOF(self, arg):
        """exit thr program with EOF """
        print()
        return True

    def do_create(self, arg):
        """'create' command creates an instant of BaseModel if you add
class as argument after it"""
        if not arg:
            print("** class name missing **")
        elif arg not in ["BaseModel", "User", "State", "City",
                         "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        else:
            instance = eval(arg)()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """show <class name> <id>: Prints the string representation
of an instance with the given ID of the given class name"""

        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "State", "City",
                             "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")

        else:
            if len(args) < 2:
                print("** instance id missing **")

            else:
                class_name = args[0]
                instance_id = args[1]
                key = class_name + "." + instance_id

                if key not in models.storage.all().keys():
                    print("** no instance found **")

                else:
                    instance = models.storage.all()[key]
                    print(instance)

    def do_destroy(self, arg):
        """destroy <class name> <id>: Deletes the instance
with the given ID of the given class name"""

        models.storage.reload()
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "State", "City",
                             "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")

        else:
            if len(args) < 2:
                print("** instance id missing **")

            else:
                class_name = args[0]
                instance_id = args[1]
                key = class_name + "." + instance_id

                if key not in models.storage.all().keys():
                    print("** no instance found **")

                else:
                    del models.storage.all()[key]
                    models.storage.save()

    def do_all(self, arg):
        """all [class name]: Prints the string representation
of all instances of the given class name"""

        if arg and arg not in ["BaseModel", "User", "State", "City",
                               "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        elif not arg:
            print(f"{str(models.storage.all())}")
        else:
            class_name = arg
            for key in models.storage.all().keys():
                if key.startswith(class_name):
                    print(models.storage.all()[key])

    def do_update(self, arg):
        """Updates an instance based on the class name
and id by adding or updating attribute
Usage: update <class name> <id> <attribute name> "<attribute value>" """
        models.storage.reload()
        args = arg.split()

    def do_update(self, arg):
        """Updates an instance based on the class name
and id by adding or updating attribute
Usage: update <class name> <id> <attribute name> "<attribute value>" """
        args = arg.split()

        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "State", "City",
                             "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")

        else:
            if len(args) == 1:
                print("** instance id missing **")
            elif len(args) >= 2:
                class_name = args[0]
                instance_id = args[1]
                key = class_name + "." + instance_id

                if key not in models.storage.all().keys():
                    print("** no instance found **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(models.storage.all()[key], args[2], args[3])
                    """ models.storage.all()[key].args[2] = args[3] """

    def do_help_quit(self, arg):
        """help to quit """

    def do_help_EOF(self, arg):
        """help to EOF"""

    def do_help_create(self, arg):
        """help to create"""

    def do_help_show(self, arg):
        """help to show"""

    def do_help_destroy(self, arg):
        """help to destroy"""

    def do_help_all(self, arg):
        """help all"""

    def do_help_update(self, args):
        """help to update"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
