import socket

host=raw_input

#host='0.0.0.0'
port=80
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect((host, port))
mysocket.send(b'GET / HTTP/1.1\r\nHOST: test\r\n\r\n')
response = mysocket.recv(4096)
print(response)
