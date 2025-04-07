import nmap

def scan_network(target):
    try:
        nm = nmap.PortScanner()
        nm.scan(target, arguments='-sS')

        if nm[target].state() == 'up':
            print(f"Host: {target} is up")
            for host in nm.all_hosts():
                print(f"Open Ports on {host}:")
                for proto in nm[host].all_protocols():
                    ports = nm[host][proto].keys()
                    # Loop through each port and print its status (open/closed/etc.)
                    for port in ports:
                        print(
                            f"  Port: {port} - State: {nm[host][proto][port]['state']}"
                        )
        else:
            # If the host is down, print that the target is not responding
            print(f"Host: {target} is down")

    except nmap.PortScannerError as e:
        print(f"Nmap PortScanner Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    # Specify the target IP address or IP range to scan
    target_ip = "192.168.1.1"
    # Call the scan function to perform a vulnerability scan on the
    # target IP
    scan_network(target_ip)
