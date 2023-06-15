import serial

ser = serial.Serial('/dev/ttyACM0', 9600)  # Replace '/dev/cu.usbmodem1101' with your Arduino's serial port

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)  # Print the message received from Arduino
        # Add your desired actions here based on the received message

