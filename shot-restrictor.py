import os
import platform
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def create_dummy_file(drive_path, avg_jpeg_size_mb, num_shots):
    free_space_to_leave = int(avg_jpeg_size_mb * num_shots * 1024 * 1024)  # Convert MB to bytes
    if platform.system() == "Windows":
        import ctypes
        _, total_space, free_space = ctypes.c_ulonglong(), ctypes.c_ulonglong(), ctypes.c_ulonglong()
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(drive_path, None, ctypes.byref(total_space), ctypes.byref(free_space))
        free_space = free_space.value
    else:
        statvfs = os.statvfs(drive_path)
        free_space = statvfs.f_frsize * statvfs.f_bavail
    
    target_file_size = free_space - free_space_to_leave

    if target_file_size <= 0:
        messagebox.showerror("Error", "Not enough space to create a dummy file with the specified requirements.")
        return

    dummy_file_path = os.path.join(drive_path, "dummy.dat")
    
    with open(dummy_file_path, 'wb') as dummy_file:
        dummy_file.seek(target_file_size - 1)
        dummy_file.write(b'\0')

    messagebox.showinfo("Success", f"Dummy file created: {dummy_file_path}\nSize: {target_file_size / (1024 ** 3):.2f} GB\nFree space left: {free_space_to_leave / (1024 ** 3):.2f} GB")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, folder_selected)

def on_create():
    try:
        drive_path = entry_path.get()
        avg_jpeg_size_mb = float(entry_avg_size.get())
        num_shots = int(entry_num_shots.get())
        create_dummy_file(drive_path, avg_jpeg_size_mb, num_shots)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for average JPEG size and number of shots.")

app = tk.Tk()
app.title("Shot Restrictor")

description = ttk.Label(app, text="This tool helps create a more intentional photography experience by simulating the limitation of film. "
                                  "By generating a dummy file, it restricts the number of available shots on your SD card.", wraplength=400, justify="left")
description.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

ttk.Label(app, text="SD Card:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_path = ttk.Entry(app, width=50)
entry_path.grid(row=1, column=1, padx=10, pady=5)
ttk.Button(app, text="Browse...", command=browse_folder).grid(row=1, column=2, padx=10, pady=5)

ttk.Label(app, text="Average JPEG Size (MB):").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_avg_size = ttk.Entry(app)
entry_avg_size.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(app, text="Number of Shots:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
entry_num_shots = ttk.Entry(app)
entry_num_shots.grid(row=3, column=1, padx=10, pady=5)

ttk.Button(app, text="Generate", command=on_create).grid(row=4, column=0, columnspan=3, padx=10, pady=20)

app.mainloop()
