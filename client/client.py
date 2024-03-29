import requests
import serial
from time import sleep

def postServer(lightOut: str):
    url = 'http://192.168.1.70:5000/'

    try:
        response = requests.get(url, params={"lightOut": lightOut})

        # Check the response status code
        if response.status_code == requests.codes.ok:
            # Request was successful
            print('get request successful')
        else:
            # Request failed
            print('get request failed with status code:', response.status_code)

    except requests.exceptions.RequestException as e:
        # Request encountered an exception
        print('get request failed:', e)

    return None

serOut = serial.Serial('/dev/tty.usbmodem21101', 9601)  # Replace '/dev/cu.usbmodem1101' with your Arduino's serial port

count = 0
while True:
    if serOut.in_waiting > 0:
        lightOut = serOut.readline().decode('utf-8').rstrip()
        print()
        print(lightOut)
        sleep(0.0001) # Check the light value every 10 seconds
        count += 1
        if count%100 == 0:
            postServer(lightOut)
            count = 0
        
