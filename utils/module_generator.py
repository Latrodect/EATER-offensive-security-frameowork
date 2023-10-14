from abc import ABC, abstractmethod
from modules.port_scanner import PortScannerFactory
from modules.banner_grabber import BannerGrabberFactory

class ModuleFactory:
    @staticmethod
    def generate_module(module_type):
        """
        Factory method to generate a module instance based on the provided module_type.

        Args:
            module_type (str): The type of module to create ("protosearch" or "bannergrabber").

        Returns:
            ModuleBase: An instance of the specified module.
        """
        modules = {
            "protosearch": ProtosearchModule(),
            "bannergrabber": BannergrabberModule()
        }

        if module_type in modules:
            return modules[module_type]
        else:
            print(f"Module type '{module_type}' is not recognized.")
            return None

class ModuleBase(ABC):
    def __init__(self):
        self.run()

    @abstractmethod
    def run(self):
        """
        Abstract method that defines the behavior of the module. Subclasses must implement this method.
        """
        pass

class ProtosearchModule(ModuleBase):
    def run(self):
        """
        Runs the 'protosearch' module.

        This method prompts the user for target information and initiates a port scan.
        """
        print("You've selected the 'protosearch' module.")
        target = input("Enter the target (hostname or IP address): ")
        port_range = input("Enter the port range (e.g., 80-100): ").strip()
        scan_type = input("Enter the scan type (TCP/UDP/ICMP/SCTP, default is TCP): ").strip().upper() or "TCP"

        port_scanner = PortScannerFactory.generate_port_scanner(scan_type)
        port_scanner.scan_target(target, port_range)
        print(f"Performing port scanning on target: {target} with port range: {port_range} using {scan_type}...")

class BannergrabberModule(ModuleBase):
    def run(self):
        """
        Runs the 'bannergrabber' module.

        This method prompts the user for target information and initiates a banner grabbing operation.
        """
        print("You've selected the 'bannergrabber' module.")
        target = input("Enter the target (hostname or IP address): ")
        port_range = input("Enter the port range (e.g., 80-100): ").strip()
        scan_type = input("Enter the scan type (TCP/UDP/ICMP/SCTP, default is TCP): ").strip().upper() or "TCP"

        banner_grabber = BannerGrabberFactory.generate_banner_grabber(scan_type)
        banner_grabber.grab_banner(target, port_range)
        print(f"Performing banner grabber on target: {target} with port range: {port_range} using {scan_type}...")
