import ftplib

HOSTNAME = "cheat.aezakmi.com"
USERNAME = "CJ"
PASSWORD = "bagufix"

ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
ftp_server.encoding = "utf-8"

ftp_server.dir()

ftp_server.quit()