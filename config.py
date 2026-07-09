import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# File Paths (resolved absolute paths to prevent working directory issues)
BLACKLIST_FILE = os.path.join(BASE_DIR, "blacklist.txt")
LOG_FILE = os.path.join(BASE_DIR, "firewall_log.txt")
REPORT_FILE = os.path.join(BASE_DIR, "firewall_report.csv")

# Credentials Configuration
# Default Username: sai
# Default Password: saie1007
USERNAME = "sai"
PASSWORD_HASH = "17c11c25d8c5bd857bd69e1d82f528dbe81f20b59f77137ebbe3fceca2f9ecc5"
