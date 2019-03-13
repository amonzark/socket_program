#import socket
import socket
import threading

#inisialisasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.0.0.10"
#Bind
sock.bind(("0.0.0.0", 7775))
#s.bind(("0.0.0.0", 7775))

conlist = {}
conlist["kirim"] = []
conlist["terima"] = []

#listen
sock.listen(100)  #Berapa jumlah koneksi yang dapat di handle dalam satu koneksi

#fungsi utk menghandle thread baru
def handle_thread(conn):
    while True :
        try :
            #terima data yang di kirimkan oleh client
            data = conn.recv(100) #berapa data yang mau kita baca dari buffer
            #Decode jdai String
            data = data.decode("ascii")
            print(data)
            if (conn not in conlist["kirim"] and conn not in conlist["terima"]) :                
                msg = "connected as"
                if (data == "kirim") :
                    conlist["kirim"].append(conn)
                    msg = msg+" sender"
                    conn.send(msg.encode("ascii"))
                elif (data == "terima") :
                    conlist["terima"].append(conn)
                    msg = msg+" reciever"
                    conn.send(msg.encode("ascii"))
                else :
                    msg = "failed"+msg
                    conn.send(msg.encode("ascii"))
                #kirim lagi ke client
                #s.connect((host, 7774))    
            else :                
                if (conn in conlist["kirim"]) :
                    for client in conlist["terima"] :
                        client.send(data.encode("ascii"))
        except(socket.error): #agar tidak terjadi error ketika di matikan secara paksa
            s.close()
            sock.close()
            break

#menggunakan "while True"(agar  koneksinya dapat berulang-ulang)
while True :
    #Terima permintaan koneksi
    conn, client_addr = sock.accept()  #tidak harus nama conn, dan client_addr
    #conn1, client_addr1 = s.accept()
    #pemanggilang fungsi thread (thread baru)
    t = threading.Thread(target=handle_thread, args=(conn,))
    #start thread
    t.start()
    