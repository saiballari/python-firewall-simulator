<div align="center">

# 🛡️ Python Firewall Simulator

### A GUI-Based Firewall Simulator Built with Python & Tkinter

<p>
A desktop-based cybersecurity application that simulates the core functionality of a firewall. The project allows users to monitor and control simulated network access by filtering IP addresses and ports, managing blacklists, recording security logs, viewing statistics, and exporting reports through an intuitive graphical interface.
</p>

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

</div>

---

# 📌 Overview

The **Python Firewall Simulator** is a cybersecurity learning project developed using **Python** and **Tkinter**. It demonstrates how firewall rules work by simulating IP filtering, port filtering, blacklist management, activity logging, and basic monitoring features in a graphical desktop application.

This project is intended for educational purposes to help understand firewall concepts and security event monitoring.

---

# ✨ Features

- 🔐 Admin Login System
- 🌐 IP Address Filtering
- 🚪 Port Filtering
- 🚫 Add IP to Blacklist
- 🗑️ Remove IP from Blacklist
- 📋 View Blacklisted IP Addresses
- 📝 Security Activity Logging
- 🔍 Search Logs by IP Address
- 📊 Firewall Statistics Dashboard
- 📁 Export Logs to CSV
- 💾 Persistent Blacklist Storage
- 🖥️ User-Friendly Tkinter GUI

---

# 🛠️ Technologies Used

- Python 3
- Tkinter
- File Handling
- CSV Module
- Datetime Module

---

# 📂 Project Structure

```
python-firewall-simulator/
│
├── login_firewall.py        # Login Screen
├── firewall_gui.py          # Main GUI Application
├── firewall.py              # Firewall Logic
├── config.py                # Configuration
├── utils.py                 # Utility Functions
├── blacklist.txt            # Stored Blacklisted IPs
├── firewall_log.txt         # Generated Security Logs
├── firewall_report.csv      # Exported Report
├── .gitignore
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/saiballari/python-firewall-simulator.git
```

Go to the project directory

```bash
cd python-firewall-simulator
```

Run the application

```bash
python login_firewall.py
```

---

# 🔑 Default Login Credentials

| Username | Password |
|----------|----------|
| admin | admin123 |

> Update these credentials in the source code if you want to use custom login details.

---

# 📖 How It Works

1. Launch the application.
2. Login using the administrator credentials.
3. Enter an IP Address and Port Number.
4. The firewall checks whether the IP or Port is blocked.
5. Allowed or blocked events are recorded in the log file.
6. Users can:
   - View logs
   - Search logs
   - Add or remove blacklisted IPs
   - Export logs to CSV
   - View firewall statistics

---

# 📊 Current Features

- GUI Firewall Dashboard
- Login Authentication
- IP Filtering
- Port Filtering
- Blacklist Management
- Activity Logging
- Search Logs
- Statistics Monitoring
- CSV Report Export

---

# 📸 Screenshots

Add screenshots here after running the application.

Example:

```
screenshots/
│
├── login.png
├── dashboard.png
├── logs.png
├── statistics.png
└── blacklist.png
```

---

# 🔮 Future Enhancements

- Real-time Network Traffic Monitoring
- Database Integration
- User Management
- Email Alert System
- Graphical Analytics Dashboard
- Advanced Rule Management
- Packet Inspection Simulation

---

# 🎯 Learning Outcomes

This project demonstrates practical understanding of:

- Firewall Concepts
- Network Security Basics
- GUI Development
- Python Programming
- File Handling
- Logging Systems
- Security Monitoring
- Data Export

---

# 👨‍💻 Author

**Sai Ballari**

GitHub:
https://github.com/saiballari

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

---

## 📄 License

This project is developed for educational and learning purposes.

MIT License © 2026 Sai Ballari
