# Access Verification and Logging System (Python)

This project is a simple Python-based access control system that simulates user verification, access levels, and logs activities.

## 📌 Features

- ✅ VIP and Normal user access checking
- 🔐 Clearance level validation
- 🤖 Human-check simulation
- 📄 Access result logging into `log.txt`
- 🧪 Easy testing via `Test.py`

## 🧠 How It Works

The system contains three main modules:

### 1. `Checker.py`
Defines the `User` class and includes methods to:
- Check VIP access code
- Validate clearance level
- Confirm if the user passed the human check

### 2. `System.py`
Contains the `system` class that:
- Uses a `User` object to perform checks
- Returns access level (0–3)
- Saves access attempts into `log.txt` using `message()`

### 3. `Test.py`
A testing script that:
- Creates sample `User` objects
- Passes them into the system
- Prints and logs access results

## 🚀 Getting Started

1. Clone this repo or download the files.
2. Make sure Python is installed on your device.
3. Run the following command:

```bash
python Test.py
```

## 📁 Files

- `Checker.py`: User access validation
- `System.py`: System logic and logging
- `Test.py`: Sample users and access attempts
- `log.txt`: Output log file (auto-generated)

## ✅ Example Output

```
mubarak   Access granted
tim       Access granted
kally     ALERT: Unauthorized access attempt!
phive     Access denied
joy       Access denied
```

## 📜 License

This project is open-source and free to use.

---

Created by Mubarak 🇳🇬
