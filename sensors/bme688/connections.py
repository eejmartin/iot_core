import time
import network
import constants

def connect_wlan():
    """
    Connects to a Wi-Fi network using the provided SSID and password.

    Raises:
        Exception: If there is an issue connecting to the Wi-Fi network.

    """
    try:        
        # Connect to WLAN
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            print('connecting to network')
            wlan.connect(constants.SSID, constants.PASSWORD)
            print('.......')
            for i in range(0, 10):
                if not wlan.isconnected():
                    time.sleep(1)
            print("Connected to Wi-Fi")
    except Exception as e:
        print('There was an issue connecting to WIFI')
        print(e)
