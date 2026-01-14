import psutil

def check_system_health():
    # Taking thresholds from user
    cpu_threshold = int(input("Enter CPU Threshold (%): "))
    memory_threshold = int(input("Enter Memory Threshold (%): "))
    disk_threshold = int(input("Enter Disk Threshold (%): "))

    print("\n--- System Health Status ---")

    # Fetching system metrics
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    # Storing metrics in dictionary (for loop use)
    metrics = {
        "CPU": (cpu_usage, cpu_threshold),
        "Memory": (memory_usage, memory_threshold),
        "Disk": (disk_usage, disk_threshold)
    }

    # Comparing metrics with thresholds
    for name, (usage, threshold) in metrics.items():
        print(f"{name} Usage: {usage}%")

        if usage > threshold:
            print(f"⚠️ ALERT: {name} usage crossed threshold!")
        else:
            print(f"✅ {name} usage is within limit.")

        print("---------------------------")

# Calling the function
check_system_health()
