import socket
from ipaddress import ip_network

def is_open(ip, port, timeout=0.5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((str(ip), port))
            return True
        except:
            return False

def scan_network(network_cidr, ports):
    print(f"Scanning network: {network_cidr}")
    net = ip_network(network_cidr)
    for ip in net.hosts():
        open_ports = []
        for port in ports:
            if is_open(ip, port):
                open_ports.append(port)
        if open_ports:
            print(f"IP {ip} has open ports: {open_ports}")

if __name__ == "__main__":
    # Change this to your local network CIDR
    local_network = "192.168.0.0/24"
    # Common ports to scan; you can add more
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

    scan_network(local_network, common_ports)
