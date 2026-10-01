import socket
import sys
from rich import print
from rich.panel import Panel
from datetime import datetime

"""
TCP Port Scanner
Author: Zacarias Eduardo Joao
Description: Simple TCP port scanner for 1-1024 range
Usage: python port_scanner.py <target_ip>
"""

target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"

header = f"Scanning target [green]{target}[/]"
header += f"\nStart time: [yellow]{datetime.now()}[/]"
print(Panel(header, title="PORT SCANNER", width=50))

open_ports = 0
try:
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port}: [green]OPEN[/]")
            open_ports += 1
        s.close()

except KeyboardInterrupt:
    print("\n[!] Scan cancelled by user.")

print("-" * 40)
print(f"[*] Scan completed. {open_ports} open port(s) found.")

