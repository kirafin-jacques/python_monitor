import sys

from python_monitor.pywinrm_monitor import check_with_pywinrm

os_type = sys.platform
if os_type == "win32":
    from python_monitor.wmi_monitor import check_with_paramiko
    
print(f"OS : {os_type}")


# List of Windows servers to monitor
windows_servers = [
        {"host":"192.168.16.147","username":"adminstrator","password":"bct2bnco#"},
        {"host":"192.168.2.199","username":"adminstrator","password":"bct1bnco#"}
    ]

for creds in windows_servers:
    if os_type == "linux":
        check_with_pywinrm(creds)
    elif os_type == "win32":
        check_with_paramiko(creds)


    
