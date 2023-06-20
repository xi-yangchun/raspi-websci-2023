import serial

#

ser1 = serial.Serial('/dev/cu.usbmodem1101', 9600)  # Replace '/dev/cu.usbmodem1101' with your Arduino's serial port
ser2 = serial.Serial('/dev/cu.usbmodem1201', 9601)  # Replace '/dev/cu.usbmodem1101' with your Arduino's serial port

while True:
    if ser1.in_waiting > 0 and ser2.in_waiting > 0:
        line1 = ser1.readline().decode('utf-8').rstrip()
        line2 = ser2.readline().decode('utf-8').rstrip()
        print(f"Light Ser1: {line1}. Light Ser2: {line2}")  # Print the message received from Arduino
        # Add your desired actions here based on the received message

