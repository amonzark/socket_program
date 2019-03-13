#import sokcet
import socket

#inisialisasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#kirim permintaan koneksi
sock.connect(("127.0.0.1", 7775))
t = "kirim"     
sock.send(t.encode("ascii"))
data = sock.recv(100)
print(data.decode("ascii"))
while True :    
    #kirim data ke server
    data = input ("Masukkan kata : ")
    sock.send(data.encode("ascii"))

    #terima balasan dari server
    #data = sock.recv(100)
    #print(data.decode("ascii"))