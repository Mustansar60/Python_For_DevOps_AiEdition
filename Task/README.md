📂 Project Structure
Task/
│
├── system_health.py   # Main monitoring script
└── README.md          # Task documentation

🧠 How the Script Works

The script follows these steps:

1️⃣ Asks the user to define threshold values for:

CPU usage

Memory usage

Disk usage

2️⃣ Collects real-time system metrics using psutil

3️⃣ Compares current usage with the given thresholds

4️⃣ Prints:

✅ Normal status if usage is within limit

⚠️ Alert message if usage exceeds the threshold

▶️ How to Run the Script
Step 1: Move into the Task directory
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

🧩 Concepts Covered

This task covers the following Python & DevOps concepts:

User input using input()

Conditional logic (if / else)

Python functions

for-loops

System monitoring basics

Automation mindset for DevOps

🔍 Why This Task Matters (DevOps Perspective)

In real DevOps environments:

Servers are continuously monitored

Alerts are triggered when thresholds are crossed

Automation scripts reduce manual work

👉 This script is a foundation for:

Server monitoring tools

Alerting systems

Health checks in CI/CD pipelines

🚀 Future Improvements

In upcoming tasks, this script can be extended to:

Send email alerts

Run continuously using loops

Log data to files

Monitor remote servers

Integrate with Slack or cloud platforms

✅ Task Status

✔️ Task completed successfully
✔️ Clean & readable code
✔️ Output visible in terminal
✔️ Beginner-friendly implementation

👨‍💻 Author

Mustansar Maqsood
Python for DevOps – AI Edition

🧭 What’s Next?

➡️ Day-02:

Logging

File handling

Better automation patterns

🔥 Last Step (Git)

After adding this README file:

git add Task/README.md
git commit -m "Added detailed README for Day-01 Task"
git push origin master
