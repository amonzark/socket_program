import socket

#inisialisasi objek soket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #AF_INET digunakan untuk ipv4
#SOCK_DGRAM digunakan untuk menandakan protokol UDP

#bind ke alamat ip dan port
s.bind(("127.0.0.1", 2000))

MAX_SIZE_UDP = 65536

while True :
    #recieve
    data, address = s.recvfrom(MAX_SIZE_UDP) 

    pemisahan = data.decode('ascii').split('.')

    a = int(pemisahan[0])
    b = int(pemisahan[1])
    c = pemisahan[2]
    x = 0

    if c == "*":
        x = a * b
    elif c == "/":
        x = a / b
    elif c == "+":
        x = a + b
    elif c == "-":
        x = a - b
    else :
        x = 0
    #tambahkan string ok di depan dan decode byte jadi string dikarenakan python 3
    
    #send
    s.sendto(str(x).encode("ascii"),address)

s.close()