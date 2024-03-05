import time

cur_time = time.time()
local = time.localtime()

print("Seconds since January 1, 1970:", "{:,.4f}".format(cur_time), end=" ")
print("or", "{:.2e}".format(cur_time), "in scientifique notation")
print(time.strftime("%b %d %Y",local))
