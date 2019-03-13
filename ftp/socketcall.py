import socket

request = (
    "USER amon\r\n" +
    "PASS secret\r\n" +
    "PWD /home/amon/Documents/ftpserver \r\n")

sock = socket.socket ()
sock.connect ( ("0.0.0.0", 111) )
sock.send (str.encode (request))


while True :
    buffer = sock.recv (1024)
    if not buffer :
        break
    print (buffer)

sock.close ()
