import socket
import  sys
from rich import print
from rich.panel import Panel
from datetime import datetime

target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1" 
conteudo = (f"Iniciando scan em [green]{target}[/]")
conteudo += (f"\nHora de início: [yellow]{datetime.now()}[/]")
print(Panel(conteudo, title="PORT SCANNER", width=50))

try:
    for porta in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        resultado = s.connect_ex((target, porta))
        
        if resultado == 0:
            print(f"Porta {porta}: ABERTA")
        s.close()

except KeyboardInterrupt:
    print("\nScan cancelado.")

print("-" * 40)
print("Scan finalizado.")
