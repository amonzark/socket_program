import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#kirim data
s.sendto( " Selama Datang".encode("ascii"),("127.0.0.1", 2000))
#menerima kembalian data
data = s.recv(65536)

print(data)