import ftplib
server = ftplib.FTP()
server.connect('0.0.0.0', 111)
server.login('amon','secret')
#server.cwd('/home') 

server.dir()
def uploadFile():
 filename = 'class.py'
 server.storbinary('STOR '+filename, open(filename, 'rb'))
 server.quit()
def downloadFile():
 filename = 'coba.txt' 
 localfile = open(filename, 'wb')
 server.retrbinary('RETR ' + filename, localfile.write, 1024)
 server.quit()
 localfile.close()

uploadFile()
downloadFile()