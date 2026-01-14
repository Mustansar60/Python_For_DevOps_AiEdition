📂 Files in This Task
Task/
│
├── system_health.py
└── README.md

🧠 What the Script Does

The script performs the following steps:

Takes threshold values for:

CPU usage

Memory usage

Disk usage

Fetches current system usage using psutil

Compares usage with thresholds

Displays alerts if any threshold is crossed

▶️ How to Run the Script

1️⃣ Activate virtual environment (if any)

2️⃣ Navigate to Task folder:

cd Task


3️⃣ Run the script:

python system_health.py


4️⃣ Enter threshold values when prompted.

📊 Sample Output
Enter CPU Threshold (%): 50
Enter Memory Threshold (%): 70
Enter Disk Threshold (%): 80

--- System Health Status ---
CPU Usage: 30%
✅ CPU usage is within limit
---------------------------
Memory Usage: 73%
⚠️ ALERT: Memory usage crossed threshold!
---------------------------
Disk Usage: 32%
✅ Disk usage is within limit

🧩 Concepts Covered

User input handling

Conditional statements (if / else)

Python functions

for-loops

System monitoring basics

DevOps automation mindset

🚀 DevOps Perspective

This script is a foundation for:

Server monitoring

Alerting systems

Automation scripts

CI/CD health checks

In future tasks, this can be extended to:

Send email alerts

Monitor continuously

Run as a cron job

Integrate with Slack or cloud servers

✅ Task Status

✔️ Task completed successfully
✔️ Output visible in terminal
✔️ Beginner-friendly and clean code

👨‍💻 Author

Mustansar Maqsood
Python for DevOps – AI Edition

🔥 Next Step

After this task, we move towards:

Logging

File handling

Email alerts

Advanced automation
