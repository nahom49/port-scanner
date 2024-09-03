import socket
import termcolor



print(termcolor.colored("portscanner by Nahom", 'dark_grey'))


def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Set timeout to 1 second
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
                service = get_service_name(port)
                print(termcolor.colored(f"Port {port} is open. Service: {service}" , 'cyan'))
            else:
                pass
    return open_ports

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except OSError:
        return "Unknown"

if __name__ == "__main__":
    target_host = input(termcolor.colored("Enter the host to scan (e.g., 192.168.1.1): " ,"green"))
    start_port = int(input(termcolor.colored("Enter the starting port number: ", 'green')))
    end_port = int(input(termcolor.colored("Enter the ending port number: ", 'green')))
    
    print(termcolor.colored(f"Scanning ports from {start_port} to {end_port} on {target_host}...", 'cyan'))
    open_ports = scan_ports(target_host, start_port, end_port)
    
    if open_ports:
        print(termcolor.colored(f"Open ports: {open_ports}", 'blue'))
    else:
        print(termcolor.colored("No open ports found.", 'light_red' ))



