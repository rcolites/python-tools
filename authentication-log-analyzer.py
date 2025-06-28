# VERSION 1.0

import subprocess

# Run the bash command "journalctl > journalctl.txt"
subprocess.run("journalctl > /tmp/journalctl.txt", shell=True)


# OPEN THE TEXT FILE TO EXAMINE THE AUTHENTICATION LOGS
_file = input("Please input a file: ")
if len(_file) < 1:
    _file = "/tmp/journalctl.txt"
_handle = open(_file, "r")

print("##################################")
print("What do you want to examine? ")
print("##################################")
print("  1: Authentication Failures")
print("##################################")
_selection = input()
_selection = int(_selection)

# CODE FOR THE FIRST SELECTION, AUTH FAILURES:
if _selection == 1:
    # CODE FOR EXAMINING AUTHENTICATION FAILURES IN PVEDAEMON ON PROXMOX
    ## count variable for counting pvedaemon authentication failures
    _count1 = 0
    ################################################################
    _users = [] # using a list to store users

    for lines in _handle:
        lines = lines.strip()
        if "pvedaemon" in lines and "failure" in lines:
            _count1 = _count1 + 1
            #print(_count1, lines)
            _words = lines.split()
            _users.append(_words[8]) # append each user to the _users variable

    # {', '.join(_users)}:
    # This inserts the result of ', '.join(_users) into the string, which joins the list of users into a single string separated by commas.
    print(f"There are {_count1} authentication failures in this journalctl log with the following users: {', '.join(_users)}")

