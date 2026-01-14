# ✅ Day-01 Task: System Health Monitoring with Python
### Python for DevOps – AI Edition
---
## 👋 Welcome
This task marks the **first practical step** in the *Python for DevOps* journey.  
Here, we use Python to monitor **system health metrics** — a core responsibility of every DevOps engineer.

This task is **beginner-friendly**, clean, and focused on building the **right DevOps mindset**.
---
## 🎯 Task Goal
The objective of this task is to:

- Take threshold values from the user
- Fetch real-time system metrics
- Compare metrics with thresholds
- Display alerts directly in the terminal

This simulates **basic monitoring logic** used in real production environments.
---
## 🛠️ Tools & Technologies
- Python 3
- psutil library
- Terminal / PowerShell
- Git & GitHub

---
Task/

├── system_health.py

└── README.md

---

## 🧠 What This Script Does
The script performs the following steps:

1. Takes user-defined thresholds for:
   - CPU usage
   - Memory usage
   - Disk usage
2. Fetches current system metrics using `psutil`
3. Compares each metric with its threshold
4. Prints:
   - ✅ OK message if usage is within limit
   - ⚠️ ALERT message if usage exceeds threshold

---

## ▶️ How to Run

### Step 1: Navigate to Task directory
```bash
cd Task
Step 2: Run the script
python system_health.py
Step 3: Enter threshold values when prompted
📊 Sample Output
Enter CPU Threshold (%): 50
Enter Memory Threshold (%): 70
Enter Disk Threshold (%): 80

--- System Health Status ---
CPU Usage: 30.4%
✅ CPU usage is within limit
---------------------------
Memory Usage: 73.0%
⚠️ ALERT: Memory usage crossed threshold!
---------------------------
Disk Usage: 32.5%
✅ Disk usage is within limit
