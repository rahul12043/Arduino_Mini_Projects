from flask import Flask, render_template, jsonify
import serial

app = Flask(__name__)

# Open the serial port
ser = serial.Serial('COM5', 9600)
ser.flush()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/data')
def data():
    # Read data from the serial port
    data = []
    for _ in range(4):  # Read 4 lines of data
        line = ser.readline().decode().strip()
        data.append(line)
    return jsonify(data)  # Return data as JSON

if __name__ == "__main__":
    app.run(debug=False)
