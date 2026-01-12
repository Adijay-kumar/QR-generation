"""
File Name: persistent_qr_generator.py

WHEN TO USE THIS FILE:
---------------------
Run this file when you want the QR code numbering to CONTINUE
from where it stopped in the previous run.

Example:
Run 1 → project_qr_0.png, project_qr_1.png
Run 2 → project_qr_2.png, project_qr_3.png

This is useful for:
- College events
- Bulk student QR generation
- Avoiding file overwrite
- Real-world tools where history matters

"""

import qrcode
import os

# This file stores the last used QR number
COUNT_FILE = "count.txt"

# Load the previous count if it exists
# This allows the program to remember past runs
if os.path.exists(COUNT_FILE):
    with open(COUNT_FILE, "r") as f:
        count = int(f.read())
else:
    # If this is the first run, start from 0
    count = 0

while True:
    repo_url = input("Enter the github repo link (type 'done' to stop): ")

    if repo_url.lower() == "done":
        break

    qr = qrcode.make(repo_url)
    file_name = f"project_qr_{count}.png"
    qr.save(file_name)

    print(file_name, "created successfully")
    count += 1

# Save the updated count before exiting
# This ensures the next run continues numbering correctly
with open(COUNT_FILE, "w") as f:
    f.write(str(count))
