# ScrollPi
Scroll pHAT HD - https://shop.pimoroni.com/products/scroll-phat-hd

Instructions:
1. Install the Scroll pHAT on a raspberry pi 
2. Add the repository to the device.
3. Create the JSON file you wish to use
4. Change the file opened by the main.py script (line 6) - `open('jojo.json')`
5. Run the script using python main.py or python3.py
6. Prints texts from a json to the pimroni scroll phat

Running On Boot
If you want to run this script on boot you need to use crontab -e and put the command at the end of the file
You need to use an absolute path for the main.py file
You also need to use the exact path in the script to reference the file you want open
