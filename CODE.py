from scapy.all import IP, TCP, sr1
import time

import numpy as np
import matplotlib.pyplot as plt 
from threading import Thread
# import keyboard

def measure_response_time(target_ip, target_port):
    """
    This function sends a SYN packet to a specified server and waits for the SYN-ACK response to calculate the round-trip time.

    Args:
    target_ip (str): The IP address of the target server.
    target_port (int): The port of the target server.

    Returns:
    float: The round-trip time in seconds.
    """
    # Create a SYN packet
    packet = IP(dst=target_ip)/TCP(dport=target_port, flags='S')

    # Send the packet and record the start time
    start_time = time.time()
    response = sr1(packet, verbose=1)

    # Check if the response is a SYN-ACK packet
    if response[TCP].flags == 'SA':
        # Calculate the round-trip time
        rtt = time.time() - start_time
        return rtt
    else:
        return None


# while True:
#     if keyboard.is_pressed("a"):
#         print("You pressed 'a'.")
#         break
# Test the function
print("Would you like to use our database or input your own web addresses to test? Type 'My own' or 'Yours'")
response = input()

if response == "My own":
    print ("Sounds good! If you'd like to directly compare two websites, enter two domain names then write \"STOP\". Else, if you have a longer list, enter those domains then write \"STOP\".")
    
    list = []
    element = input()
  
    while element != "STOP":
       list.append(element)
       element = input()
    print("Working on your data now!")
    print(list)

if response == "Yours":
    USdomains = ["google.com", "microsoft.com", "nike.com", "timberland.com", "adidas.com", "amazon.com", "apple.com", "asics.com", "underarmour.com", "gap.com", "bing.com", "linkedin.com", "ditch.la", "youtube.com", "docs.google.com", "issaquah.instructure.com", "mail.google.com", "nfl.com", "bbc.com", "adobe.com", "espn.com", "scapy.net", "riotgames.com", "stackoverflow.com", "earth.google.com", "starbucks.com", "spotify.com"]
    NATIONALdomains = ["amazon.in", "nike.in", "amazon.co.uk", "google.co.uk", "adidas.co.uk", "apple.co.uk", "microsoft.co.uk", "gap.co.uk", "bing.co.uk", "linkedin.co.uk", "myntra.com", "amazon.au"]

    USRTT = dict()
    for domain in USdomains:
        rtt = measure_response_time(domain, 80) * 1000
        USRTT.update({domain : rtt})
        if rtt is not None:
            print(f'The round-trip time is {rtt} ms (milliseconds).')
        else:
            print('No SYN-ACK response received.')

    s = sorted(USRTT.items(), key=lambda item : item[1])
    print(s)
    fig, ax = plt.subplots()

    USRTTX = list(USRTT.keys())
    USRTTY = list(USRTT.values())
    ax.bar(USRTTX, USRTTY)

    ax.set_ylabel('ROUND TRIP TIME')
    ax.set_xlabel('PACKET DESTINATION')

    ax.set_title('RTT vs. PACKET DEST.')
    plt.xticks(rotation=90)
    plt.subplots_adjust(bottom=0.479)


    plt.show()

    