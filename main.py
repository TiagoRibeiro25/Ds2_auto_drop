import time
import subprocess

ACTION_INTERVAL = 0.01
KEY_PRESS_INTERVAL = 0.08

def press_key(key):
    subprocess.run(['xdotool', 'keydown', key])
    time.sleep(KEY_PRESS_INTERVAL)
    subprocess.run(['xdotool', 'keyup', key])
    time.sleep(ACTION_INTERVAL)

def get_mouse_position():
    result = subprocess.run(['xdotool', 'getmouselocation'], stdout=subprocess.PIPE)
    output = result.stdout.decode()
    position = {}

    for item in output.split(' '):
        values = item.split(":")

        if (values[0] == 'x' or values[0] == 'y'):
            position[values[0]] = int(values[1])

    return position['x'], position['y']

def main():
    print("Starting")

    time.sleep(5)
    initial_cursor_position = get_mouse_position()

    while True:
        print("Dropping")
        press_key('Return')
        press_key('Down')
        press_key('Down')
        press_key('Return')
        for i in range(8):
            press_key('Return')
            press_key('Right')
        press_key('Left')
        press_key('Return')
        for i in range(8):
            press_key('Left')

        current_cursor_position = get_mouse_position()
        if current_cursor_position != initial_cursor_position:
            print("Cursor moved, aborting...")
            exit(1)

if __name__ == "__main__":
    main()
