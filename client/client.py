import requests
import serial
from time import sleep

def postServer(lightOut: str):
    url = 'locallhost:3000/'

    data = {
        'lightOut': lightOut,
    }

    try:
        # Send a POST request to the server
        response = requests.post(url, json=data)

        # Check the response status code
        if response.status_code == requests.codes.ok:
            # Request was successful
            print('POST request successful')
            # Parse the response as JSON
            response_data = response.json()
            # Process the response data as needed
            print('Response:', response_data)
        else:
            # Request failed
            print('POST request failed with status code:', response.status_code)

    except requests.exceptions.RequestException as e:
        # Request encountered an exception
        print('POST request failed:', e)

    return None 
serOut = serial.Serial('/dev/cu.usbmodem1201', 9601)  # Replace '/dev/cu.usbmodem1101' with your Arduino's serial port

while True:
    if serOut.in_waiting > 0:
        lightOut = serOut.readline().decode('utf-8').rstrip()
        postServer(lightOut)
        sleep(10) # Check the light value every 10 seconds