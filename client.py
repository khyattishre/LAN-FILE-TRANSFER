
import socket
import os
import struct

HOST = input("Enter server IP address (127.0.0.1 for same laptop): ").strip()
PORT = 5000

print("===================================")
print("       LAN FILE TRANSFER CLIENT")
print("===================================")

file_path = input("Enter the full path of the file to send: ").strip().strip('"')

if not os.path.isfile(file_path):
    print("File not found! Check the path and try again.")
    raise SystemExit

file_name = os.path.basename(file_path)
name_bytes = file_name.encode("utf-8")

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print("Connected to server!")

        # Send filename length, then filename
        client.sendall(struct.pack("!I", len(name_bytes)))
        client.sendall(name_bytes)

        # Wait for server readiness
        response = client.recv(5)

        if response != b"READY":
            print("Server did not accept the file.")
            raise SystemExit

        print(f"Sending file: {file_name}")

        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                client.sendall(data)

        print("File sent successfully!")

except ConnectionRefusedError:
    print("Could not connect. Make sure server.py is running.")

except OSError as e:
    print(f"Network error: {e}")

print("Connection closed.")
