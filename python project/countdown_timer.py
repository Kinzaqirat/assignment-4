import time

my_time= int(input("Enter time in sec: "))
for i in range(my_time , 0 , -1):# for reverse time
  seconds=i % 60
  minutes=int(i/60)%60
  hours= int(i / 3600)
  print(f"{hours:02}:{minutes:02}:{seconds:02}")
  time.sleep(1)  # pause for 1 sec

print("TIMES UP !")
