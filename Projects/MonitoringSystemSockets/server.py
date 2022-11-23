import random
import socket


def random_function(type):
    if type in ["energy", "humidity"]:
        number = random.randrange(0, 100, 1)

    elif type == "temp":
        number = random.randrange(-55, 150, 1)

    else:
        number = bool(random.getrandbits(1))

    print(number)
    return number


def check_commands():
    command = client.recv(1024).decode()
    if command == "alarm_tick":
        # print(str(random_function("energ")))

        info = str(random_function("temp")) + " " + str(random_function("energy")) + " " + \
               str(random_function("humidity")) + " " + str(random_function("people")) + " " + \
               str(random_function("door"))

        client.send(str(info).encode())

        check_commands()
    if command == "close":
        print("Closing connection")
        client.close()
        quit()


# Initialize Socket Instance
server = socket.socket()
print("Socket created successfully.")

# Defining port and host
port = 8800
host = ''

# binding to the host and port, that`s what define it as a server
server.bind((host, port))

# Accepts up to 100 connections
server.listen()
print('Socket is listening...')

while True:
    # Establish connection with the clients.
    client, addr = server.accept()
    print('Connected with ', addr)

    check_commands()
    client.close()
