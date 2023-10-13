from modules.port_scanner import PortScannerFactory

def test_port_scanning():
    target = "example.com"
    ports = range(80, 101) 

    port_scanner = PortScannerFactory.generate_port_scanner("TCP")

    open_ports, closed_ports = port_scanner.scan_target(target, ports)

    print("Open ports:", open_ports)
    print("Closed ports:", closed_ports)

if __name__ == "__main__":
    test_port_scanning()
