coords = (10.0, 20.5)
ip_port = ("10.0.0.5", 22)

host, port = ip_port
a, *middle, z = range(10)

# print(a)
# print(middle)
# print(z)

from collections import namedtuple
Result = namedtuple("Result", "ip port status")
r = Result("10.0.0.5", 80, "open")

services = {"ssh": 22, "http": 80, "https": 443}
services["dns"] = 53
port = services.get("ftp", 21)   # default value
print(services)
print(port)

for key, value in services.items():
    print(key, value)