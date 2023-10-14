"""
Banner Grabber

This module provides classes for grabbing banners from remote services running on specified target hosts using various network protocols, including TCP, UDP, ICMP (Ping), and SCTP. The BannerGrabberFactory allows the creation of specific banner grabber instances based on the selected banner type. Each banner grabber class is responsible for grabbing banners from services and provides methods for this purpose.

Classes:
- BannerGrabberFactory: Factory for creating banner grabber instances based on the banner type.
- BannerGrabberBase: Abstract base class for banner grabbers.
- TCPBannerGrabber: Banner grabber for TCP ports.
- UDPBannerGrabber: Banner grabber for UDP ports.
- ICMPBannerGrabber: Banner grabber for ICMP Echo Request (Ping).
- SCTPBannerGrabber: Banner grabber for SCTP ports.

Usage:
1. Choose the type of banner grabber (e.g., "tcp", "udp", "icmp", "sctp").
2. Specify the target hostname or IP address and the port from which to grab the banner.
3. Execute the banner grabber to attempt to retrieve the service banner from the specified target.

This module is intended for network diagnostics and information gathering. Unauthorized use may violate laws and regulations.
"""

import socket
from abc import ABC, abstractmethod
        
class BannerGrabberBase(ABC):
    """"
    Abstract base class for banner grabbers.
    """
    @abstractmethod
    def grab_banner(self, target, port):
        """
        Attempt to grab the banner from a remote service running on a specified target and port.

        Args:
            target (str): The target hostname or IP address.
            port (int): The target port on which to grab the banner.

        Prints the banner information to the console if successful. Handles socket-related exceptions and
        general exceptions, providing error messages in case of issues.
        """
        pass

class TCPBannerGrabber(BannerGrabberBase):
    """
    Banner grabber for TCP ports.
    """
    
    def grab_banner(self, target, port):
        """
        Attempt to grab the banner from a remote service running on a specified target and port.

        Args:
            target (str): The target hostname or IP address.
            port (int): The target port on which to grab the banner.

        Prints the banner information to the console if successful. Handles socket-related exceptions and
        general exceptions, providing error messages in case of issues.
        """
        try:
            tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_sock.settimeout(2)
            tcp_sock.connect((target,port))

            banner = socket.recv(1024).decode('utf-8')
            print(f"Banner from {target}:{port} for TCP -> {banner}")
        
        except (socket.timeout, ConnectionRefusedError):
            print(f"Unable to grab banner from {target}:{port}")
        except Exception as e:
            print(f"An error occured: {e}")
        finally:
            tcp_sock.close()

class UDPBannerGrabber(BannerGrabberBase):
    """
    Banner grabber for UDP ports.
    """

    def grab_banner(self, target, port):
        """
        Attempt to grab the banner from a remote service running on a specified target and port.

        Args:
            target (str): The target hostname or IP address.
            port (int): The target port on which to grab the banner.

        Prints the banner information to the console if successful. Handles socket-related exceptions and
        general exceptions, providing error messages in case of issues.
        """
        try:
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_socket.settimeout(2)
            udp_socket.connect((target, port))

            banner = socket.recv(1024).decode('utf-8')
            print(f"Banner from {target}:{port} for UDP -> {banner}")
        
        except (socket.timeout, ConnectionRefusedError):
            print(f"Unable to connect socket {target}:{port}")
        except Exception as e:
            print(f"An error occured: {e}")
        finally:
            udp_socket.close()

class ICMPBannerGrabber(BannerGrabberBase):
    """
    Banner grabber for ICMP Echo Request (Ping).
    """
    def grab_banner(self, target, port):
        """
        Attempt to grab the banner from a remote service running on a specified target and port.

        Args:
            target (str): The target hostname or IP address.
            port (int): The target port on which to grab the banner.

        Prints the banner information to the console if successful. Handles socket-related exceptions and
        general exceptions, providing error messages in case of issues.
        """
        try:
            icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            icmp_socket.settimeout(2)
            icmp_socket.connect((target, port))

            banner = icmp_socket.recv(1024).decode('utf-8')
            print(f"Banner from {target}:{port} for ICMP -> {banner}")
        except (socket.timeout, ConnectionRefusedError):
            print(f"Unable to connect {target}:{port}")
        except Exception as e:
            print(f"An error occured {target}:{port}")
        finally:
            icmp_socket.close()

class SCTPBannerGrabber(BannerGrabberBase):
    """
    Banner grabber for SCTP ports.
    """
    def grab_banner(self, target, port):
        """
        Attempt to grab the banner from a remote service running on a specified target and port.

        Args:
            target (str): The target hostname or IP address.
            port (int): The target port on which to grab the banner.

        Prints the banner information to the console if successful. Handles socket-related exceptions and
        general exceptions, providing error messages in case of issues.
        """
        try:
            sctp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_SCTP)
            sctp_socket.settimeout(1024)
            sctp_socket.connect((target,socket))

            banner = sctp_socket.recv(1024).decode('utf-8')
            print(f"Banner from {target}:{port} -> {banner}")
        except (socket.timeout, ConnectionRefusedError):
            print(f"Unable to connect  {target}:{port}")
        except Exception as e:
            print(f"An error occured {target}:{port}")
        finally:
            sctp_socket.close()
            
class BannerGrabberFactory:
    """ Banner Grabber Factory Class"""
    banner_classes = {
            "tcp": TCPBannerGrabber(),
            "udp": UDPBannerGrabber(),
            "icmp": ICMPBannerGrabber(),
            "sctp": SCTPBannerGrabber()
        }

    @staticmethod
    def generate_banner_grabber(banner_type):
        """
        Factory method to generate an instance of a banner grabber.

        Args:
            banner_type (str): Type of the banner grabber (e.g., "tcp", "udp", "icmp", "sctp").

        Returns:
            BannerGrabberBase: An instance of the specified banner grabber class.
        """
        banner_type = banner_type.lower()
        banner_class = BannerGrabberFactory.banner_classes.get(banner_type)
        if banner_class:
            scanner_instance = banner_class()
            return scanner_instance
        else:
            raise ValueError(f"Cracker type '{banner_type}' is not recognized.")
            
