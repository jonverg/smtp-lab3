# smtp_client.py
# Group #2: Clarissa Morales, Jonathan Vergonio, Kalyan Fernande, Adam Wang
from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (localhost SMTP server for testing)
mailserver = ('localhost', 3525)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(f"Server: {recv}")
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(f"Server: {recv1}")
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
mailFrom = 'MAIL FROM:<alice@localhost>\r\n'
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(f"Server: {recv2}")
if recv2[:3] != '250':
    print('250 reply not received from server after MAIL FROM.')

# Send RCPT TO command and print server response.
rcptTo = 'RCPT TO:<bob@localhost>\r\n'
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print(f"Server: {recv3}")
if recv3[:3] != '250':
    print('250 reply not received from server after RCPT TO.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(f"Server: {recv4}")
if recv4[:3] != '354':
    print('354 reply not received from server after DATA.')

# Send message data.
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(f"Server: {recv5}")
if recv5[:3] != '250':
    print('250 reply not received from server after sending message.')

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(f"Server: {recv6}")
if recv6[:3] != '221':
    print('221 reply not received from server after QUIT.')

# Close the connection
clientSocket.close()
