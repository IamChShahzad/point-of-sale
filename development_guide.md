# Development Guide - POS Payment Gateway

Welcome to the POS Payment Gateway project development guide. This document provides an overview of the system architecture, setup instructions, and guidance for developers.

## 🚀 Project Overview

This is a Retail Point of Sale (POS) system built with Python using the Kivy and KivyMD frameworks. It integrates with the SPIn payment gateway for processing credit and EBT transactions and supports ESC/POS thermal printers.

### Tech Stack
- **Language:** Python 3.x
- **UI Framework:** [Kivy](https://kivy.org/) & [KivyMD](https://kivymd.readthedocs.io/)
- **Database:** SQLite3
- **Data Handling:** Pandas
- **Printing:** `python-escpos`
- **Payment Gateway:** SPIn API (REST)

---

## 📁 Project Structure

```bash
pos-payment_gateway/
├── main.py              # Application entry point & Screen switcher
├── mainFunc.py          # Core business logic (Printing, Shifts, Receipts)
├── posapp.kv            # Kivy layout file (UI declarations)
├── requirements.txt     # Python dependencies
├── variable.txt         # Persistent state (Store info, Printers, Shifts)
├── databaseScripts/      # SQLite database management
│   ├── inventory.py     # Inventory CRUD operations
│   ├── shifts.py        # Shift tracking logic
│   └── transactions.py  # Transaction storage
├── kivyScripts/         # UI Screen implementations
│   ├── retailScreen.py  # Main POS transaction screen
│   ├── inventoryScreen.py # Inventory management UI
│   └── payment_gateway.py # SPIn API integration
└── data/                # SQLite database files (.db)
```

---

## 🛠️ Setup & Installation

### 1. Prerequisites
- Python 3.8+
- USB Thermal Printer (Optional, for testing printing)
- SPIn TPN and Auth Key (For payment processing)

### 2. Environment Setup
```bash
# Clone the repository
git clone <repo-url>
cd pos-payment_gateway

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
The system uses a `.env` file for sensitive credentials (ensure this is created based on `.env.example` if applicable) and `variable.txt` for runtime configuration.

---

## 🧠 Core Logic & Workflows

### 1. Persistent State (`variable.txt`)
The application stores its configuration and current shift state in `variable.txt`. This file is read at startup to initialize global dictionaries:
- `data`: Store information (Name, Address, Phone).
- `shift`: Current shift details (Number, Start time).
- `printerSettings`: USB Printer VendorID and ProductID.

### 2. Database Management
Data is stored in `./data/` using SQLite. Key modules in `databaseScripts/` handle table creation and data persistence. 
- **Inventory:** Managed via `databaseScripts/inventory.py`. Uses `items` and `category` tables.

### 3. Payment Processing
Payment logic resides in `kivyScripts/payment_gateway.py`. It communicates with the SPIn API via HTTP requests. 
- Supported operations: `credit_sale`, `ebt_cash`, `refund_sale`, `void_sale`, and `settle_batch_out`.

### 4. Printing
Printing is handled in `mainFunc.py` using the `printer` class. It uses the `escpos` library to send raw commands to USB thermal printers.

---

## 🆕 Adding Features

### Adding a New Screen
1. Create a new Python file in `kivyScripts/` (e.g., `myNewScreen.py`).
2. Define the screen class inheriting from `Screen`.
3. Update `main.py` to import and add the new screen to the `ScreenManager` (variable `sm`).
4. Add the UI layout in `posapp.kv`.

### Database Changes
1. Modify the relevant script in `databaseScripts/`.
2. Ensure you handle `CREATE TABLE IF NOT EXISTS` for new tables.
3. Update `mainFunc.py` if global data mapping is required.

---

## 📝 Troubleshooting & Logging

- **Kivy Logs:** Saved in `logsKivy/`. Configured in `main.py`.
- **Application Errors:** Logged to `errorLog`.
- **Database Issues:** If the database becomes corrupt, you can use the `reset__()` function in `mainFunc.py` to archive the current data and start fresh (Caution: This deletes current transaction data).

---

## 📜 License
This project is licensed under the MIT License - see the `LICENSE` file for details.
