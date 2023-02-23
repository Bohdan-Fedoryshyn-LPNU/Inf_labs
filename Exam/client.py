import http.client

# Define server host and port
SERVER_HOST = 'localhost'
SERVER_PORT = 433

# Create a connection to the server
connection = http.client.HTTPConnection(SERVER_HOST, SERVER_PORT)

# Send a GET request to the server
connection.request('GET', '/')

# Get the server's response
response = connection.getresponse()

# Print the response status code and body
print(f'Status: {response.status}')
print(f'Body:\n{response.read().decode()}')

# Close the connection
connection.close()