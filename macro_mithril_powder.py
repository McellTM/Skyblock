import keyboard
import pyautogui
import time
import random
import threading

w, h = pyautogui.size()
running = False

def wiggle():
    pyautogui.moveRel(0, 10, duration=0.2)
    pyautogui.moveRel(0, -10, duration=0.2)
    time.sleep(0.3)

def macro_loop():
    global running
    try:
        while running:
            # fresh random coords each cycle
            q1 = (random.randint(0, w // 2),           random.randint(0, h // 2))
            q2 = (random.randint(w // 2 + 1, w),       random.randint(0, h // 2))
            q3 = (random.randint(0, w // 2),           random.randint(h // 2 + 1, h))
            q4 = (random.randint(w // 2 + 1, w),       random.randint(h // 2 + 1, h))

            # right-click center
            pyautogui.mouseUp()
            pyautogui.moveTo(w // 2, h // 2, duration=0.2)
            pyautogui.rightClick()

            # hold + tour quadrants
            pyautogui.mouseDown()
            for pt in (q1, q2, q3, q4):
                if not running: break
                wiggle()
                pyautogui.moveTo(pt[0], pt[1], duration=0.2)
                wiggle()
    finally:
        # always release if we stop mid-loop
        pyautogui.mouseUp()

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
