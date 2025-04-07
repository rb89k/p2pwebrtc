import netifaces

def generate_routing_table():
    routing_table = []
    # Loop through network interfaces
    for interface in netifaces.interfaces():
        # Initialize current address of interface
        interface_addresses = netifaces.ifaddresses(interface)
        # Check for, then loop through the addresses
        if netifaces.AF_INET in interface_addresses:
            for entry in interface_addresses[netifaces.AF_INET]:
                # Create routing entry where found
                if 'netmask' in entry and 'addr' in entry:
                    routing_entry = {
                        'interface': interface,
                        'destination': entry['addr'],
                        'netmask': entry['netmask']
                    }
                    # Append route to routing table
                    routing_table.append(routing_entry)
    return routing_table


# Calls generate_routing_table
routing_table = generate_routing_table()

# Display routing table
for entry in routing_table:
    print(f"Interface: {entry['interface']}")
    print(f"Destination: {entry['destination']}")
    print(f"Netmask: {entry['netmask']}")
    print("-" * 30)

