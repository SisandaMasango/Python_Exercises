import random
import string
import time

def random_url():
    domain = ''.join(random.choices(string.ascii_lowercase, k=8)) + ".com"
    path = '/' + ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return "http://" + domain + path

urls = [random_url() for _ in range(500_000)]

for i in urls:

    print(i)