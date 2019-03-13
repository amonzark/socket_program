#import socket
import socket

#inisialisasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#Bind
sock.bind(("0.0.0.0", 7777))
#listen
sock.listen(100)  #Berapa jumlah koneksi yang dapat di handle dalam satu koneksi


#menggunakan "while True"(agar  koneksinya dapat berulang-ulang)
while True :
    #Terima permintaan koneksi
    conn, client_addr = sock.accept()  #tidak harus nama conn, dan client_addr
    #terima data yang di kirimkan oleh client
    data = conn.recv(100) #berapa data yang mau kita baca dari buffer
    #Decode jdai String
    data = data.decode("ascii")
    data = "OK " + data
    #kirim lagi ke client
    conn.send(data.encode("ascii"))