import cmd
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from pyfiglet import figlet_format
from modules.port_scanner import PortScannerFactory
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
        if module_name == "protosearch":
            print("You've selected the 'protosearch' module.")
            target = input("Enter the target (hostname or IP address): ")
            port_range = input("Enter the port range (e.g., 80-100): ").strip()
            scan_type = input("Enter the scan type (TCP/UDP/ICMP/SCTP, default is TCP): ").strip().upper() or "TCP"

            port_scanner = PortScannerFactory.generate_port_scanner(scan_type)
            port_scanner.scan_target(target, port_range)
            print(f"Performing port scanning on target: {target} with port range: {port_range} using {scan_type}...")

        else:
            print(f"Module '{module_name}' not found.")

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