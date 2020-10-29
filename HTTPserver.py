# importacao das bibliotecas
import socket

# definicao do host e da porta do servidor
HOST = '' # ip do servidor (em branco)
PORT = 8080 # porta do servidor

# cria o socket com IPv4 (AF_INET) usando TCP (SOCK_STREAM)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# permite que seja possivel reusar o endereco e porta do servidor caso seja encerrado incorretamente
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# vincula o socket com a porta (faz o "bind" do IP do servidor com a porta)
listen_socket.bind((HOST, PORT))

# "escuta" pedidos na porta do socket do servidor
listen_socket.listen(1)

# imprime que o servidor esta pronto para receber conexoes
print ('Serving HTTP on port %s ...' % PORT)

while True:
    # aguarda por novas conexoes
    client_connection, client_address = listen_socket.accept()
    # o metodo .recv recebe os dados enviados por um cliente atraves do socket
    request = client_connection.recv(1024)
    array = request.decode('utf-8').split('/')
    # imprime na tela o que o cliente enviou ao servidor
    print(array[1])
    url = array[1].split()
    print(url[0])
    # declaracao da resposta do servidor
    if url[0] == 'index.html':
        http_response = "HTTP/1.1 200 OK"
        page = open('pages/index.html', 'r')
    else:
        http_response = "HTTP/1.1 404 Not found \r \n \r \n"
        page = open('pages/bad_request.html', 'r')
    # servidor retorna o que foi solicitado pelo cliente (neste caso a resposta e generica)
    client_connection.send((http_response.encode('utf-8'), page.read(),))
    # encerra a conexao
    client_connection.close()

# encerra o socket do servidor
listen_socket.close()