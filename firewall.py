import sys
import os
import pydivert

# Define your firewall rules here
BLOCKLIST_IPS = {
    "8.8.8.8": "Blocked Google DNS Example",
    "142.250.190.46": "Blocked Target IP Example"
}

BLOCKLIST_PORTS = {
    80: "HTTP Traffic Blocked"
}

def is_admin():
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

def start_firewall():
    if not is_admin():
        print("[-] Error: This firewall script must be run as an Administrator!")
        sys.exit(1)

    print("[*] Initializing Windows Personal Firewall...")
    print("[*] Loading packet filtering rules...")
    
    filter_string = "outbound and ip"

    # Open the network interface manually without using 'with' to prevent syntax conflicts
    handle = pydivert.WinDivert(filter_string)
    
    try:
        handle.open()
        print("[+] Firewall actively monitoring outbound traffic. Press Ctrl+C to stop.\n")
        
        for packet in handle:
            dst_addr = packet.dst_addr
            dst_port = None
            
            if packet.tcp:
                dst_port = packet.tcp.dst_port
            elif packet.udp:
                dst_port = packet.udp.dst_port

            block_packet = False
            reason = ""

            if dst_addr in BLOCKLIST_IPS:
                block_packet = True
                reason = BLOCKLIST_IPS[dst_addr]
            elif dst_port in BLOCKLIST_PORTS:
                block_packet = True
                reason = BLOCKLIST_PORTS[dst_port]

            if block_packet:
                print(f"[BLOCK] Dropped packet to {dst_addr}:{dst_port if dst_port else 'N/A'} | Reason: {reason}")
                continue
            else:
                handle.send(packet)

    except KeyboardInterrupt:
        print("\n[*] Shutting down personal firewall safely.")
    except Exception as e:
        print(f"[-] Critical Runtime Error: {e}")
    finally:
        try:
            handle.close()
        except:
            pass

if __name__ == "__main__":
    start_firewall()
