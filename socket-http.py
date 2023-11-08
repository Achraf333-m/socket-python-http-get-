# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('www.py4inf.com', 80))
# cmd = 'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()

# ^^^^ forgot about \r, that is why it was not working

# import socket

# mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mySocket.connect(('data.pr4e.org', 80))
# command = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mySocket.send(command)

# while True:
#     data = mySocket.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())

print(ord('i'))
# mySocket.close()