#!/usr/bin/python3
"""
===========
Console module for the Airbnb project
===========
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl-D)."""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
