import socket


def transfer():
    file_names = server.recv(1024).decode('utf-8')  # getting files names from server
    print(f"The files that u can download are: {file_names}, which one would you like to download?")
    dl_file = input('')  # choosing file
    server.send(dl_file.encode())  # # sending name that should be downloaded
    file_size = server.recv(1024).decode('utf-8')  # getting file size from server
    print(f"The size of the file is: {file_size} bytes")
    print(f"Are you sure you want to download it? Type 'y' to download or 'n' to  exit")
    return dl_file


server = socket.socket()
print("Socket created successfully.")

# Defining port and host
port = 8800
host = 'localhost'

# Connect socket to the host and port
server.connect((host, port))
print('Connection Established.')

done = "False"
while done == "False":
    dl_file = transfer()  # getting the name of the file that should be downloaded
    confirmation = input('')  # confirmation that we should end the loop
    if confirmation == 'y':
        done = "True"
        server.send(str(done).encode())  # 2 sent 4
        break
    elif confirmation == 'n':
        done = "False"
        server.send(str(done).encode())  # 2 sent 4

# Write File in binary
file = open(dl_file, 'wb')

# Keep receiving data from the server
line = server.recv(1024)  # 3 received

while line:
    file.write(line)
    line = server.recv(1024)

print('File has been received successfully.')

file.close()
server.close()
print('Connection Closed.')
