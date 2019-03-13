import socket

#inisialisasi objek soket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#bind ke alamat ip dan port
s.bind(("127.0.0.1", 2000))

MAX_SIZE_UDP = 65536

while True :
    #recieve
    data, address = s.recvfrom(MAX_SIZE_UDP) 

    #tambahkan string ok di depan dan decode byte jadi string dikarenakan python 3
    data = "OK"+data.decode("ascii")
    #send
    s.sendto(data.encode("ascii"),address)