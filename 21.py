#######
#task1
#####################

import json
from concurrent.futures import ThreadPoolExecutor

json_data = [
    {"product": "Laptop", "price": 1200, "stock": 20},
    {"product": "Smartphone", "price": 800, "stock": 50},
    {"product": "Tablet", "price": 300, "stock": 100}
]

file_names = ["product1.json", "product2.json", "product3.json"]

for i, data in enumerate(json_data):
    with open(file_names[i], "w") as file:
        json.dump(data, file)

def parse_json(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
        print(f"Data from {file_name}: {data}")

with ThreadPoolExecutor() as executor:
    executor.map(parse_json, file_names)

#######
#task2
#####################

import queue
from concurrent.futures import ThreadPoolExecutor
import threading
import time

def process_queue(q):
    while not q.empty():
        num = q.get()
        thread_name = threading.current_thread().name
        even = "even" if num % 2 == 0 else "odd"
        print(f"Thread {thread_name}: Retrieved {num} ({even})")
        q.task_done()

q = queue.Queue()

with ThreadPoolExecutor(max_workers=3) as executor:
    for _ in range(3):
        executor.submit(process_queue, q)

time.sleep(1)
numbers = [12, 9, 4, 7, 6, 1, 14]
for num in numbers:
    q.put(num)

q.join()

print("Sorted numbers:", sorted(numbers))
print("All tasks done.")
