#import sokcet
import socket

host = "127.0.0.1"
#inisialisasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#kirim permintaan koneksi
#sock.bind(("0.0.0.0", 7774))
sock.connect((host, 7775))
t = "terima"     
sock.send(t.encode("ascii"))
data = sock.recv(100)
print(data)
while True :
    data = sock.recv(100)
    print(data)
    #data = input ("Masukkan kata : ")
    #sock.send(data.encode("ascii"))
    