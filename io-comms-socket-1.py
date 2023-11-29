# Import libraries
import socket
import time

# Setup all working variables
port = 443
retry = 5
delay = 1
timeout = 3

# List websites to test
ip = ["facebook.com",
      "google.com",
      "fbi.gov",
      "nottingham.ac.uk",
      "digiscore.github.io",
      "garbage.gigo"
      ]

# Function that opens an ip Socket
def isOpen(ip, port):
    # Instantiate a socket object for a given ip address
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)

    # Try to connect and if successful return a True bool
    try:
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    # Important to close it
    finally:
        s.close()

# Function that dispatches socket info to isOpen func and returns results
def checkHost(ip, port):
    # Sets condition to False
    is_up = False

    # For a number of trys
    for t in range(retry):
        print(f"Checking {ip}")
        if isOpen(ip, port):
            is_up = True
            break
        else:
            time.sleep(delay)
    return is_up

# Function controlling the main loop
def main():
    # For each web address in ip list check if it is up and running
    for i in ip:
        if checkHost(i, port):
            print(f"\t\t{i} is UP and running")
            time.sleep(1)

# Code starts here
if __name__ == "__main__":
    main()
