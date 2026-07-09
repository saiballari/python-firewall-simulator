import os
import re
import ipaddress
import hashlib
import csv
from datetime import datetime
from config import BLACKLIST_FILE, LOG_FILE, REPORT_FILE, PASSWORD_HASH

def validate_ip(ip):
    """
    Validate if the input string is a valid IPv4 or IPv6 address.
    """
    ip_str = ip.strip()
    if not ip_str:
        return False
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

def validate_port(port):
    """
    Validate if the port is an integer between 1 and 65535.
    """
    try:
        p = int(port)
        return 1 <= p <= 65535
    except (ValueError, TypeError):
        return False

def load_blacklist():
    """
    Load blocked IPs from blacklist.txt. If the file does not exist,
    create it with default IPs. Filters out any empty entries.
    """
    if not os.path.exists(BLACKLIST_FILE):
        default_ips = ["192.168.1.10", "10.0.0.5"]
        save_blacklist(default_ips)
        return default_ips
    
    blocked_ips = []
    try:
        with open(BLACKLIST_FILE, "r") as file:
            for line in file:
                ip = line.strip()
                if ip:
                    blocked_ips.append(ip)
    except Exception as e:
        print(f"Error loading blacklist: {e}")
    return blocked_ips

def save_blacklist(blocked_ips):
    """
    Save list of blocked IPs to blacklist.txt.
    """
    try:
        with open(BLACKLIST_FILE, "w") as file:
            for ip in blocked_ips:
                file.write(f"{ip}\n")
    except Exception as e:
        print(f"Error saving blacklist: {e}")

def verify_password(password):
    """
    Verify if the SHA-256 hash of the password matches the configuration hash.
    """
    pwd_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return pwd_hash == PASSWORD_HASH

def parse_logs():
    """
    Parse the firewall log file. Handles both the new structured format:
       YYYY-MM-DD HH:MM:SS | STATUS | IP | Port
    and older log formats dynamically.
    Returns a list of dicts: [{'timestamp', 'status', 'ip', 'port'}]
    """
    logs = []
    if not os.path.exists(LOG_FILE):
        return logs

    try:
        with open(LOG_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                # 1. Parse standard new pipe-delimited format
                parts = [p.strip() for p in line.split("|")]
                if len(parts) == 4:
                    logs.append({
                        "timestamp": parts[0],
                        "status": parts[1],
                        "ip": parts[2],
                        "port": parts[3]
                    })
                    continue

                # 2. Try parsing old formats (with and without timestamps)
                # Check for timestamp prefix (e.g., "2026-06-23 12:00:00 - ...")
                ts_match = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s*-\s*(.*)$", line)
                if ts_match:
                    timestamp = ts_match.group(1)
                    body = ts_match.group(2)
                else:
                    timestamp = "N/A"
                    body = line

                # Try patterns inside body
                if "BLOCKED IP:" in body:
                    m = re.search(r"BLOCKED IP:\s*([^\s,]+),\s*Port:\s*(\d+)", body)
                    if m:
                        logs.append({"timestamp": timestamp, "status": "BLOCKED IP", "ip": m.group(1), "port": m.group(2)})
                        continue
                if "BLOCKED PORT:" in body:
                    m = re.search(r"BLOCKED PORT:\s*(\d+),\s*IP:\s*([^\s,]+)", body)
                    if m:
                        logs.append({"timestamp": timestamp, "status": "BLOCKED PORT", "ip": m.group(2), "port": m.group(1)})
                        continue
                if "ALLOWED:" in body:
                    m = re.search(r"ALLOWED:\s*([^:]+):(\d+)", body)
                    if m:
                        logs.append({"timestamp": timestamp, "status": "ALLOWED", "ip": m.group(1), "port": m.group(2)})
                        continue
                    m = re.search(r"ALLOWED:\s*(.*)", body)
                    if m:
                        logs.append({"timestamp": timestamp, "status": "ALLOWED", "ip": m.group(1), "port": "N/A"})
                        continue
                if "BLOCKED:" in body:
                    m = re.search(r"BLOCKED:\s*(.*)", body)
                    if m:
                        logs.append({"timestamp": timestamp, "status": "BLOCKED IP", "ip": m.group(1), "port": "N/A"})
                        continue
                
                # Fallback if line format is completely unrecognized
                logs.append({
                    "timestamp": timestamp,
                    "status": "UNKNOWN",
                    "ip": body,
                    "port": "N/A"
                })
    except Exception as e:
        print(f"Error parsing logs: {e}")
    return logs

def write_log_entry(status, ip, port):
    """
    Append a log entry using the standardized pipe-delimited format.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(LOG_FILE, "a") as file:
            file.write(f"{timestamp} | {status} | {ip} | {port}\n")
    except Exception as e:
        print(f"Error writing to log: {e}")

def get_statistics():
    """
    Parse existing logs to count historical statistics.
    """
    logs = parse_logs()
    allowed = sum(1 for l in logs if "ALLOWED" in l["status"].upper())
    blocked = sum(1 for l in logs if "BLOCKED" in l["status"].upper() or "BLOCK" in l["status"].upper())
    return {
        "total": len(logs),
        "allowed": allowed,
        "blocked": blocked
    }

def export_logs_to_csv():
    """
    Parse logs and write them in structured CSV format.
    """
    logs = parse_logs()
    try:
        with open(REPORT_FILE, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Timestamp", "Status / Action", "IP Address", "Port"])
            for log in logs:
                writer.writerow([log["timestamp"], log["status"], log["ip"], log["port"]])
        return True
    except Exception as e:
        print(f"Error exporting CSV: {e}")
        return False
