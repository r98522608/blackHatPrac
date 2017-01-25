def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # connect to our target host
        client.connect((target,port))
        if len(buffer):
            client.send(buffer)
                # now wait for data back
                recv_len = 1
                response = ""
                while recv_len:
                    data
                    = client.recv(4096)
                    recv_len = len(data)
                    response+= data
                    if recv_len < 4096:
                        break
                    print response,
                    # wait for more input
                    buffer = raw_input("")
                    buffer += "\n"
                    # send it off
                    client.send(buffer)
    except:
        print "[*] Exception! Exiting."
        # tear down the connection
        client.close()

client_sender("test 04 oooo")
