import keyboard
import pyautogui
import time
import threading

w, h = pyautogui.size()
running = False


def macro_loop():
    global running
    try:
        while running:
            pyautogui.keyDown("w")
            time.sleep(110)
            pyautogui.keyUp("w")
            pyautogui.keyDown("s")
            time.sleep(110)
            pyautogui.keyUp("s")
    finally:
        # always release if we stop mid-loop
        pyautogui.keyUp("w")
        pyautogui.keyUp("s")

def start_macro():
    global running
    if running:
        return
    running = True
    threading.Thread(target=macro_loop, daemon=True).start()
    print("Macro started (F9 to stop, Esc to exit).")

def stop_macro():
    global running
    running = False
    print("Stopping macro…")

# Hotkeys:
keyboard.add_hotkey('f8', start_macro)  # start
keyboard.add_hotkey('f9', stop_macro)   # stop
print("F8=start, F9=stop, Esc=exit.")
keyboard.wait('esc')
