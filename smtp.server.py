# smtp_server.py
# Group #2: Clarissa Morales, Jonathan Vergonio, Kalyan Fernande, Adam Wang
from socket import *

# Set server address and port
serverAddress = ('localhost', 3525)

# Create socket and bind to the server address
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(serverAddress)
serverSocket.listen(1)

print("SMTP Server is running on port 1025...")

while True:
    # Accept a new client connection
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection established with {addr}")

    # Send 220 Service ready message
    connectionSocket.send(b"220 localhost SMTP Server Ready\r\n")

    # Handle HELO command
    recv = connectionSocket.recv(1024).decode()
    print(f"Client: {recv.strip()}")
    if recv.startswith("HELO"):
        connectionSocket.send(b"250 Hello Alice\r\n")

    # Handle MAIL FROM command
    recv = connectionSocket.recv(1024).decode()
    print(f"Client: {recv.strip()}")
    if recv.startswith("MAIL FROM"):
        connectionSocket.send(b"250 OK\r\n")

    # Handle RCPT TO command
    recv = connectionSocket.recv(1024).decode()
    print(f"Client: {recv.strip()}")
    if recv.startswith("RCPT TO"):
        connectionSocket.send(b"250 OK\r\n")

    # Handle DATA command
    recv = connectionSocket.recv(1024).decode()
    print(f"Client: {recv.strip()}")
    if recv.startswith("DATA"):
        connectionSocket.send(b"354 End data with <CRLF>.<CRLF>\r\n")

    # Receive the message data and end it with a period (.)
    data = connectionSocket.recv(1024).decode()
    print(f"Message data: {data.strip()}")
    connectionSocket.send(b"250 OK Message received\r\n")

    # Handle QUIT command
    recv = connectionSocket.recv(1024).decode()
    print(f"Client: {recv.strip()}")
    if recv.startswith("QUIT"):
        connectionSocket.send(b"221 Bye\r\n")

    # Close the connection with the client
    connectionSocket.close()
