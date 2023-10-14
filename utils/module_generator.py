"""
Module Factory

This module provides a factory for generating specific modules in the Eater Network Utility Tool. It allows the creation of modules based on the provided module_type.

Classes:
- ModuleFactory: Factory class for generating modules.
- ModuleBase: Abstract base class for modules.
- ProtosearchModule: A module for performing port scanning.
- BannergrabberModule: A module for grabbing banners from services.
- WirelessEaterModule: A module for wireless network password cracking.

Usage:
1. Use the 'generate_module' method in the 'ModuleFactory' to create a module instance based on the provided module_type.
2. 'ModuleBase' is an abstract class that defines the structure for all modules.
3. Implement specific module behavior by extending 'ModuleBase' and overriding the 'run' method.

Modules available:
- 'protosearch': Port scanning module.
- 'bannergrabber': Banner grabbing module.
- 'wireless_eater': Wireless network password cracking module.

The 'ModuleFactory' creates instances of these modules based on the module_type provided. 
"""

from abc import ABC, abstractmethod
from modules.port_scanner import PortScannerFactory
from modules.banner_grabber import BannerGrabberFactory
from modules.wireless_eater import WirelessEaterFactory

class ModuleBase(ABC):
    """
    Abstract base class for modules.
    """
    
    def __init__(self):
        """
        Initializes the module.
        """
        self.run()

    @abstractmethod
    def run(self):
        """
        Abstract method that defines the behavior of the module. Subclasses must implement this method.
        """
        pass

class ProtosearchModule(ModuleBase):
    """
    Port scanning module.
    """
    
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
    """
    Banner grabbing module.
    """
    
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

class WirelessEaterModule(ModuleBase):
    """
    Wireless network password cracking module.
    """
    
    def run(self):
        """
        Runs the 'wireless_eater' module.

        This method prompts the user for dictionary and network type information and initiates a password cracking operation.
        """
        print("You've selected the 'wireless_eater' module.")
        dictionary_path = input("Enter the dictionary path: ")
        network_type = input("Enter the network type (WEP/WPA/WPA2, default is WEP): ").strip().upper() or "WEP"

        wireless_eater = WirelessEaterFactory.generate_wireless_factory(network_type)
        wireless_eater.crack(dictionary_path)
        print(f"Performing password cracking with dictionary: {dictionary_path}, network type: {network_type}...")

class ModuleFactory:
    """
    Factory class for generating modules.
    """
    module_classes = {
        "protosearch": ProtosearchModule,
        "bannergrabber": BannergrabberModule,
        "wireless-eater": WirelessEaterModule,
    }

    @staticmethod
    def generate_module(module_type):
        """
        Factory method to generate a module instance based on the provided module_type.

        Args:
            module_type (str): The type of module to create ("protosearch" or "bannergrabber" or "wireless-eater").

        Returns:
            ModuleBase: An instance of the specified module.
        """
        module_class = ModuleFactory.module_classes.get(module_type)
        if module_class:
            return module_class()
        else:
            print(f"Module type '{module_type}' is not recognized.")
            return None