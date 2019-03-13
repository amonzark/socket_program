import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

a = input("Enter First Number : ")
b = input("Enter Second Number : ")
c = input("Enter Operator : ")

mergeArray = a + "." + b + "." + c
encodeFile = mergeArray.encode("ascii")

#kirim data
s.sendto( encodeFile,("127.0.0.1", 2000))
#menerima kembalian data
data = s.recv(65536)
hasil = data.decode("ascii")
print("Result = " + hasil)