#!/usr/bin/python3
"""Console for AirBnB project"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create new instance, save to JSON file, print id"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new_obj = classes[arg]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """Show string representation of instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if obj_key in objects:
                print(objects[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete instance, save to JSON file"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if obj_key in objects:
                del objects[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print string representations of instances"""
        objects = storage.all()
        obj_list = []
        if len(arg) == 0:
            for value in objects.values():
                obj_list.append(str(value))
        else:
            if arg in classes:
                for key in objects:
                    if key.split('.')[0] == arg:
                        obj_list.append(str(objects[key]))
            else:
                print("** class doesn't exist **")
        print(obj_list)

    def do_update(self, arg):
        """Update instance, save to JSON file"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if obj_key in objects:
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(objects[obj_key], args[2], args[3])
                    storage.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
