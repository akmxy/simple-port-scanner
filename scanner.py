import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        print(f"[+] Porta {port} aberta")
        sock.close()
    except:
        pass

if __name__ == "__main__":
    target = input("Digite o IP para escanear: ")
    ports = range(1, 1025)

    print(f"\nIniciando o scan em {target}...\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports:
            executor.submit(scan_port, target, port)
