import socket
import json

SERVER_HOST = 'localhost'
SERVER_PORT = 9000

def handle_client_proxy(client_conn):
    try:
        # Reading request from client
        req_json = client_conn.recv(1024).decode()  # bytes ->  string (JSON format)

        if not req_json:
            return
        
        # Convert JSON string to Python dict
        request_dict = json.loads(req_json)

        print("Message received from:")
        print(json.dumps(request_dict))  # Pretty print dict as JSON

        # Connect to backend server
        server_socket = socket.socket()
        server_socket.connect((SERVER_HOST, SERVER_PORT))

        # Send request to server (dict ->  JSON string ->  bytes)
        server_socket.sendall(json.dumps(request_dict).encode())

        # Receive response from server
        response_json = server_socket.recv(1024).decode()  # bytes -> string

        if not response_json:
            return

        print("Response from server:")
        print(response_json)

        # Send response back to client
        client_conn.sendall(response_json.encode())  # it's already a JSON string, no need for dumps()

        server_socket.close()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_conn.close()


def start_proxy():
    proxy_socket = socket.socket()
    proxy_socket.bind(('0.0.0.0', 8080))
    proxy_socket.listen(5)
    print("Reverse Proxy Server is running on port 8080...")
    while True:
        c, addr = proxy_socket.accept() #c is a new socket object 
        print(f"Accepted connection from {addr}")
        handle_client_proxy(c)

if __name__ == "__main__":
    start_proxy()