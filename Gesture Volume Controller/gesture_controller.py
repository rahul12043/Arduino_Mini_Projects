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
    arduino.close()