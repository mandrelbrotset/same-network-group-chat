import socket
import threading

class Server(object):
    def __init__(self, hostname, port):
        self.clients = {}

        # create server socket
        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # start server
        self.tcp_server.bind((hostname, port))
        self.tcp_server.listen(5)

        print("[INFO] Server running on {}:{}".format(hostname, port))

        while True:
            connection, address = self.tcp_server.accept()
            nickname = connection.recv(1024)
            nickname = nickname.decode()
            self.clients[nickname] = connection

            # start a thread for the client
            threading.Thread(target=self.receive_message, args=(connection, nickname), daemon=True).start()

            print("[INFO] Connection from {}:{} AKA {}".format(address[0], address[1], nickname))


    def receive_message(self, connection, nickname):
        print("[INFO] Waiting for messages")
        while True:
            try:
                msg = connection.recv(1024)

                self.send_message(msg, nickname)
                print(nickname + ": " + msg.decode())
            except:
                connection.close()

                #remove user from users list
                del(self.clients[nickname])

                break

        print(nickname, " disconnected")


    def send_message(self, message, sender):
        if len(self.clients) > 0:
            for nickname in self.clients:
                if nickname != sender:
                    msg = sender + ": " + message.decode()
                    self.clients[nickname].send(msg.encode())


if __name__ == "__main__":
    port = 5555
    hostname = "localhost"

    chat_server = Server(hostname, port)