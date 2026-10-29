<<<<<<< HEAD

# File Transfer Over LAN Using Python

## Project Overview
This project transfers files between a client and a server using Python TCP sockets. The server receives files and stores them in a folder named server_files.

## Technologies Used
- Python
- TCP/IP
- Socket programming
- Multithreading

## Features
- Client-server communication
- Reliable file transfer using TCP
- Transfer of different files
- File storage on the server
- Thread-based handling of multiple client connections

## Project Files
- server.py: Receives and saves files.
- client.py: Connects to the server and sends files.
- test.txt: Sample file for testing.
- test2.txt: Second sample file.
- server_files/: Stores received files.

## How to Run

1. Open a terminal in the project folder.
2. Start the server:
   python server.py
3. Open another terminal.
4. Run the client:
   python client.py
5. Enter 127.0.0.1 as the server IP when testing on the same laptop.
6. Enter the full path of the file to send.

## Testing
The project was tested on one laptop using the loopback IP address 127.0.0.1. Multiple client connections were tested sequentially.

## Conclusion
The project demonstrates TCP communication, socket programming, file handling, and multithreading using Python.
=======
# LAN-FILE-TRANSFER
LAN-FILE-TRANSFER
>>>>>>> 23cc1cf84a80a603ba63d9a08f587a34190b8e83
