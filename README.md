
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

The project uses the following built-in Python modules:

* `os` – Used for file and directory operations
* `platform` – Used to obtain operating system and hardware information
* `socket` – Used to obtain hostname and IP address
* `shutil` – Used to check disk space

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

The program provides the following options:

1. **System Information** – Displays basic computer information.
2. **Disk Information** – Displays available disk space.
3. **Network Information** – Displays hostname and IP address.
4. **Configuration** – Displays or changes the current working directory.
5. **Exit** – Closes the program.

## Requirements

* Python 3.x
* No external libraries or packages

## How to Run

1. Install Python 3.x on your computer.
2. Save the Python program as:

```text
system_diagnostics.py
```

3. Open Command Prompt or Terminal.
4. Navigate to the folder containing the program.
5. Run:

```bash
python system_diagnostics.py
```

## Sample Menu

```text
===== SYSTEM DIAGNOSTICS TOOL =====
1. System Information
2. Disk Information
3. Network Information
4. Configuration
5. Exit

Enter choice:
```

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

The project can be enhanced by adding:

* CPU usage monitoring
* RAM usage monitoring
* Battery information
* Internet connectivity testing
* System health score
* Temporary file cleanup
* Diagnostic report generation
* A graphical user interface (GUI)

## Conclusion
---

**Author: Rithin Bala B** 

**Reg No.: 25BOE10025**

**course: Python Programming**

**Branch: B tech. Bioengineering**

The Adaptive CLI System Diagnostics & Configuration Tool is a simple beginner-level Python project that demonstrates how Python can interact with the operating system and provide useful system information through a command-line interface.
