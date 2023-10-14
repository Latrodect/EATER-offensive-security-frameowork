import socket
from abc import ABC, abstractmethod
class BannerGrabberFactory:
    def generate_banner_grabber(banner_type):
        """
        Factory method to generate an instance of a banner grabber.

        Args:
            banner_type (str): Type of the banner grabber (e.g., "tcp", "udp", "icmp", "sctp").

        Returns:
            BannerGrabberBase: An instance of the specified banner grabber class.
        """
        banner_classes = {
            "tcp": TCPBannerGrabber(),
            "udp": UDPBannerGrabber(),
            "icmp": ICMPBannerGrabber(),
            "sctp": SCTPBannerGrabber()
        }
        return banner_classes[banner_type]
        
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



            
        