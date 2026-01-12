"""
File Name: basic_qr_generator.py

WHEN TO USE THIS FILE:
---------------------
Run this file when you only need QUICK QR generation
and DO NOT care about saving the count between runs.

Each time the program is restarted, numbering will begin from 0.

This is useful for:
- Learning while loops
- Understanding counters
- Small demos
- One-time QR creation
"""

import qrcode

# Counter starts fresh every time the program runs
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
