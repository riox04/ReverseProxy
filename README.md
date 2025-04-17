# Reverse Proxy Server

A simple JSON-based reverse proxy implemented in Python using the standard `socket` and `json` modules. This setup allows a client to send a payload through the proxy to a backend server and receive a response.

---

## Prerequisites

- Python 3.8 or higher
- No external packages required (all dependencies are part of the Python standard library)

---

## How to Run

1. Open three separate terminals.
2. In **Terminal 1**, start the **server**:
   ```bash
   python server.py
   ```
3. In **Terminal 2**, start the **reverse proxy**:
   ```bash
   python proxy.py
   ```
4. In **Terminal 3**, start the **client**:
   ```bash
   python client.py
   ```
5. When prompted by the client, enter the message you want to send.
6. Observe the message flow: **Client → Proxy → Server → Proxy → Client**.

---

## Communication Flow

### Client → Proxy

1. Serialize Python object to JSON string: `json.dumps()`
2. Encode JSON string to bytes: `.encode()`
3. Send bytes over the socket

### Proxy → Server

1. Receive bytes over the socket
2. Decode bytes to string: `.decode()`
3. Deserialize JSON string to Python object: `json.loads()`

### Server → Proxy (Response)

1. Serialize Python object to JSON string: `json.dumps()`
2. Encode JSON string to bytes: `.encode()`
3. Send bytes back to proxy

### Proxy → Client (Final Response)

1. Receive bytes from server
2. Decode bytes to string: `.decode()`
3. Deserialize JSON string to Python object: `json.loads()`
4. Send response back to client

---

## Key Functions

| Function            | Description                                                              |
|---------------------|--------------------------------------------------------------------------|
| `json.dumps()`      | Convert a Python object (dict, list, etc.) into a JSON-formatted string |
| `.encode()`         | Convert a string into bytes (default UTF-8 encoding)                    |
| `.decode()`         | Convert bytes back into a string                                        |
| `json.loads()`      | Parse a JSON-formatted string into a Python object                       |

```python
# Example: sending a request to the server
dict_as_json  = json.dumps(request_dict)
json_as_bytes = dict_as_json.encode()
server_socket.sendall(json_as_bytes)
```

> **Note:** Socket communication only handles bytes, not strings. Always encode before sending.

---

## TODO

- Add multithreading support (using `threading` or `concurrent.futures`)
- Support multiple backend servers (server pool)

