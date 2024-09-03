Code Explanation
The provided code implements a basic port and service scanner in Python. Here’s a breakdown of its components:

Imports: The socket library is imported to facilitate network connections.

Function scan_ports:

This function takes three parameters: host, start_port, and end_port.
It initializes an empty list open_ports to store the ports that are found to be open.
A loop iterates through the range of ports specified by the user. For each port, a socket is created and a connection attempt is made using connect_ex(), which returns 0 if the connection is successful (indicating the port is open).
If a port is open, it appends the port number to the open_ports list and retrieves the service name using the get_service_name function.
The results are printed to the console, indicating whether each port is open or closed.
Function get_service_name:

This function attempts to retrieve the service name associated with a given port using getservbyport(). If the port does not correspond to a known service, it returns "Unknown service".
Main Execution Block:

The script prompts the user for the target host and the range of ports to scan.
It then calls the scan_ports function and displays the list of open ports at the end.
This scanner is a straightforward tool for network diagnostics and can be expanded with additional features such as multi-threading for faster scanning or more detailed service information.
