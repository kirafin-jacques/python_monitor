import wmi
 

# Function to monitor CPU usage on a remote Windows server
def check_with_wmi(creds):
    hostname = creds["host"]
    username = creds["username"]
    password = creds["password"]
    conn = wmi.WMI(hostname, user=username, password=password)
    cpu_usage = conn.Win32_Processor()[0].LoadPercentage
    return cpu_usage