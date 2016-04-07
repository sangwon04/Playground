import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tells the server to listen on bind_ip IP on bind_port port
server.bind((bind_ip, bind_port))

# Tells the server to start listening w/ a max backlog of connections set to 5
server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip, bind_port)

# This is our client-handling thread
def handle_client(client_socket):
    # Print out what the client sends
    request = client_socket.recv(1024)

    print "[*] Received: %s" % request

    # Send back a packet
    client_socket.send("ACK!")

    client_socket.close()

while True:
    # When a client connects, set the client var with the client socket and addr
    # with the remote connection details.
    # The server.accept() function returns (conn, address) where conn is a new
    # socket object usable to send/receive data on the connection, and address
    # is the address bound to the socket on the other side of the conn.
    client, addr = server.accept()

    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

    # Spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
