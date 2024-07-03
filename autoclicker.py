import keyboard
import mouse
import time
import threading

clicking = False

def autoclick():
    while clicking:
        print("click")
        mouse.click(button='left')
        time.sleep(0.1)

def toggle_clicking():
    global clicking
    clicking = not clicking
    if clicking:
        thread = threading.Thread(target=autoclick)
        thread.start()
    else:
        print("fin")

keyboard.add_hotkey('f6', toggle_clicking)

print("Presiona F6 para iniciar/detener el click.")
keyboard.wait('esc')