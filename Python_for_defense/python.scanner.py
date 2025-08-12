import socket
from ipaddress import ip_network
from concurrent.futures import ThreadPoolExecutor, as_completed

def is_open(ip, port, timeout=0.5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((str(ip), port))
            return True
        except:
            return False

def scan_host(ip, ports):
    open_ports = []
    for port in ports:
        if is_open(ip, port):
            open_ports.append(port)
    return ip, open_ports

def scan_network(network_cidr, ports, max_workers=100):
    net = ip_network(network_cidr)
    results = {}

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(scan_host, ip, ports): ip for ip in net.hosts()}

        for future in as_completed(futures):
            ip, open_ports = future.result()
            if open_ports:
                results[str(ip)] = open_ports

    return results

def main():
    network = input("Enter network to scan (e.g. 192.168.0.0/24): ")
    ports_input = input("Enter ports to scan, separated by commas (e.g. 21,22,80,443): ")

    ports = [int(p.strip()) for p in ports_input.split(",")]

    print(f"Scanning network {network} on ports {ports}...")
    results = scan_network(network, ports)

    if results:
        print("\nScan results:")
        for ip, open_ports in results.items():
            print(f"IP {ip} has open ports: {open_ports}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
