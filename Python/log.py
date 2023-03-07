"""
Simple package to both print and log to file messages
"""
# Standard Imports
import os

# Create the log file if it doesn't exist
if not os.path.exists("log.txt"):
    with open("log.txt", "w"):
        pass

def log(text: str):
    """
    Prints the message and logs message to log file
    """
    print(text)
    with open("log.txt", "a") as fileout:
        fileout.write(text + "\n")
