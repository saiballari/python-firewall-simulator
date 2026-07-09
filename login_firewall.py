import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import utils
import config

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def login():
    username = username_entry.get().strip()
    password = password_entry.get()

    if username == config.USERNAME and utils.verify_password(password):
        messagebox.showinfo("Success", "Login Successful! Welcome to Firewall Dashboard.")
        root.destroy()
        
        # Import gui and launch it
        import firewall_gui
        firewall_gui.launch_dashboard()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# Main Login GUI
root = tk.Tk()
root.title("Firewall Login")
root.configure(bg="#1e1e24")
center_window(root, 360, 320)

# Set standard styles
style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", background="#1e1e24", foreground="#ffffff", font=("Segoe UI", 10))
style.configure("Title.TLabel", font=("Segoe UI Semibold", 16), foreground="#ffffff")
style.configure("Login.TButton", background="#4f46e5", foreground="#ffffff", font=("Segoe UI", 10, "bold"), borderwidth=0, focuscolor="none")
style.map("Login.TButton", background=[("active", "#6366f1")])

# Layout
title_label = ttk.Label(root, text="Firewall Access Control", style="Title.TLabel")
title_label.pack(pady=25)

form_frame = tk.Frame(root, bg="#1e1e24")
form_frame.pack(pady=10, padx=40, fill="both", expand=True)

# Username Entry
user_lbl = ttk.Label(form_frame, text="Username")
user_lbl.pack(anchor="w", pady=(0, 5))
username_entry = tk.Entry(form_frame, bg="#2a2b36", fg="#ffffff", insertbackground="#ffffff", 
                          relief="flat", font=("Segoe UI", 10), bd=6)
username_entry.pack(fill="x", pady=(0, 15))
username_entry.focus()

# Password Entry
pass_lbl = ttk.Label(form_frame, text="Password")
pass_lbl.pack(anchor="w", pady=(0, 5))
password_entry = tk.Entry(form_frame, bg="#2a2b36", fg="#ffffff", insertbackground="#ffffff", 
                          show="*", relief="flat", font=("Segoe UI", 10), bd=6)
password_entry.pack(fill="x", pady=(0, 20))

# Bind Enter key to submit login
password_entry.bind("<Return>", lambda event: login())
username_entry.bind("<Return>", lambda event: login())

# Login Button
login_btn = ttk.Button(form_frame, text="LOG IN", command=login, style="Login.TButton")
login_btn.pack(fill="x", ipady=4)

root.mainloop()