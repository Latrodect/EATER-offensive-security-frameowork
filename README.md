
# Eater - Network Utility Tool

Eater is a versatile network utility tool designed to facilitate network diagnostics and information gathering. It offers modules for banner grabbing, port scanning, and wireless network penetration testing, each accessible via a command-line interface (CLI). The tool is organized using the abstract factory design pattern, allowing the creation of specific instances based on the selected module type.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Creating New Modules](#creating-new-modules)
- [Tests](#tests)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

Eater is a network utility tool that allows users to perform various network-related tasks, including banner grabbing, port scanning, and wireless network penetration testing. These operations are available as separate modules accessible through the command-line interface (CLI). Eater is organized using the abstract factory design pattern, making it easy to add new modules for different network-related tasks.

## Features

- **Modular Design:** Eater is designed with a modular structure, allowing you to add new network-related modules with ease.
- **Abstract Factory Pattern:** The tool uses the abstract factory pattern to create specific instances based on the selected module type.
- **Banner Grabbing:** Use banner grabber modules to retrieve service banners from remote services running on target hosts using various network protocols, such as TCP, UDP, ICMP (Ping), and SCTP.
- **Port Scanning:** Perform port scanning on target hosts using the Port Scanner module, supporting different scan types, including TCP, UDP, ICMP, and SCTP.
- **Wireless Network Penetration Testing:** Eater supports a Wireless Eater module for wireless network penetration testing, which can crack WEP, WPA, and WPA2 networks.

## Project Structure

The project is structured as follows:

- `modules/`: Contains the banner grabber, port scanner, and wireless eater modules.
- `utils/`: Contains the module generator, which follows the abstract factory pattern.
- `eater.py`: The main script that creates a CLI for accessing the modules.

## Getting Started

Follow these instructions to set up and start using Eater.

### Prerequisites

Before using Eater, ensure you have the following prerequisites:

- Python 3.x

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/yourusername/eater.git
   ```
