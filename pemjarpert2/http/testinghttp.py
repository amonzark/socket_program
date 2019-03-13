#import library http
import http.client

# inisiasi koneksi http
conn = http.client.HTTPConnection("ftp1.at.proftpd.org")
# kirim req
conn.request("GET", "/")
resp = conn.getresponse()
# cetak respon
print(resp.read())
print(resp.status)

'''from ftplib import FTP
import http.client
with FTP("ftp1.at.proftpd.org") as ftp:
    ftp.login() #login
    #ftp.mkd('newdir') #make new directory
    ftp.dir() #list file
    #ftp.retrlines('LIST') #list file
    #wdir = ftp.sendcmd('PWD')
    #print(wdir)


conn = http.client.HTTPConnection("ftp1.at.proftpd.org")
conn.request("GET", "/")
resp = conn.getresponse()
print(resp.status)'''