import serial
import time
import subprocess
import json
from datetime import datetime

# === CONFIG ===
PORT = 'COM5'  # Change to your Arduino COM port
BAUD = 9600
SECRET_KEY = 0xABCDEF
APP_PATH = r"C:\Windows\System32\notepad.exe"  # Change as needed

def generate_otp(unixtime):
    time_chunk = unixtime // 30  # Divide by 30 to chunk the time
    otp = (time_chunk ^ SECRET_KEY) % 1000000  # XOR the chunk with secret key, mod by 1 million
    return str(otp).zfill(6)  # Ensure OTP is 6 digits

def get_arduino_data(ser):
    print("Waiting for data from Arduino...")
    data_received = ""
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            data_received = line
            break
    return data_received

def sync_arduino_time(ser):
    # Get current system time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Sending time to Arduino: {current_time}")
    ser.write(current_time.encode('utf-8') + b"\n")  # Send system time to Arduino

def main():
    print("Waiting for OTP from Arduino...")
    try:
        with serial.Serial(PORT, BAUD, timeout=3) as ser:
            # Wait for Arduino to reboot
            time.sleep(2.5)

            # Sync Arduino time with Python
            sync_arduino_time(ser)

            while True:
                # Get data from Arduino (only after button press)
                data = get_arduino_data(ser)

                # Parse the received JSON
                try:
                    arduino_data = json.loads(data)
                    print(f"Received data from Arduino: {arduino_data}")
                    
                    # Extract OTP and Unix time
                    unix_time = arduino_data["unix_time"]
                    expected_otp = generate_otp(unix_time)

                    # Compare OTP
                    arduino_otp = str(arduino_data["otp"]).zfill(6)
                    print(f"Arduino OTP: {arduino_otp}")
                    print(f"Expected OTP: {expected_otp}")

                    if arduino_otp == expected_otp:
                        print("OTP matched. Launching app...")
                        subprocess.Popen([APP_PATH])
                    else:
                        print("OTP doesn't match. Access denied.")
                
                except json.JSONDecodeError:
                    print("Failed to decode JSON data.")
                    print(f"Received raw data: {data}")

    except serial.SerialException as e:
        print(f"Serial error: {e}")

if __name__ == "__main__":
    main()
