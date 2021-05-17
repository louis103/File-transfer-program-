import socket,threading

HOST = "127.0.0.1"
PORT = 9999

client_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_server.connect((HOST,PORT))
print("connected...")

files_received = []
filename = input(str("Enter the name for incoming file: "))
file = open(filename,'wb')
file_data = client_server.recv(1024)
file.write(file_data)
file.close()
files_received.append(file)
print("File received and appended successfully!!!")
print(f"The length of the files list is {len(files_received)}")
print(files_received)
