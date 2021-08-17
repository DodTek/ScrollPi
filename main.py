import scrollphathd as sphd
import time
import random
import json

with open('jojo.json') as jojo:
  data = json.load(jojo)

option_number = random.randint(0, data["size"])
data_option = "option" + str(option_number)
print(data["entries"][data_option])

sphd.write_string(data["entries"][data_option] + " ")

while True:
    sphd.set_brightness(0.25)
    sphd.rotate(180)
    sphd.show()
    sphd.scroll(1)
    time.sleep(0.05)
