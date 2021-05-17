import socket
HOST = "127.0.0.1"
PORT = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
print("*****Server waiting for connections!*****")

conn,address = server.accept()

print(f"{address} has connected to the server!")

filename = input(str("Enter the name of the file to send: "))
file = open(filename,'rb')
file_data = file.read(1024)
conn.send(file_data)
print("File has been send successfully!!!")