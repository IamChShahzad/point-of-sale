# 📘 Development Guide - Retail POS System

Welcome to the development guide for the Retail POS System. This document provides technical insights into the architecture, state management, and guidance for extending the system's functionality.

---

## 🏗️ System Architecture

The project is structured with a modular approach to separate core concerns, following a controller-like pattern where `src/core/logic.py` mediates between the UI and data persistence.

### 🖼️ Presentation Layer (`src/ui/`)
- Handles all user-facing interactions.
- Built using **Kivy** for the application engine and **KivyMD** for a modern, Material Design aesthetic.
- Screens are managed by the `ScreenManager` (defined in `src/ui/screenManager.py`).

### ⚙️ Business Logic (`src/core/`)
- `logic.py` contains the core functional workflows such as generating receipts, ending shifts, and managing the application's persistent state.
- Handles hardware communication (Thermal Printer via ESC/POS).

### 🗄️ Persistence Layer (`src/database/`)
- Encapsulates interaction with SQLite3 databases.
- Modules such as `inventory.py`, `shifts.py`, and `transactions.py` provide a clean API for CRUD operations, insulating the rest of the app from raw SQL logic.

---

## 💾 State & Configuration

### 1. Global State (`variable.txt`)
The application uses a persistent file `variable.txt` to store runtime configuration. This enables the system to recover its state (e.g., store info, current shift, printer IDs) after a restart.

- **`data`**: Store metadata (Name, Address, Phone).
- **`shift`**: Tracking for the current active shift.
- **`tabs`**: Configuration for quick-access retail buttons.
- **`printerSettings`**: USB Vendor and Product IDs for the hardware connection.

### 2. Databases (`data/`)
SQLite databases are used for local data storage:
- `inventory.db`: Tracks products, categories, tax, and stock.
- `transactions.db`: Historical record of all sales and refunds.
- `shifts.db`: Detailed logs of shift duration and activities.

---

## 🛠️ Developer Workflows

### Adding a New UI Screen
1. Create a new class inheriting from `Screen` or `MDScreen` in `src/ui/`.
2. Define the screen's layout in `src/assets/posapp.kv`.
3. Register the new screen in the `posApp.build` method within `main.py`.
4. Trigger navigation using `sm.current = "your_screen_name"`.

### Database Schema Updates
1. Modify the relevant module in `src/database/`.
2. Use `CREATE TABLE IF NOT EXISTS` to ensure seamless updates for existing installations.
3. Update any relevant data models or summary logic in `src/core/logic.py`.

### Logging & Debugging
- **Kivy Internal Logs:** Located in `logs/` (configured via `Config.set` in `main.py`).
- **Application Errors:** Captured manually in `logs/error.log`.
- **Reset Utility:** The `reset__()` function in `logic.py` can be used to archive current data and re-initialize the environment for testing purposes.

---

## 🤝 Contribution Guidelines
- Ensure all new features include appropriate error handling and logging.
- Maintain the modular structure—keep database logic separate from UI events.
- Update the `README.md` if existing setup instructions or features change.
