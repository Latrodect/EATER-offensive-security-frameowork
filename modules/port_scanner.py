"""
Port Scanner

This module provides classes for scanning and identifying open and closed network ports on a target host using various network protocols, including TCP, UDP, ICMP (Ping), and SCTP. The PortScannerFactory allows the creation of specific port scanner instances based on the selected scan type. Each port scanner class is responsible for scanning a specific type of port and provides methods for conducting the scans.

Classes:
- PortScannerFactory: Factory for creating port scanner instances based on the scan type.
- PortScannerBase: Abstract base class for port scanners.
- TCPScanner: Port scanner for TCP ports.
- UDPScanner: Port scanner for UDP ports.
- ICMPScanner: Port scanner for ICMP Echo Request (Ping).
- SCTPScanner: Port scanner for SCTP ports.

Usage:
1. Choose the type of port scanner (e.g., "TCP", "UDP", "ICMP", "SCTP").
2. Specify the target hostname or IP address.
3. Provide a range of ports to scan.
4. Execute the port scanner to identify open and closed ports.

This module is intended for network diagnostics and security testing purposes. Unauthorized use may violate laws and regulations.
"""

import socket
from pathos.multiprocessing import ProcessingPool as Pool
from multiprocessing import Manager
from abc import ABC, abstractmethod

class PortScannerBase(ABC):
    """Base class for port scanners."""
    
    @abstractmethod
    def scan_port(self, target_ip, port, result):
        """Scan a specific port on the target IP address and update the result.

        Args:
            target_ip (str): The IP address of the target host.
            port (int): The port to scan.
            result (multiprocessing.Manager().dict()): A shared dictionary to store scan results.
        """
        pass

    def scan_target(self, target, ports):
        """Scan a range of ports on the target host using multiprocessing.

        Args:
            target (str): The hostname or IP address of the target host.
            ports (range): The range of ports to scan.

        Returns:
            dict: A dictionary of open and closed ports.
        """
        open_ports = {}
        closed_ports = {}

        try:
            target_ip = socket.gethostbyname(target)
        except socket.gaierror:
            print(f"Error: Could not resolve {target}")
            return open_ports, closed_ports

        with Pool() as pool:  
            manager = Manager()
            result = manager.dict()

            def scan_single_port(port):
                """Scan a single port on the target IP address.

                Args:
                    port (int): The port to scan.
                """
                status = self.scan_port(target_ip, port, result)
                if status == "open":
                    open_ports[port] = status
                else:
                    closed_ports[port] = status

            pool.map(scan_single_port, ports)

        return open_ports, closed_ports

class TCPScanner(PortScannerBase):
    """Port scanner for TCP ports."""
    def scan_port(self, target_ip, port, result):
        """Scan a specific TCP port on the target IP address and update the result.

        Args:
            target_ip (str): The IP address of the target host.
            port (int): The TCP port to scan.
            result (multiprocessing.Manager().dict()): A shared dictionary to store scan results.
        """
        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_sock.settimeout(1)

        try:
            tcp_sock.connect((target_ip, port))
            result[port] = "open"
        except (socket.timeout, ConnectionRefusedError):
            result[port] = "closed"
        finally:
            tcp_sock.close()

class UDPScanner(PortScannerBase):
    """Port scanner for UDP ports."""
    def scan_port(self, target_ip, port, result):
        """Scan a specific UDP port on the target IP address and update the result.

        Args:
            target_ip (str): The IP address of the target host.
            port (int): The UDP port to scan.
            result (multiprocessing.Manager().dict()): A shared dictionary to store scan results.
        """
        udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_sock.settimeout(1)

        try:
            udp_sock.sendto(b'', (target_ip, port))
            data, addr = udp_sock.recvfrom(1024)
            result[port] = "open"
        except (socket.timeout, ConnectionRefusedError):
            result[port] = "closed"
        finally:
            udp_sock.close()

class ICMPScanner(PortScannerBase):
    """Port scanner for ICMP Echo Request (Ping)."""
    def scan_port(self, target_ip, port, result):
        """Send an ICMP Echo Request packet to the target IP address and update the result.

        Args:
            target_ip (str): The IP address of the target host.
            port (int): The ICMP Echo Request port (usually 0) to scan.
            result (multiprocessing.Manager().dict()): A shared dictionary to store scan results.
        """
        icmp_sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        icmp_sock.settimeout(1)

        try:
            packet = b'\x08\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f'
            icmp_sock.sendto(packet, (target_ip, port))
            recv_data, addr = icmp_sock.recvfrom(1024)
            result[port] = "open"
        except (socket.timeout, ConnectionRefusedError):
            result[port] = "closed"
        finally:
            icmp_sock.close()

class SCTPScanner(PortScannerBase):
    """Port scanner for SCTP ports."""
    def scan_port(self, target_ip, port, result):
        """Scan a specific SCTP port on the target IP address and update the result.

        Args:
            target_ip (str): The IP address of the target host.
            port (int): The SCTP port to scan.
            result (multiprocessing.Manager().dict()): A shared dictionary to store scan results.
        """
        sctp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_SCTP)
        sctp_sock.settimeout(1)

        try:
            sctp_sock.connect((target_ip, port))
            result[port] = "open"
        except (socket.timeout, ConnectionRefusedError):
            result[port] = "closed"
        finally:
            sctp_sock.close()

class PortScannerFactory:
    """Factory for creating port scanner instances based on the scan type."""
    scanner_classes = {
            "TCP": TCPScanner(),
            "UDP": UDPScanner(),
            "ICMP": ICMPScanner(),
            "SCTP": SCTPScanner(),
        }

    @staticmethod
    def generate_port_scanner(port_type):
        """Generate a port scanner instance based on the provided port type.

        Args:
            port_type (str): The type of port scanner to create (e.g., "TCP", "UDP", "ICMP", "SCTP").

        Returns:
            PortScannerBase: An instance of the specified port scanner.
        """
        port_type = port_type.lower()
        scanner_class = PortScannerFactory.scanner_classes.get(port_type)
        if scanner_class:
            scanner_instance = scanner_class()
            return scanner_instance
        else:
            raise ValueError(f"Cracker type '{port_type}' is not recognized.")
