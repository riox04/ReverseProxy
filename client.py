import socket
import json

def start_client():
    try:
        # Connect to the reverse proxy 
        client_socket = socket.socket()
        client_socket.connect(('localhost', 8080))  

        message_dict = {
            "code": 0,
            "payload": "The lion ____ anyon who speaks!"
        }
        
        client_socket.sendall(json.dumps(message_dict).encode())
        
        # Wait to receive the response from the proxy
        response_data = client_socket.recv(1024).decode()
        if response_data:
            # Convert the JSON string back to a Python dictionary
            response_dict = json.loads(response_data)
            print("Response received from proxy:")
            print(json.dumps(response_dict, indent=4))
        else:
            print("No response received.")
            
    except Exception as e:
        print(f"Error in client: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
