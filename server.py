import socket 
import json

HOST = 'localhost'
PORT = 9000

def handle_connection(conn):
    try:
        req_data = conn.recv(1024).decode()  
        if not req_data:
            return
        
        request_dict = json.loads(req_data)
        print("Message received from proxy:\n", request_dict["payload"])

        response_dict = {
            "code": 200,
            "payload": "Hello from the server!"
        }

        # Send response back as dict -> JSON string -> bytes
        conn.sendall(json.dumps(response_dict).encode())

    except Exception as e:
        print(f"Error processing connection: {e}")
    finally:
        conn.close()

def start_server():
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server is running on {HOST}:{PORT}...")
    
    while True:
        c, addr = server_socket.accept()
        #print(f"Accepted connection from {addr}")
        handle_connection(c)

if __name__ == "__main__":
    start_server()
