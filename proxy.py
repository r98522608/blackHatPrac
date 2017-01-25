#/usr/lib/python2.7
import sys
import socket
import threading


def server_loop(local_host, local_port, remote_host,
                remote_port, receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((local_host, local_port))
    except:
        print ("""Failed to listen {0}:{1}!!
              Please try again!""".format(local_host, local_port))
        sys.exit(0)
    print ("-*- Listen on {0:16}:{1:5}".format(local_host, local_port))
    server.listen(5)

    while True:
        cli_socket, cli_addr = server.accept()
        print ("[==>]   Received incoming connection from {0:16}:{1:5}".format(cli_addr[0],
                                                                               cli_addr[1]))
        proxy_thread = threading.Thread(target = proxy_handler, args = (cli_socket, remote_host,
                                                                        remote_port, receive_first))
        proxy_thread.start()

def main():
    if len(sys.argv[1:]) != 5:
        print ("Usage: ./proxy.py [local_host] [local_port] [remote_host] [remote_port] [receive_first]")
        sys.exit(0)

    local_host = sys.argv[1]
    local_port = int(sys.argv[2])
    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])
    receive_first = sys.argv[5]

    if "True" or "true" in receive_first:
        receive_first = True
    else:
        receive_first = False

    server_loop(local_host, local_port, remote_host, remote_port, receive_first)

def proxy_handler(client_socket, remote_host, remote_port, receive_first):

    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))

    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)
        remote_buffer = response_to_handler(remote_buffer)
        if len(remote_buffer):
            print("[<==] Sending {0} bytes to local_host".format(len(remote_buffer)))
            client_socket.send(remote_buffer)

    while True:
        localbuffer = receive_from(client_socket)
        if len(localbuffer):
            print ("[==>] Received {0} bytes from local_host.".format(len(localbuffer)))
            hexdump(localbuffer)
            localbuffer = request_handler(localbuffer)
            remote_socket.send(localbuffer)
            print ("[==>] Sent to remote")

        remote_buffer = receive_from(remote_socket)


main()
