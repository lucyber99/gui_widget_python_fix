import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from tkinter import messagebox

user_info = {
    "username": "admin",
    "password": "admin123"
}

def message_info(text):
    messagebox.showinfo('Validasi', text)

def validasi():
    input_username = entry_username.get()
    input_password = entry_password.get()
    if input_username == user_info["username"] and input_password == user_info["password"]:
        message_info("Login berhasil!")
    else:
        message_info("Maaf, username atau password salah.")

def new_window():
    new_window_reg = Toplevel(window)
    new_window_reg.title("Register Akun")
    new_window_reg.geometry("250x150")

    label_register_username = ttk.Label(new_window_reg, text="Username:")
    label_register_username.pack()
    entry_register_username = ttk.Entry(new_window_reg)
    entry_register_username.pack()

    label_register_password = ttk.Label(new_window_reg, text="Password:")
    label_register_password.pack()
    entry_register_password = ttk.Entry(new_window_reg, show="*")
    entry_register_password.pack()

    def save_register():
        user_info["username"] = entry_register_username.get()
        user_info["password"] = entry_register_password.get()
        message_info("Akun berhasil diregistrasi!")
        new_window_reg.destroy()

    button_register = ttk.Button(new_window_reg, text="Simpan", command=save_register)
    button_register.pack(pady=5)

# Jendela utama
window = tk.Tk()
window.title("Input Nilai")
window.geometry("300x200")

label_username = ttk.Label(window, text="Username:")
label_username.pack()
entry_username = ttk.Entry(window)
entry_username.pack()

label_password = ttk.Label(window, text="Password:")
label_password.pack()
entry_password = ttk.Entry(window, show="*")
entry_password.pack()

tombol_login = ttk.Button(window, text="Login", command=validasi)
tombol_login.pack(pady=5)
tombol_register = ttk.Button(window, text="Register", command=new_window)
tombol_register.pack()

window.mainloop()
