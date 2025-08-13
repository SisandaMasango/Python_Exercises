import time
import random
import string

# def random_url():
#     domain = "".join(random.choices(string.ascii_lowercase, k=8)) + ".com"
#     path = '/' + ''.join(random.choices(string.ascii_letters + string.digits, k=10))
#     return "http://" + domain + path

# num_urls = 100000
# print()
# start_gen = time.perf_counter()
# urls = [random_url() for _ in range(num_urls)]
# end_gen = time.perf_counter()
# print()

urls = []
with open("/Users/sisarmasango/Desktop/Python_Exercises/Python_for_defense/random_urls.txt", "r") as file:
    for line in file:
        clean_url = line.strip()
        urls.append(clean_url)
        
print(len(urls))

start_list = time.perf_counter()
url_list = []
for url in urls:
    if url not in url_list:
        url_list.append(url)
end_list = time.perf_counter()
seconds_for_list = end_list - start_list
print(f"Time elapsed for List: {seconds_for_list:.6f} seconds")

start_set = time.perf_counter()
url_set = set(urls)
end_set = time.perf_counter()
seconds_for_set = end_set - start_set
print(f"Time Elapsed for the Set: {seconds_for_set:.6f} seconds")

minimum_time = min(seconds_for_list, seconds_for_set)
maximum_time = max(seconds_for_list, seconds_for_set)

print(f"Minimum time between the set and list: {minimum_time}")
print(f"Maximum time between the set and list: {maximum_time}")

if seconds_for_list == minimum_time:
    print(f"List took the least time to run with {seconds_for_list:.6f} seconds.")
else:
    print(f"Set took the least time to run with {seconds_for_set:.6f} seconds.")
