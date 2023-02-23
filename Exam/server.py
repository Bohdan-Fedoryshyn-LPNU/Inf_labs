import socket

# Define server host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 443

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(1)
print(f'Server listening on {SERVER_HOST}:{SERVER_PORT}')

while True:
    # Accept incoming connections
    client_connection, client_address = server_socket.accept()
    print(f'New connection from {client_address[0]}:{client_address[1]}')

    # Receive the client's HTTP request
    request = client_connection.recv(1024).decode()
    print(f'Received request:\n{request}')

    # Send a response back to the client
    response = 'HTTP/1.0 200 OK\nContent-Type: text/html\n\nHello, world!'
    client_connection.sendall(response.encode())

    # Close the connection
    client_connection.close()