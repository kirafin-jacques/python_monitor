import winrm

def check_with_pywinrm(creds):
    """
    Connects to a Windows server using WinRM and checks the uptime.
    """
    try:
        ip = creds["host"]
        username = creds["username"]
        password = creds["password"]
        print(f"Checking Windows Server: {ip}")
        # Establish a session with the Windows server
        session = winrm.Session(f'http://{ip}:5985/wsman', auth=(username, password), transport='ntlm')

        # PowerShell command to get the system uptime
        ps_script = "Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object LastBootUpTime"
        result = session.run_ps(ps_script)

        if result.status_code == 0:
            output = result.std_out.decode('utf-8').strip()
            print(f"Server {ip} is up. Last boot time: {output}")
        else:
            print(f"Failed to check server {ip}. Error: {result.std_err.decode('utf-8').strip()}")

    except Exception as e:
        print(f"Error connecting to server {ip}: {str(e)}")