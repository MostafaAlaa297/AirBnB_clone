#!/usr/bin/python3
"""
===========
Console module for the Airbnb project
===========
"""

import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = '(hbnb) '

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def do_create(self, arg):
        """Creates a new instance of the specified class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objs = models.storage.all()
            print(all_objs.get(key, "** no instance found **"))

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objs = models.storage.all()
            obj_to_del = all_objs.get(key)
            if obj_to_del:
                del all_objs[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        args = arg.split()
        all_objs = models.storage.all()
        if not args:
            print([str(obj) for obj in all_objs.values()])
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in all_objs.items()
                   if args[0] == key.split('.')[0]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objs = models.storage.all()
            obj_to_update = all_objs.get(key)
            if obj_to_update:
                setattr(obj_to_update, args[2], eval(args[3]))
                models.storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
