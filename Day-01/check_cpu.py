import psutil
#apko kaam krna h ky user sy CPU thershold lo
# current cpu usage ka pta kro
# agr cpu usage threshold sy zyada huwa to email kr do admin ko

def check_cpu_threshold():
        cpu_threshold = int(input("Enter CPU Threshold (%): "))
        
        current_cpu = psutil.cpu_percent(interval=1)
        print(f"Current CPU % Usage: {current_cpu}%")
        
        if current_cpu > cpu_threshold:
            print("CPU Alert Email Sent...")
        else:
            print("CPU usage is within the threshold.")
            
check_cpu_threshold()