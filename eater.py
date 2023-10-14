import cmd
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from pyfiglet import figlet_format
from utils.module_generator import ModuleFactory

class EaterCLI(cmd.Cmd):
    ascii_art = figlet_format('EATER', font="isometric1")
    intro = cprint(ascii_art, 'yellow', attrs=['bold'])
    desc_head = cprint('Introduction:', 'green', attrs=['bold'])
    desc_cont = cprint('Welcome to Eater - The Network Utility Tool\nType `help` to see available commands.' , 'white', attrs=['bold'])
    prompt="Command: "

    def do_use(self, module_name):
        """Use a specific module.

        Args:
            module_name (str): The name of the module to use.
        """
        activate_module = ModuleFactory[module_name]
        print(f"Module activated: {activate_module}")

    def do_show(self, arg):
        """Show available modules or help for a specific module.

        Args:
            arg (str): The argument to show specific module's help.
        """
        print("\nYou can use modules with 'use' command.")
        if arg == "modules":
            print("Available modules:")
            print("1. protosearch - Port scanning module\n")
        elif arg == "help":
            print("To use a module, type 'use <module_name>'.\n")
            print("To see available modules, type 'show modules'.\n")
        else:
            print("Unknown command. Type 'show modules' to see available modules or 'show help' for more information.\n")

    def do_quit(self, arg):
        """Exit the Eater CLI."""
        print("\nExiting Eater CLI.")
        return True

if __name__ == "__main__":
    eater_cli = EaterCLI()
    eater_cli.cmdloop()