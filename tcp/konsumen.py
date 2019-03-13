#import sokcet
import socket

host = "127.0.0.1"
#inisialisasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#kirim permintaan koneksi
#sock.bind(("0.0.0.0", 7774))
sock.connect((host, 7774))
t = input("queue : ")
sock.send(t.encode("ascii"))
data = sock.recv(100)
print(data)
while True :
    #q = input("queue : ")
    #sock.send(q.encode("ascii"))
    data = sock.recv(100)
    print(data)
    #data = input ("Masukkan kata : ")
    #sock.send(data.encode("ascii"))
    