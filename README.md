# ReverseProxy
 Reverse Proxy Server

### The working:

- json.dumps: Converts a Python object (like a dictionary, list, or string) into a JSON string.

- .encode(): Converts a string into bytes using the specified encoding (default is UTF-8). 

- .decode(): Converts bytes back into a string

- json.loads(): Converts a JSON string into a Python dictionary (or other corresponding Python data types like lists, strings, etc.).


        #sending the request to server
        #to understand
        # dict_as_json = json.dumps(json_dict)
        # json_as_bytes = dict_as_json.encode()
        # server_socket.sendall(json_as_bytes)


The socket communication can only handle bytes, not strings. 
So, we encode the JSON string into bytes before sending it over the socket.



General Flow in Network Communication (Socket):
Client → Proxy:
- Convert Python object to JSON string: json.dumps()
- Convert JSON string to bytes: .encode()
- Send bytes over the socket.

Proxy → Server:
- Receive bytes over the socket.
- Decode bytes to string: .decode()
- Convert JSON string to Python object: json.loads()

Server → Proxy (response):
- Convert Python object (response) to JSON string: json.dumps()
- Convert JSON string to bytes: .encode()
- Send bytes back to proxy.

Proxy → Client (final response):
- Receive bytes from server.
- Decode bytes to string: .decode()
- Convert JSON string to Python object: json.loads() (if needed)
- Send response back to client in the appropriate format.