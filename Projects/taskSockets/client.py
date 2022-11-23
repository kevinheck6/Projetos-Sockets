import socket
import time
import threading

report_number = 0
temp_limit = 80
energy_limit = 10
humidity_limit = 20
alarm_frequency = 5


def check_limits(value, type):
    global temp_limit
    global energy_limit
    global humidity_limit

    if type == "temperature":
        if int(value) > temp_limit:
            print(f"Throw water in the system!! The temperature is equal to {value}! It's on fire!")
    elif type == "humidity":
        if int(value) > humidity_limit:
            print(f"You threw too much water!! The humidity is equal to"
                  f" {value}%! You want the electric system to blow?!?")
    elif type == "energy":
        if int(value) < energy_limit:
            print(f"We are almost out of energy! We only have {value}% left! Do something!!")

    elif type == "change_temperature":
        temp_limit = int(value)
    elif type == "change_energy_limit":
        energy_limit = int(value)
    elif type == "change_humidity_limit":
        humidity = int(value)

    elif type == "people":
        if value == "False":
            print(f"There are no People taking care of the system!")

    elif type == "door":
        if value == "False":
            print(f"There are no doors open in the system!")

    else:  # Error case
        print("There is no command with such name")


def send_tick():
    global report_number
    report_number = report_number + 1
    print("Report number: " + str(report_number))
    print(time.ctime())
    alarm_tick = "alarm_tick"
    server.send(str(alarm_tick).encode())  # sending alarm tick to server

    info = server.recv(1024).decode()
    temp, energy, humidity, people, door = info.split(' ')
    check_limits(temp, "temperature")
    check_limits(energy, "energy")
    check_limits(humidity, "humidity")
    check_limits(people, "people")
    check_limits(door, "door")


def normal():
    global alarm_frequency
    global flag
    while flag == 1:

        send_tick()
        print(" ")
        print('Preparing new reports! wait for a few seconds...')
        print('#############################')
        time.sleep(alarm_frequency)
        if not flag:
            print('#####################################')


def get_input():
    global flag
    keystrk = input('Press a key to stop \n')
    # thread doesn't continue until key is pressed
    print('You are no longer monitoring the server')
    print(' ')
    flag = False
    main_menu()


def run_automatically():
    # set global variable flag
    global flag
    flag = 1

    n = threading.Thread(target=normal)
    i = threading.Thread(target=get_input)
    n.start()
    i.start()


def limits_change():
    user_input = input('')
    if user_input == "1":
        print("What is the new Temperature limit would you like the system to have?")
        user_input = input('')
        if user_input.isnumeric():
            check_limits(user_input, "change_temperature")
            main_menu()
        else:
            print("Sorry but this parameter is not a number, choose a new command between: ")
            print("1. temperature, 2. humidity, 3. energy")
            limits_change()

    if user_input == "2":
        print("What is the new Humidity limit would you like the system to have?")
        user_input = input('')
        if user_input.isnumeric():
            check_limits(user_input, "change_humidity_limit")
            main_menu()
        else:
            print("Sorry but this parameter is not a number, choose a new command between: ")
            print("1. temperature, 2. humidity, 3. energy")
            limits_change()

    if user_input == "3":
        print("What is the new energy limit would you like the system to have?")
        user_input = input('')
        if user_input.isnumeric():
            check_limits(user_input, "change_energy_limit")
            main_menu()
        else:
            print("Sorry but this parameter is not a number, choose a new command between: ")
            print("1. temperature, 2. humidity, 3. energy")
            limits_change()

    else:
        print("We are sorry to inform but this is not a vallid command. Please try one of the following commands:")
        print("1. temperature, 2. humidity, 3. energy")
        limits_change()


def alarm_change():
    global alarm_frequency
    print("Would you like to set alarm frequency to what value?(In seconds)")
    user_input = input('')
    if user_input.isnumeric():
        alarm_frequency = int(user_input)
        main_menu()
    else:
        print("Your input is not a number, please try once more.")
        alarm_change()


def main_menu():
    print("You are in the Menu now. Choose what option you want to run:")
    print("1. Change the limits of the alarm to a new value")
    print("2. Start the automatic alarm")
    print("3. Change the alarm time to a new value")
    print("4. Close the server")

    user_input = input('')

    if user_input == "1":
        print("What variable limit for the alarm would you like to change? Choose from the following:")
        print("1. temperature, 2. humidity, 3. energy")
        limits_change()

    if user_input == "2":
        print("Instructions:")
        print(
            "To make the alarm stop immediately you just have to write anything in the terminal and u will go back to "
            "menu")
        print(" ")
        print(
            f"The temperature alarm is going to alert you if the temperature is above the threshold of : {temp_limit},")
        print(f" the for the humidity above: {humidity_limit}, the energy bellow: {energy_limit} ")
        print(f" and if there is no one in the server and if there are no doors open")
        print("The alarm reports are going to start in 15 seconds!")
        time.sleep(15)
        print(" ")
        print("########################")
        run_automatically()

    if user_input == "3":
        alarm_change()

    if user_input == "4":
        print("Thanks for using this service. We are closing the connection now!")
        server.send(str("close").encode())
        server.close()

    if not user_input.isnumeric():
        print("This command is not available, please try a different one in 2 seconds.")
        time.sleep(2)
        print("###############################")
        main_menu()


server = socket.socket()
print("Socket created successfully.")

# Defining port and host
port = 8800
host = 'localhost'

# Connect socket to the host and port
server.connect((host, port))
print('Connection Established.')

main_menu()
