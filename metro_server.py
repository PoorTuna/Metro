import socket
from functions import *

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 27020))
server_socket.listen(1)

client_socket, client_ip_address = server_socket.accept()

# Variables:
# Request_Type => 1 = login / 0 = Register
login_attempts = 0
logged = False
USER_DATA = "user_data.data"
while True:  # Temporary until threads will be initialized:
    request_type = client_socket.recv(1)

    # HANDLE LOGIN REQUEST:
    if request_type == "1":
        login_info = client_socket.recv(1024)
        # Should receive with USERNAME;PASSWORD format! will be decoded in server side.

        login_info = login_info.split(";")

        print "Login attempt from : " + client_ip_address[0] + " : "
        print login_info

        # Convenient variables:
        name = login_info[0]
        password = login_info[1]

        if check_name_pass(name,password,USER_DATA,0) and (name != "" and password != ""):
            logged = True

        if login_attempts <= 5:
            if logged:
                login_attempts = 0
                client_socket.send("1") #Logged On! CALL FUNCTION TO CHANGE SCREEN!
            else:
                login_attempts += 1
                client_socket.send("0") # Invalid Credentials!
                logged = False
        else:
            client_socket.send("Too many login attempts! Please try again later...")

    # HANDLE REGISTER REQUEST:
    elif request_type == "0":
        register_info = client_socket.recv(1024)
        # Should receive with EMAIL;USERNAME;PASSWORD format! will be decoded in server side.

        register_info = register_info.split(";")
        # Convenient variables:
        email = register_info[0]
        name = register_info[1]
        password = register_info[2]
        if len(name) <= 3 or password == "" or not check_mail(email) or name.isdigit() or not check_name_pass(name,
                                                                                                              password,
                                                                                                              USER_DATA,
                                                                                                              1):
            client_socket.send("A user with that name already exists! POPUP FUNCTION")
        else:
            client_socket.send("Creating new account!")

            with open(USER_DATA, "a") as file_handle:
                file_handle.write(email + ";" + name + ";" + password)

    # HANDLE INVALID REQUEST:
    else:
        client_socket.send("Illegal Request!")
        client_socket.close()
