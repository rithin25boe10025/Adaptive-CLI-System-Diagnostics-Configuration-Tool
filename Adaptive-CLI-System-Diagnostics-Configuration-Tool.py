# Adaptive CLI System Diagnostics & Configuration Tool

import os
import platform
import socket
import shutil

def system_info():
    print("\n--- System Information ---")
print("OS:", platform.system())
print("Machine:", platform.machine())
print("Processor:", platform.processor())
print("Computer:", socket.gethostname())
print("Python:", platform.python_version())

def disk_info():
    total, used, free = shutil.disk_usage(os.getcwd())


    print("\n--- Disk Information ---")
    print("total:", round(total / 1024**3, 2), "GB")
    print("used :", round(used / 1024**3, 2), "GB")
    print("free :", round(free / 1024**3, 2), "GB")


def network_info():
    print("\n--- Network Information ---")
host = socket.gethostname()
print("Computer:", host)


try:
    print("IP Address:", socket.gethostbyname(host))
except:
    print("IP Address: Not available")


def configuration():
    print("\n--- Configuration ---")
print("Current Folder:", os.getcwd())


path = input("Enter new folder path (or press Enter to skip): ")

if path:
    if os.path.exists(path):
        os.chdir(path)
        print("Folder changed successfully!")
    else:
        print("Folder not found.")
 

def main():
    while True:
        print("\n===== SYSTEM DIAGNOSTICS TOOL =====")
print("1. System Information")
print("2. Disk Information")
print("3. Network Information")
print("4. Configuration")
print("5. Exit")

choice = input("Enter choice: ")

if choice == "1":
   system_info()

elif choice == "2":
    disk_info()

elif choice == "3":
    network_info()

elif choice == "4":
    configuration()

elif choice == "5":
    print("Thank you!")



else:
    print("Invalid choice!")


main()
