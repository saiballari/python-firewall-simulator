import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import utils
import config

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

class FirewallDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyber Security Firewall Dashboard")
        self.root.configure(bg="#121214")
        center_window(self.root, 1020, 720)
        
        # Load local blacklist copy
        self.blocked_ips = utils.load_blacklist()
        
        # Stats variables
        self.total_checks_var = tk.StringVar(value="0")
        self.allowed_count_var = tk.StringVar(value="0")
        self.blocked_count_var = tk.StringVar(value="0")
        
        self.setup_styles()
        self.create_widgets()
        
        # Load initial data
        self.refresh_data()

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # General Styles
        self.style.configure(".", background="#121214", foreground="#ffffff", fieldbackground="#121214")
        
        # Frame Card Style
        self.style.configure("Card.TFrame", background="#1a1a1f")
        
        # Label Styles
        self.style.configure("TLabel", background="#121214", foreground="#ffffff", font=("Segoe UI", 10))
        self.style.configure("Card.TLabel", background="#1a1a1f", foreground="#ffffff", font=("Segoe UI", 9))
        self.style.configure("Header.TLabel", background="#121214", foreground="#ffffff", font=("Segoe UI Semibold", 18))
        self.style.configure("SubHeader.TLabel", background="#121214", foreground="#9ca3af", font=("Segoe UI", 10))
        
        # Treeview Custom Styles (Modern Table)
        self.style.configure("Treeview", 
                             background="#1a1a1f", 
                             foreground="#ffffff", 
                             fieldbackground="#1a1a1f", 
                             rowheight=26, 
                             font=("Segoe UI", 9),
                             relief="flat")
        self.style.configure("Treeview.Heading", 
                             background="#27272a", 
                             foreground="#ffffff", 
                             font=("Segoe UI Semibold", 9), 
                             relief="flat",
                             padding=4)
        self.style.map("Treeview", 
                       background=[("selected", "#3b82f6")], 
                       foreground=[("selected", "#ffffff")])
        self.style.map("Treeview.Heading",
                       background=[("active", "#3f3f46")])

        # Button Styles
        self.style.configure("Primary.TButton", background="#3b82f6", foreground="#ffffff", font=("Segoe UI Bold", 9), borderwidth=0, focuscolor="none", padding=6)
        self.style.map("Primary.TButton", background=[("active", "#60a5fa")])

        self.style.configure("Success.TButton", background="#10b981", foreground="#ffffff", font=("Segoe UI Bold", 9), borderwidth=0, focuscolor="none", padding=6)
        self.style.map("Success.TButton", background=[("active", "#34d399")])

        self.style.configure("Danger.TButton", background="#ef4444", foreground="#ffffff", font=("Segoe UI Bold", 9), borderwidth=0, focuscolor="none", padding=6)
        self.style.map("Danger.TButton", background=[("active", "#f87171")])

        self.style.configure("Secondary.TButton", background="#3f3f46", foreground="#ffffff", font=("Segoe UI Bold", 9), borderwidth=0, focuscolor="none", padding=6)
        self.style.map("Secondary.TButton", background=[("active", "#52525b")])

    def create_widgets(self):
        # 1. Header Frame
        header_frame = tk.Frame(self.root, bg="#121214", height=80)
        header_frame.pack(fill="x", padx=25, pady=(20, 10))
        
        title = ttk.Label(header_frame, text="🛡️ CYBER SIMULATOR FIREWALL", style="Header.TLabel")
        title.pack(anchor="w")
        subtitle = ttk.Label(header_frame, text="Real-time Network Access Control List (ACL) & Traffic Monitoring Dashboard", style="SubHeader.TLabel")
        subtitle.pack(anchor="w", pady=(2, 0))

        # Divider line
        divider = tk.Frame(self.root, bg="#27272a", height=1)
        divider.pack(fill="x", padx=25, pady=(0, 15))

        # 2. Main Dashboard Body Frame
        body_frame = tk.Frame(self.root, bg="#121214")
        body_frame.pack(fill="both", expand=True, padx=25, pady=(0, 20))

        # 2A. Left Control Column
        left_column = tk.Frame(body_frame, bg="#121214", width=340)
        left_column.pack(side="left", fill="y", padx=(0, 15))
        left_column.pack_propagate(False)

        # -- Connection Tester Card
        conn_card = tk.LabelFrame(left_column, text=" CONNECTION TESTER ", bg="#1a1a1f", fg="#3b82f6", 
                                  font=("Segoe UI Bold", 10), bd=1, relief="solid", padx=15, pady=12)
        conn_card.pack(fill="x", pady=(0, 15))

        ttk.Label(conn_card, text="IP Address (IPv4/IPv6)", style="Card.TLabel").pack(anchor="w", pady=(0, 2))
        self.ip_test_entry = tk.Entry(conn_card, bg="#27272a", fg="#ffffff", insertbackground="#ffffff", 
                                      relief="flat", font=("Segoe UI", 10), bd=5, highlightthickness=1, highlightbackground="#3f3f46", highlightcolor="#3b82f6")
        self.ip_test_entry.pack(fill="x", pady=(0, 12))
        self.ip_test_entry.insert(0, "192.168.1.1")

        ttk.Label(conn_card, text="Port Number", style="Card.TLabel").pack(anchor="w", pady=(0, 2))
        self.port_test_entry = tk.Entry(conn_card, bg="#27272a", fg="#ffffff", insertbackground="#ffffff", 
                                        relief="flat", font=("Segoe UI", 10), bd=5, highlightthickness=1, highlightbackground="#3f3f46", highlightcolor="#3b82f6")
        self.port_test_entry.pack(fill="x", pady=(0, 15))
        self.port_test_entry.insert(0, "80")

        self.test_conn_btn = ttk.Button(conn_card, text="CHECK TRAFFIC CONNECTION", style="Primary.TButton", command=self.check_connection)
        self.test_conn_btn.pack(fill="x", ipady=2)

        self.conn_result_lbl = tk.Label(conn_card, text="Ready to Test", bg="#1a1a1f", fg="#9ca3af", font=("Segoe UI Semibold", 10), pady=8)
        self.conn_result_lbl.pack(fill="x")

        # -- Blacklist Control Card
        blacklist_card = tk.LabelFrame(left_column, text=" BLACKLIST ADMINISTRATOR ", bg="#1a1a1f", fg="#ef4444", 
                                       font=("Segoe UI Bold", 10), bd=1, relief="solid", padx=15, pady=12)
        blacklist_card.pack(fill="both", expand=True)

        ttk.Label(blacklist_card, text="Block New IP Address", style="Card.TLabel").pack(anchor="w", pady=(0, 2))
        
        block_ip_frame = tk.Frame(blacklist_card, bg="#1a1a1f")
        block_ip_frame.pack(fill="x", pady=(0, 10))
        
        self.ip_block_entry = tk.Entry(block_ip_frame, bg="#27272a", fg="#ffffff", insertbackground="#ffffff", 
                                       relief="flat", font=("Segoe UI", 10), bd=5, highlightthickness=1, highlightbackground="#3f3f46", highlightcolor="#ef4444")
        self.ip_block_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))
        
        self.add_block_btn = ttk.Button(block_ip_frame, text="BLOCK", style="Danger.TButton", command=self.block_ip_action)
        self.add_block_btn.pack(side="right")

        # Blacklisted IPs List
        ttk.Label(blacklist_card, text="Currently Blocked IPs", style="Card.TLabel").pack(anchor="w", pady=(5, 2))
        
        list_frame = tk.Frame(blacklist_card, bg="#1a1a1f")
        list_frame.pack(fill="both", expand=True, pady=(0, 10))
        
        self.blacklist_scroll = ttk.Scrollbar(list_frame, orient="vertical")
        self.blacklist_scroll.pack(side="right", fill="y")
        
        self.blacklist_listbox = tk.Listbox(list_frame, bg="#27272a", fg="#ffffff", selectbackground="#ef4444", 
                                            selectforeground="#ffffff", relief="flat", font=("Segoe UI Semibold", 9), 
                                            bd=4, highlightthickness=0, yscrollcommand=self.blacklist_scroll.set)
        self.blacklist_listbox.pack(side="left", fill="both", expand=True)
        self.blacklist_scroll.config(command=self.blacklist_listbox.yview)

        self.remove_block_btn = ttk.Button(blacklist_card, text="UNBLOCK SELECTED IP", style="Secondary.TButton", command=self.unblock_ip_action)
        self.remove_block_btn.pack(fill="x", ipady=2)


        # 2B. Right Stats & Logs Column
        right_column = tk.Frame(body_frame, bg="#121214")
        right_column.pack(side="right", fill="both", expand=True)

        # -- Statistics Row
        stats_frame = tk.Frame(right_column, bg="#121214")
        stats_frame.pack(fill="x", pady=(0, 15))
        stats_frame.columnconfigure(0, weight=1)
        stats_frame.columnconfigure(1, weight=1)
        stats_frame.columnconfigure(2, weight=1)

        # Total Card
        card_total = tk.Frame(stats_frame, bg="#1a1a1f", bd=1, relief="solid", highlightbackground="#27272a")
        card_total.grid(row=0, column=0, padx=(0, 8), sticky="nsew")
        tk.Label(card_total, textvariable=self.total_checks_var, bg="#1a1a1f", fg="#3b82f6", font=("Segoe UI Bold", 20)).pack(pady=(10, 2))
        tk.Label(card_total, text="TOTAL CHECKS", bg="#1a1a1f", fg="#9ca3af", font=("Segoe UI Semibold", 8)).pack(pady=(0, 10))

        # Allowed Card
        card_allowed = tk.Frame(stats_frame, bg="#1a1a1f", bd=1, relief="solid", highlightbackground="#27272a")
        card_allowed.grid(row=0, column=1, padx=4, sticky="nsew")
        tk.Label(card_allowed, textvariable=self.allowed_count_var, bg="#1a1a1f", fg="#10b981", font=("Segoe UI Bold", 20)).pack(pady=(10, 2))
        tk.Label(card_allowed, text="ALLOWED CONNS", bg="#1a1a1f", fg="#9ca3af", font=("Segoe UI Semibold", 8)).pack(pady=(0, 10))

        # Blocked Card
        card_blocked = tk.Frame(stats_frame, bg="#1a1a1f", bd=1, relief="solid", highlightbackground="#27272a")
        card_blocked.grid(row=0, column=2, padx=(8, 0), sticky="nsew")
        tk.Label(card_blocked, textvariable=self.blocked_count_var, bg="#1a1a1f", fg="#ef4444", font=("Segoe UI Bold", 20)).pack(pady=(10, 2))
        tk.Label(card_blocked, text="BLOCKED CONNS", bg="#1a1a1f", fg="#9ca3af", font=("Segoe UI Semibold", 8)).pack(pady=(0, 10))

        # -- Real-Time Log Viewer Card
        logs_card = tk.LabelFrame(right_column, text=" FIREWALL ACTIVITY MONITOR ", bg="#1a1a1f", fg="#10b981", 
                                  font=("Segoe UI Bold", 10), bd=1, relief="solid", padx=15, pady=12)
        logs_card.pack(fill="both", expand=True)

        # Log Search Frame
        search_frame = tk.Frame(logs_card, bg="#1a1a1f")
        search_frame.pack(fill="x", pady=(0, 10))
        
        tk.Label(search_frame, text="🔍 Search Logs:", bg="#1a1a1f", fg="#ffffff", font=("Segoe UI Semibold", 9)).pack(side="left", padx=(0, 8))
        self.search_entry = tk.Entry(search_frame, bg="#27272a", fg="#ffffff", insertbackground="#ffffff", 
                                     relief="flat", font=("Segoe UI", 9), bd=4, width=30, highlightthickness=1, highlightbackground="#3f3f46", highlightcolor="#10b981")
        self.search_entry.pack(side="left")
        self.search_entry.bind("<KeyRelease>", lambda event: self.filter_logs())

        # Reset Search Button
        self.clear_search_btn = ttk.Button(search_frame, text="Clear", style="Secondary.TButton", command=self.clear_search)
        self.clear_search_btn.pack(side="left", padx=5)

        # Log Table Treeview
        table_frame = tk.Frame(logs_card, bg="#1a1a1f")
        table_frame.pack(fill="both", expand=True)

        self.table_scroll_y = ttk.Scrollbar(table_frame, orient="vertical")
        self.table_scroll_y.pack(side="right", fill="y")
        
        self.table_scroll_x = ttk.Scrollbar(table_frame, orient="horizontal")
        self.table_scroll_x.pack(side="bottom", fill="x")

        # Treeview definition
        self.log_table = ttk.Treeview(table_frame, columns=("time", "status", "ip", "port"), 
                                      show="headings", yscrollcommand=self.table_scroll_y.set, xscrollcommand=self.table_scroll_x.set)
        
        self.log_table.heading("time", text="Timestamp")
        self.log_table.heading("status", text="Action / Event")
        self.log_table.heading("ip", text="IP Address")
        self.log_table.heading("port", text="Port")
        
        self.log_table.column("time", width=150, anchor="center")
        self.log_table.column("status", width=130, anchor="center")
        self.log_table.column("ip", width=160, anchor="w")
        self.log_table.column("port", width=80, anchor="center")
        
        self.log_table.pack(fill="both", expand=True)
        
        self.table_scroll_y.config(command=self.log_table.yview)
        self.table_scroll_x.config(command=self.log_table.xview)

        # Bottom Actions Frame
        actions_frame = tk.Frame(logs_card, bg="#1a1a1f")
        actions_frame.pack(fill="x", pady=(12, 0))

        self.export_btn = ttk.Button(actions_frame, text="EXPORT LOGS TO CSV", style="Success.TButton", command=self.export_csv)
        self.export_btn.pack(side="left", padx=(0, 10))

        self.clear_logs_btn = ttk.Button(actions_frame, text="CLEAR SYSTEM LOGS", style="Danger.TButton", command=self.clear_logs)
        self.clear_logs_btn.pack(side="left", padx=5)

        self.refresh_btn = ttk.Button(actions_frame, text="REFRESH SYSTEM", style="Secondary.TButton", command=self.refresh_data)
        self.refresh_btn.pack(side="right")

    # --- Controller Actions ---
    
    def refresh_data(self):
        """Re-read blacklist and logs, then update all widgets."""
        self.blocked_ips = utils.load_blacklist()
        self.load_blacklist_to_listbox()
        self.load_logs_to_treeview()
        self.update_statistics_display()

    def update_statistics_display(self):
        stats = utils.get_statistics()
        self.total_checks_var.set(str(stats["total"]))
        self.allowed_count_var.set(str(stats["allowed"]))
        self.blocked_count_var.set(str(stats["blocked"]))

    def load_blacklist_to_listbox(self):
        self.blacklist_listbox.delete(0, tk.END)
        for ip in self.blocked_ips:
            self.blacklist_listbox.insert(tk.END, ip)

    def load_logs_to_treeview(self, filter_text=""):
        # Clear existing logs in the table
        for item in self.log_table.get_children():
            self.log_table.delete(item)
            
        logs = utils.parse_logs()
        filter_text = filter_text.strip().lower()
        
        # Populate table (in reverse order to show newest logs on top)
        for log in reversed(logs):
            ts = log.get("timestamp", "N/A")
            status = log.get("status", "UNKNOWN")
            ip = log.get("ip", "N/A")
            port = log.get("port", "N/A")
            
            # Check for filter match
            if filter_text:
                match = (filter_text in ts.lower() or 
                         filter_text in status.lower() or 
                         filter_text in ip.lower() or 
                         filter_text in str(port).lower())
                if not match:
                    continue

            # Check status type to add color tags/emoji in view
            display_status = status
            if "ALLOWED" in status.upper():
                display_status = "✅ ALLOWED"
                tag = "allowed"
            elif "BLOCKED IP" in status.upper():
                display_status = "🚫 BLOCKED (IP)"
                tag = "blocked"
            elif "BLOCKED PORT" in status.upper():
                display_status = "⚡ BLOCKED (PORT)"
                tag = "blocked"
            else:
                tag = "unknown"
                
            item_id = self.log_table.insert("", tk.END, values=(ts, display_status, ip, port))
            
            # Highlight blocked/allowed connections
            if tag == "allowed":
                self.log_table.tag_configure("allowed", foreground="#34d399")
                self.log_table.item(item_id, tags=("allowed",))
            elif tag == "blocked":
                self.log_table.tag_configure("blocked", foreground="#f87171")
                self.log_table.item(item_id, tags=("blocked",))

    def filter_logs(self):
        search_query = self.search_entry.get()
        self.load_logs_to_treeview(search_query)

    def clear_search(self):
        self.search_entry.delete(0, tk.END)
        self.load_logs_to_treeview()

    def check_connection(self):
        ip = self.ip_test_entry.get().strip()
        port_raw = self.port_test_entry.get().strip()
        
        # Validate IP Address format
        if not utils.validate_ip(ip):
            self.conn_result_lbl.config(text="❌ Invalid IP format!", fg="#ef4444")
            return
            
        # Validate Port format
        if not utils.validate_port(port_raw):
            self.conn_result_lbl.config(text="❌ Invalid Port! (1-65535)", fg="#ef4444")
            return
            
        port = int(port_raw)
        blocked_ports = [80, 443]
        
        # Test Connection against ACL Rules
        if ip in self.blocked_ips:
            status = "BLOCKED IP"
            display_text = f"❌ Connection Blocked: IP {ip} is Blacklisted"
            text_color = "#ef4444"
        elif port in blocked_ports:
            status = "BLOCKED PORT"
            display_text = f"❌ Connection Blocked: Port {port} is Closed"
            text_color = "#ef4444"
        else:
            status = "ALLOWED"
            display_text = f"✅ Access Granted: Connection Allowed to {ip}:{port}"
            text_color = "#10b981"

        # Log connection result
        utils.write_log_entry(status, ip, port)
        
        # Update display results
        self.conn_result_lbl.config(text=display_text, fg=text_color)
        
        # Refresh statistics and table view
        self.refresh_data()

    def block_ip_action(self):
        ip = self.ip_block_entry.get().strip()
        
        if not utils.validate_ip(ip):
            messagebox.showerror("Error", "Please enter a valid IP address format (e.g., 192.168.1.10).")
            return
            
        if ip in self.blocked_ips:
            messagebox.showwarning("Warning", f"IP Address {ip} is already blocked.")
            return
            
        self.blocked_ips.append(ip)
        utils.save_blacklist(self.blocked_ips)
        self.ip_block_entry.delete(0, tk.END)
        
        self.refresh_data()
        messagebox.showinfo("Success", f"IP Address {ip} has been added to blacklist.")

    def unblock_ip_action(self):
        selected_index = self.blacklist_listbox.curselection()
        
        if not selected_index:
            messagebox.showwarning("Warning", "Please select an IP address from the list to unblock.")
            return
            
        selected_ip = self.blacklist_listbox.get(selected_index)
        
        if selected_ip in self.blocked_ips:
            self.blocked_ips.remove(selected_ip)
            utils.save_blacklist(self.blocked_ips)
            self.refresh_data()
            messagebox.showinfo("Success", f"IP Address {selected_ip} has been removed from blacklist.")

    def export_csv(self):
        success = utils.export_logs_to_csv()
        if success:
            messagebox.showinfo("Success", f"System logs successfully exported to CSV.\nSaved to: {config.REPORT_FILE}")
        else:
            messagebox.showerror("Error", "Failed to export logs. Ensure file is not open elsewhere.")

    def clear_logs(self):
        confirm = messagebox.askyesno("Clear System Logs", "Are you sure you want to delete all logged traffic history permanently?")
        if confirm:
            try:
                # Truncate log file
                with open(config.LOG_FILE, "w"):
                    pass
                self.refresh_data()
                messagebox.showinfo("Success", "System connection logs have been wiped.")
            except Exception as e:
                messagebox.showerror("Error", f"Could not clear logs: {e}")

def launch_dashboard():
    root = tk.Tk()
    app = FirewallDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    launch_dashboard()