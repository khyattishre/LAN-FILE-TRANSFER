
import socket
import os
import threading
import struct

HOST = "0.0.0.0"
PORT = 5000

SAVE_FOLDER = "server_files"
os.makedirs(SAVE_FOLDER, exist_ok=True)


def handle_client(client, address):
    print(f"\nClient connected: {address}")

    try:
        # Receive the complete 4-byte filename length
        header = b""

        while len(header) < 4:
            chunk = client.recv(4 - len(header))
            if not chunk:
                print("Filename header was not received completely.")
                return
            header += chunk

        name_length = struct.unpack("!I", header)[0]

        if name_length == 0 or name_length > 1024:
            print("Invalid filename length.")
            return

        # Receive the complete filename
        name_bytes = b""

        while len(name_bytes) < name_length:
            chunk = client.recv(name_length - len(name_bytes))
            if not chunk:
                print("Filename was not received completely.")
                return
            name_bytes += chunk

        file_name = name_bytes.decode("utf-8")

        # Prevent directory paths from being used as filenames
        if os.path.basename(file_name) != file_name:
            print("Invalid filename.")
            return

        print(f"Receiving file: {file_name}")

        # Tell the client the server is ready
        client.sendall(b"READY")

        file_path = os.path.join(SAVE_FOLDER, file_name)

        # Receive and save the file data
        with open(file_path, "wb") as file:
            while True:
                data = client.recv(4096)

                if not data:
                    break

                file.write(data)

        print("File received successfully!")
        print(f"Saved at: {file_path}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client.close()
        print(f"Client disconnected: {address}")


# Create the TCP server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print("===================================")
print("       LAN FILE TRANSFER SERVER")
print("===================================")
print(f"Server listening on port {PORT}")
print("Waiting for clients...")
print("Press Ctrl+C to stop the server.\n")

try:
    while True:
        client, address = server.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(client, address),
            daemon=True
        )
        thread.start()

        print(f"Client handler started for {address}")

except KeyboardInterrupt:
    print("\nServer stopped.")

finally:
    server.close()
