<<<<<<< HEAD
import serial
import pyautogui

arduino = serial.Serial('COM6', 9600)  # Change to your port

ACTIONS = {
    "VOLUME_UP": lambda: pyautogui.press('volumeup'),
    "VOLUME_DOWN": lambda: pyautogui.press('volumedown')
}

print("Volume Gesture Controller Ready")

try:
    while True:
        if arduino.in_waiting:
            data = arduino.readline().decode().strip()
            if data in ACTIONS:
                ACTIONS[data]()
                print(f"Volume: {'↑' if data == 'VOLUME_UP' else '↓'}")  # Arrow feedback

except KeyboardInterrupt:
    print("\nExiting...")
finally:
=======
import serial
import pyautogui

arduino = serial.Serial('COM6', 9600)  # Change to your port

ACTIONS = {
    "VOLUME_UP": lambda: pyautogui.press('volumeup'),
    "VOLUME_DOWN": lambda: pyautogui.press('volumedown')
}

print("Volume Gesture Controller Ready")

try:
    while True:
        if arduino.in_waiting:
            data = arduino.readline().decode().strip()
            if data in ACTIONS:
                ACTIONS[data]()
                print(f"Volume: {'↑' if data == 'VOLUME_UP' else '↓'}")  # Arrow feedback

except KeyboardInterrupt:
    print("\nExiting...")
finally:
>>>>>>> 5d6a7b2eb21433a86a0f053ca497810ac631f214
    arduino.close()