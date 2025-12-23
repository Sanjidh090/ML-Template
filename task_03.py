import time

list = [i for i in range(-50000000, 5000000)]
start = time.time()
list.insert(0, -5)
end = time.time()
time_list = end - start
print(f"Timw taken {time_list:.6f} seconds for insert")

start = time.time()
list.append(-5)
end = time.time()
time_append = end - start
print(f"Time taken {time_append:.6f} seconds for append")