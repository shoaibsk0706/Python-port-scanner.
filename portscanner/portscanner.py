import socket

def port_scanner(target, ports):
    try:
        # Convert domain to IP if needed
        ip = socket.gethostbyname(target)
        print(f"\n[+] Scanning target: {target} ({ip})\n")
    except socket.gaierror:
        print(f"[-] Error: Unable to resolve domain {target}")
        return

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 1 second timeout
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
        sock.close()

if __name__ == "__main__":
    target = input("Enter domain or IP to scan: ")  # ✅ dynamic input
    ports = [21, 22, 23, 25, 53, 80, 110, 443]     # common ports
    port_scanner(target, ports)
