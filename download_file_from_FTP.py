import ftplib
 
HOSTNAME = "cheat.aezakmi.com"
USERNAME = "CJ"
PASSWORD = "bagufix"

ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
ftp_server.encoding = "utf-8"

ftp_server.cwd("Laboratory/PetraBasillea/") 
filename = "coba_download.txt"
 
with open(filename, "wb") as file:
    ftp_server.retrbinary(f"RETR {filename}", file.write)

ftp_server.quit