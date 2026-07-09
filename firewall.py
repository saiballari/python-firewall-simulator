import sys
import utils
import config

def login():
    print("===== Firewall CLI Login =====")
    username = input("Username: ")
    password = input("Password: ")

    if username != config.USERNAME or not utils.verify_password(password):
        print("❌ Access Denied")
        sys.exit()
    print("✅ Login Successful")

def check_access(ip, port, blocked_ips):
    blocked_ports = [80, 443]

    if ip in blocked_ips:
        print(f"\n❌ Access Denied: IP {ip} is blocked!")
        utils.write_log_entry("BLOCKED IP", ip, port)
    elif port in blocked_ports:
        print(f"\n❌ Access Denied: Port {port} is blocked!")
        utils.write_log_entry("BLOCKED PORT", ip, port)
    else:
        print(f"\n✅ Access Granted: {ip}:{port}")
        utils.write_log_entry("ALLOWED", ip, port)

def main():
    login()
    
    blocked_ips = utils.load_blacklist()
    
    while True:
        print("\n===== SIMPLE FIREWALL v2 (CLI) =====")
        print("1. Check Connection")
        print("2. View Logs")
        print("3. Add IP to Blacklist")
        print("4. Show Blacklisted IPs")
        print("5. Remove IP from Blacklist")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            ip = input("Enter IP Address: ").strip()
            if not utils.validate_ip(ip):
                print("❌ Error: Invalid IP Address format (e.g., 192.168.1.1)")
                continue
                
            port_input = input("Enter Port Number: ").strip()
            if not utils.validate_port(port_input):
                print("❌ Error: Invalid Port Number (must be integer between 1 and 65535)")
                continue
                
            port = int(port_input)
            check_access(ip, port, blocked_ips)

        elif choice == "2":
            logs = utils.parse_logs()
            if not logs:
                print("\nNo logs found.")
            else:
                print("\n===== FIREWALL LOGS =====")
                print(f"{'Timestamp':<20} | {'Status':<12} | {'IP Address':<15} | {'Port':<6}")
                print("-" * 62)
                for entry in logs:
                    print(f"{entry['timestamp']:<20} | {entry['status']:<12} | {entry['ip']:<15} | {entry['port']:<6}")

        elif choice == "3":
            new_ip = input("Enter IP to block: ").strip()
            if not utils.validate_ip(new_ip):
                print("❌ Error: Invalid IP Address format")
                continue
                
            if new_ip not in blocked_ips:
                blocked_ips.append(new_ip)
                utils.save_blacklist(blocked_ips)
                print(f"✅ {new_ip} added to blacklist")
            else:
                print("❌ IP already exists in blacklist")

        elif choice == "4":
            print("\n===== BLOCKED IPS =====")
            if not blocked_ips:
                print("(No blocked IPs)")
            for ip in blocked_ips:
                print(ip)

        elif choice == "5":
            remove_ip = input("Enter IP to remove: ").strip()
            if remove_ip in blocked_ips:
                blocked_ips.remove(remove_ip)
                utils.save_blacklist(blocked_ips)
                print(f"✅ {remove_ip} removed from blacklist")
            else:
                print("❌ IP not found in blacklist")

        elif choice == "6":
            print("Firewall CLI Stopped.")
            break

        else:
            print("❌ Invalid Choice!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nFirewall CLI Stopped.")
        sys.exit()