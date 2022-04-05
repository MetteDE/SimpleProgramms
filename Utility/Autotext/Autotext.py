import time
import keyboard as k
from pynput.keyboard import Key
from pynput.keyboard import Controller

keyboard = Controller()
text = str(input("Text -> "))
number_of_runs = int(input("Count -> "))
pause = float(input("Delay (seconds) -> "))
exit = str(input("Key to exit -> "))
time.sleep(5)
runs = 0

while runs < number_of_runs:
    if k.is_pressed(exit):
        break
    time.sleep(pause)
    for char in text:
        keyboard.press(char)
        keyboard.release(char)
    runs += 1 
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
print("Done")