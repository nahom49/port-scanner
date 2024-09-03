import socket

print("portscanner by Nahom")


def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Set timeout to 1 second
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
                service = get_service_name(port)
                print(f"Port {port} is open. Service: {service}" )
            else:
                pass
    return open_ports

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except OSError:
        return "Unknown"

if __name__ == "__main__":
    target_host = input("Enter the host to scan (e.g., 192.168.1.1): ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))
    
    print(f"Scanning ports from {start_port} to {end_port} on {target_host}...")
    open_ports = scan_ports(target_host, start_port, end_port)
    
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found.")



