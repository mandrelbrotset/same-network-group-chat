# same-network-group-chat
GUI group chat for computers in the same network. Multiple clients can be created on a single computer. After starting the server. Clients can connect to the server. Clients connected to a server will be able to send broadcast messages to other clients connected to that server. Both the server program and client program are GUI based.

## Dependency
* PyQt5

## Starting the group chat
* Start the server by running """python3 server_app.py""" in a terminal or command prompt.
* Leave the fields in the server program empty to use default configurations.
* Click "start server".
* Create a client by running """python3 client_app.py""" in a terminal or command prompt.
* In the client program enter a nickname to be seen by other clients when you send messages.
* If the client programs will be running on the same machine as the server, leave the hostname field blank othereise enter the IP address of tge computer running the server.
* Leave other fields blank if you didn't enter a port number in the server program.
* Click "Connect to server".
* Perform steps 4 to 9 to create multiple clients.


## First run of server_app.py
![server_first_run](https://user-images.githubusercontent.com/24194821/40284377-0d6782fa-5c54-11e8-8c52-17fa2094a60d.png)

## Server running
![server_started](https://user-images.githubusercontent.com/24194821/40284418-a762e9a8-5c54-11e8-9fc1-e9fcd306e82e.png)

## First run of client_app.py
![client_first_run](https://user-images.githubusercontent.com/24194821/40284425-c1e3ad1c-5c54-11e8-9cce-9c304e11bded.png)

## Client about to connect
![server_client_running](https://user-images.githubusercontent.com/24194821/40284465-3ab47d52-5c55-11e8-9252-e61449d587c6.png)

## One user connected
![single_user_connected](https://user-images.githubusercontent.com/24194821/40284454-1c9b56b0-5c55-11e8-9841-826630e9488b.png)

## Multiple users connected
![mulptiple_users_connected](https://user-images.githubusercontent.com/24194821/40284468-3e16d968-5c55-11e8-86ef-8a9bd7571b23.png)
