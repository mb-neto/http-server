import socket

HOST = '' # ip do servidor (em branco)
PORT = 8080 # porta do servidor

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listen_socket.bind((HOST, PORT))

listen_socket.listen(1)

print ('Serving HTTP on port %s ...' % PORT)

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    array = request.decode('utf-8').split()
    http_response = str()
    sentence = str()
    if array[1]:
        url = array[1].split('/')
        if url[0] == 'index.html':
            http_response = """HTTP/1.1 200 OK \r \n \r \n"""
            page = open('pages/index.html', 'r')
            sentence = page.read()
            page.close()
        else:
            http_response = """HTTP/1.1 404 Not found \r \n \r \n"""
            page = open('pages/not_found.html', 'r')
            sentence = page.read()
            page.close()
        print(http_response + sentence)
        client_connection.send((http_response + sentence).encode('utf-8'))
    client_connection.close()
listen_socket.close()