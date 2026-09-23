
# Simple Port Scanner - Ethical Hacking Tool

This is my first cybersecurity project for Open Doors Olympiad portfolio.

## Purpose
To understand how TCP ports work and how attackers find open doors in a system.

## How it works
The script tries to connect to ports 1-1024 on target IP using Python socket library. If connection succeeds, port is open.

## Ethical Use
This tool was tested ONLY on localhost (127.0.0.1) - my own machine. Never scan without permission.

## How to run
pip install rich
python scanner.py

## Screenshot
![scan] (screenshot.jpg)

## What I learned
- How socket works
- Difference between open/closed ports
- Importance of ethical hacking
- UI wiht rich

## Future improvement
Add multithreading to make scan faster.