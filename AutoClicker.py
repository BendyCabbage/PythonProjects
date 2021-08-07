from pynput import keyboard
from pynput.mouse import Button, Controller
import time
mouse = Controller()
activate = False

def on_press(key):
    if str(key) == "Key.f3":
        clickCheck()

def clickCheck():
    if activate == False:
        activate = True

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

if activate == True:
    while True:
        mouse.click(Button.left)
        #print("Clicking")
        time.sleep(1/60)
