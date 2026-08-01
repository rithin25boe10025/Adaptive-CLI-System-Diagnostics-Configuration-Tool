# Adaptive CLI System Diagnostics & Configuration Tool

## Project Description

This project is a Python-based CLI tool that provides basic system diagnostics and configuration options. It displays system, disk, and network information and allows users to change the working directory through a simple, interactive menu.

## Features

* Displays basic system information
* Shows disk space details
* Displays network and IP information
* Shows the current working directory
* Allows users to change the working directory
* Provides a simple interactive CLI menu
* Beginner-friendly implementation
* Uses only built-in Python modules

## Modules Used

* `os` – File and directory operations
* `platform` – Operating system and hardware information
* `socket` – Hostname and IP address
* `shutil` – Disk space information

No external packages are required.

## Main Functions

| Function          | Purpose                                                                |
| ----------------- | ---------------------------------------------------------------------- |
| `system_info()`   | Displays operating system, processor, computer name and Python version |
| `disk_info()`     | Displays total, used and free disk space                               |
| `network_info()`  | Displays computer name and IP address                                  |
| `configuration()` | Displays and changes the current working directory                     |
| `main()`          | Controls the main CLI menu                                             |

## Menu Options

1. **System Information** – Displays basic computer information.
2. **Disk Information** – Displays available disk space.
3. **Network Information** – Displays hostname and IP address.
4. **Configuration** – Displays or changes the current working directory.
5. **Exit** – Closes the program.

## Requirements

* Python 3.x
* No external libraries or packages

## How to Run

1. Install Python 3.x.
2. Save the program as:

```text
system_diagnostics.py
```

3. Open Command Prompt or Terminal.
4. Navigate to the program folder.
5. Run:

```bash
python system_diagnostics.py
```

## Sample Output

```text
===== SYSTEM DIAGNOSTICS TOOL =====
1. System Information
2. Disk Information
3. Network Information
4. Configuration
5. Exit

Enter choice: 1

--- System Information ---
OS: Windows
Machine: AMD64
Processor: Intel(R) Core(TM)
Computer: DESKTOP-PC
Python: 3.12.4
```

### Disk Information

```text
Enter choice: 2

--- Disk Information ---
Total: 476.94 GB
Used : 218.52 GB
Free : 258.42 GB
```

### Network Information

```text
Enter choice: 3

--- Network Information ---
Computer: DESKTOP-PC
IP Address: 192.168.1.10
```

### Configuration

```text
Enter choice: 4

--- Configuration ---
Current Folder: C:\Users\User\Desktop

Enter new folder path (or press Enter to skip):
```

### Exit

```text
Enter choice: 5

Thank you!
```

> **Note:** The actual system information, disk space, computer name, and IP address will vary depending on the computer running the program.

## Project Structure

```text
Adaptive-CLI-System-Diagnostics/
│
├── system_diagnostics.py
└── README.md
```

## Learning Outcomes

This project helps beginners understand:

* Python functions
* Conditional statements
* While loops
* User input
* Python modules
* File and directory operations
* Basic system information retrieval
* Command Line Interface (CLI) development

## Future Improvements

* CPU usage monitoring
* RAM usage monitoring
* Battery information
* Internet connectivity testing
* System health score
* Temporary file cleanup
* Diagnostic report generation
* Graphical user interface (GUI)

## Conclusion

The Adaptive CLI System Diagnostics & Configuration Tool is a simple beginner-level Python project that demonstrates how Python can interact with the operating system and provide useful system information through a command-line interface.

---

**Author: Rithin Bala B** 

**Reg No.: 25BOE10025**

**course: Python Programming**

**Branch: B tech. Bioengineering**


