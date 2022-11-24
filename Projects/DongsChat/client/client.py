import threading
import socket


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 7777))
    except:
        return print('\nError: It was not possible to connect with the server!\n')

    username = input('User> ')
    print('\nConnected to server')

    thread1 = threading.Thread(target=receive_messages, args=[client])
    thread2 = threading.Thread(target=send_messages, args=[client, username])

    thread1.start()
    thread2.start()


def receive_messages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg + '\n')
        except:
            print('\nError: it was not possible to stay in connection with the server!\n')
            print('Press <Enter> to continue...')
            client.close()
            break


def send_messages(client, username):
    while True:
        try:
            msg = input('\n')
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        except:
            return


main()