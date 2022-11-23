import os
import socket
from os import listdir
from os.path import isfile, join


def transfer():
    print(file_names)
    client.send(str(file_names).encode())  # server is sending file names
    data = client.recv(1024).decode()  # server is receiving the file name that he should send back
    path = "files/" + data
    print(data)
    client.send(str(os.path.getsize(path)).encode())  # sending the file size
    return path


# Initialize Socket Instance
server = socket.socket()
print("Socket created successfully.")

# Defining port and host
port = 8800
host = ''

# binding to the host and port, that`s what define it as a server
server.bind((host, port))

# Accepts up to 100 connections
server.listen(100)
print('Socket is listening...')

while True:
    # Establish connection with the clients.
    client, addr = server.accept()
    print('Connected with ', addr)

    # Files names
    file_names = [f for f in listdir("files") if isfile(join("files", f))]

    done = "False"
    while done == "False":
        path = transfer()  # getting the final path from function
        done = client.recv(1024).decode()  # getting the verification that the loop is over
        print(done)

    # Read File in binary
    file = open(path, 'rb')
    line = file.read(1024)

    # Keep sending data to the client
    while line:
        client.send(line)  # 3 Sending

        line = file.read(1024)

    file.close()
    print('File has been transferred successfully.')

    client.close()
