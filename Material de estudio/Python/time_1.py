import time
from datetime import datetime

cur_time = time.time()
print(cur_time)

time_struct = time.localtime(cur_time)
print(time_struct)

print(time.asctime(time_struct))
print("Good Night")
