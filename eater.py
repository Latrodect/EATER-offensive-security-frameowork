"""
Eater CLI

A command-line interface (CLI) for the Eater Network Utility Tool. The Eater CLI provides an interactive shell for using various network utility modules. Users can activate specific modules, show available modules, and access module help using the provided commands.

Commands:
- 'use <module_name>': Activate a specific module.
- 'show [modules | help]': Display available modules or get help for a specific module.
- 'quit': Exit the Eater CLI.

Usage:
1. Start the Eater CLI.
2. Use the 'use' command to activate a specific module (e.g., 'use protosearch').
3. Use the 'show' command to list available modules or get help (e.g., 'show modules' or 'show help').
4. Exit the Eater CLI using the 'quit' command.

The Eater CLI is an interactive tool for network utility tasks, providing access to various modules. Unauthorized use may violate laws and regulations.
"""

import cmd
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from pyfiglet import figlet_format
from utils.module_generator import ModuleFactory
from termcolor import colored

class EaterCLI(cmd.Cmd):
    ascii_art = figlet_format('EATER', font="isometric1")
    intro = cprint(ascii_art, 'green', attrs=['bold'])
    desc_head = cprint('Introduction:', 'green', attrs=['bold'])
    desc_cont = cprint('Welcome to Eater - The Network Utility Tool\nType `help` to see available commands.' , 'white', attrs=['bold'])
    prompt="Command: "
    activated_module = None

    def do_use(self, module_name):
        """Use a specific module.

        Args:
            module_name (str): The name of the module to use.
        """
        module_name = module_name.lower()
        self.activated_module = ModuleFactory.generate_module(module_name)
        if self.activated_module:
            text = colored(f"{module_name}", "red")
            print(f"Module activated: {module_name}")
            self.prompt = f"({text}) Command: "
        else:
            print(f"Module '{module_name}' is not recognized.")


    def do_exec(self, arg):
        """Execute the currently activated module.

        Args:
            arg (str): Any arguments to pass to the activated module.
        """
        if self.activated_module:
            self.activated_module.run()
        else:
            print("No module activated. Use 'use <module_name>' to activate a module.")

    def do_cls(self, arg):
        """Clear activated module.

        Args:
            arg (str): Any arguments to pass to the activated module.
        """
        ascii_art = figlet_format('EATER', font="isometric1")
        intro = cprint(ascii_art, 'green', attrs=['bold'])
        desc_head = cprint('Introduction:', 'green', attrs=['bold'])
        desc_cont = cprint('Welcome to Eater - The Network Utility Tool\nType `help` to see available commands.' , 'white', attrs=['bold'])
        self.activated_module = None
        self.prompt = f"\nCommand: "

    def do_act(self, arg):
        """Execute the currently activated module.

        Args:
            arg (str): Any arguments to pass to the activated module.
        """
        print(f"Activated Module Is: {self.activated_module.__class__.__name__}")

    def do_show(self, arg):
        """Show available modules or help for a specific module.

        Args:
            arg (str): The argument to show specific module's help.
        """
        print("\nYou can use modules with 'use' command.")
        if arg == "modules":
            print("Available modules:")
            print("1. protosearch - Port scanning module\n")
            print("2. bannergrabber - Banner Grabber module\n")
            print("3. wireless-eater - Wireless Eater module\n")
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
