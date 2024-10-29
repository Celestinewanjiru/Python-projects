import time

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(0, my_time)):
  print(x)
  time.sleep(1)

print("TIME'S UP!")