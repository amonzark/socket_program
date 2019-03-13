import ftplib
server = ftplib.FTP()
server.connect('0.0.0.0', 111)
server.login('amon','secret')
#server.cwd('/home') 
# You don't have to print this, because this command itself prints dir contents 
server.dir()
def uploadFile():
 filename = 'class.py' #replace with your file in your home folder
 server.storbinary('STOR '+filename, open(filename, 'rb'))
 server.quit()
def downloadFile():
 filename = 'coba.txt' #replace with your file in the directory ('directory_name')
 localfile = open(filename, 'wb')
 server.retrbinary('RETR ' + filename, localfile.write, 1024)
 server.quit()
 localfile.close()

uploadFile()