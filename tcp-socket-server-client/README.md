tcp-socket-server-client
Simple Python TCP server and client scripts for learning socket programming. Inspired by Black Hat Python.

TCP Sockets
This repository contains simple Python scripts for a basic TCP server and client, created as part of my learning journey through Black Hat Python.

The server accepts incoming TCP connections, prints received data, and responds with an acknowledgment (ACK). The client connects to the server and sends a simple message.

These scripts demonstrate low-level socket programming using Python's built-in socket and threading modules.

Files
TCP_server.py – Listens for incoming TCP connections on a specified port and handles each client in a separate thread.
TCP_client.py – Connects to the server, sends a message, and prints the server's response.
Requirements
Python 3.x
No external dependencies
Usage
Run the server:

python TCP_server.py

## 🖥️ Demo

Here’s a live run of the TCP server and client:

![Demo](demo.png)
