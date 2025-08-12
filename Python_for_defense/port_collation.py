
ip_ports = {}

with open("ports.txt", "r") as file:
    for line in file:
        line = line.strip()
        ip, port = line.split(":")
        port = int(port) 

        if ip not in ip_ports:
            ip_ports[ip] = set()
        ip_ports[ip].add(port)

#convert sets to sorted lists
for ip in ip_ports:
    ip_ports[ip] = sorted(ip_ports[ip])
print(ip_ports)

