#import socket
import socket
import threading

#inisialisasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.0.0.10"
#Bind
sock.bind(("0.0.0.0", 7774))
#s.bind(("0.0.0.0", 7775))

conlist = {}
conlist["kirim"] = []
conlist["a"] = []
conlist["b"] = []
#conlist["A"] = []
#conlist["B"] = []

#listen
sock.listen(100)  #Berapa jumlah koneksi yang dapat di handle dalam satu koneksi

#fungsi utk menghandle thread baru
def handle_thread(conn):
    while True :
        try :
            #terima data yang di kirimkan oleh client
            data = conn.recv(100) #berapa data yang mau kita baca dari buffer
            #q = conn.recv(1)
            #Decode jdai String
            data = data.decode("ascii")
            print(data)
            if (conn not in conlist["kirim"] and conn not in conlist["a"] and conn not in conlist["b"]) :                
                msg = "connected as"
                if (data == "kirim") :
                    conlist["kirim"].append(conn)
                    msg = msg+" sender"
                    conn.send(msg.encode("ascii"))
                elif (data == "a") :
                    conlist["a"].append(conn)
                    msg = msg+" reciever"
                    conn.send(msg.encode("ascii"))
                elif (data == "b") :
                    conlist["b"].append(conn)
                    msg = msg+" reciever"
                    conn.send(msg.encode("ascii"))
                else :
                    msg = "failed"+msg
                    conn.send(msg.encode("ascii"))
                #kirim lagi ke client
                #s.connect((host, 7774))    
            else :                
                if (conn in conlist["kirim"]) :
                    data = data.split('.')
                    q = data[0]
                    text = data[1]
                    if(q == "a"):
                        for client in conlist["a"] :
                            client.send(text.encode("ascii"))
                    elif(q == "b"):
                        for client in conlist["b"] :
                            client.send(text.encode("ascii"))
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
    