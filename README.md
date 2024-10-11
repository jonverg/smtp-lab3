# Simple SMTP Mail Client

Group #2: Clarissa Morales, Jonathan Vergonio, Kalyan Fernande, Adam Wang

## Overview:
This project consists of two Python files:
1. **`smtp_server.py`**: A simple SMTP server that listens for email messages, processes basic SMTP commands, and prints the message content to the console.
2. **`smtp_client.py`**: A basic SMTP client that connects to the server, sends email commands, and transmits a message.

## Example Workflow:
1. Run `smtp_server.py` in one terminal.
2. Run `smtp_client.py` in another terminal.
3. Observe the client sending commands and the server responding and printing the message to the console.

## How to Run Each File:

### 1. Running the SMTP Server (`smtp_server.py`)
   The server listens on `localhost` and a specified port (e.g., **3525** or any other port you choose).
   
   **Steps**:
   1. Open a terminal.
   2. Run the following command:
      ```bash
      python smtp_server.py
      ```
   3. The server will start listening for incoming connections and handle SMTP commands (`HELO`, `MAIL FROM`, `RCPT TO`, `DATA`, `QUIT`).

   **What It Does**:
   - The server accepts connections from an SMTP client.
   - It processes the standard SMTP commands and prints the received email message to the console.
   - It sends appropriate responses to the client after each command.

### 2. Running the SMTP Client (`smtp_client.py`)
   The client connects to the local SMTP server running on `localhost` and the specified port (e.g., **3525**).

   **Steps**:
   1. Open another terminal.
   2. Make sure the server is already running.
   3. Run the following command:
      ```bash
      python smtp_client.py
      ```
   4. The client will send SMTP commands to the server, including an email message.

   **What It Does**:
   - The client connects to the server.
   - It sends the following commands in sequence: `HELO`, `MAIL FROM`, `RCPT TO`, `DATA`, and `QUIT`.
   - It transmits a simple message ("I love computer networks!") and receives server responses after each command.

## Changing the Port:
Both the server and client default to using port **3525**. If you'd like to change the port:
  1. In `smtp_server.py`, change the port in:
     ```python
     serverAddress = ('localhost', <your_port>)
     ```
  2. In `smtp_client.py`, change the port in:
     ```python
     mailserver = ('localhost', <your_port>)
     ```

