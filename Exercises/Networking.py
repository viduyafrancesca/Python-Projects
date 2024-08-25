import ftplib

def ftp_connection(filename, HOSTNAME="ftp.dlptest.com", USERNAME="dlpuser", PASSWORD="rNrKYTX9g7z3RgJRmxWuGHbeu"):

    # Required credentials available in dlptest website, information changes from time to time
    # HOSTNAME = "ftp.dlptest.com"
    # USERNAME = "dlpuser"
    # PASSWORD = "rNrKYTX9g7z3RgJRmxWuGHbeu"

    # Connect to the server
    ftpServer = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

    # Force utf-8 encoding
    ftpServer.encoding = "utf-8"
    return ftpServer

def upload_ftp_file(filename, ftpServer):
    # Read file in binary mode
    with open(filename, "rb") as file:
        ftpServer.storbinary(f"STOR {filename}", file)

    # Get list of files
    ftpServer.dir()

    # Close connection
    ftpServer.quit()

def download_ftp_file(filename, ftpServer):
    # Get file in binary mode
    with open(filename, "wb") as file:
        ftpServer.retrbinary(f"RETR {filename}", file.write)
    
    # Get list of files
    ftpServer.dir()

    # Display content of downloaded file
    file = open(filename, "r")
    print("Content of File:\n", file.read())

    # Close connection
    ftpServer.quit()


if __name__ == '__main__':
    filename = "FTPTestFile.txt" 
    ftpServer = ftp_connection(filename)
    # upload_ftp_file(filename, ftpServer)
    download_ftp_file(filename, ftpServer)
