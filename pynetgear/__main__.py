"""Run PyNetgear from the command-line."""
import sys
import time
from pynetgear import Netgear

def main():
    """Scan for devices and print results."""
    netgear = Netgear(*sys.argv[1:])
    devices = netgear.get_attached_devices()

    def print_info():
        info = netgear.get_info()
        print("-\nInfo:")
        for key in info:
            print("\t" + key + ": " + info[key])

    if devices is None:
        print("Error communicating with the Netgear router")
    else:
        print("\n\n")

        print("-\nConnected devices:")
        for i in devices:
            print("\t" + repr(i))
        print_info()
        print("\n\n")

        print("Configuring")

        # WPA2 options:
        #   channel
        #   region
        #   ssid
        #   password
        #   mode
        # No security options:
        #   channel
        #   region
        #   ssid
        #   mode

        netgear.set_wlan_config_wpa2(ssid="HelloWorld", channel="3")
        # netgear.set_wlan_config_no_security("SSID2", "Auto")

        print_info()

if __name__ == '__main__':
    main()
