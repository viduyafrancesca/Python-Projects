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
    file = open("filename", "r")
    print("Content of File:\n", file.read())

    # Close connection
    ftpServer.quit()

def run_ftp():
    filename = "FTPTestFile.txt" 
    ftpServer = ftp_connection(filename)
    upload_ftp_file(filename, ftpServer)
    download_ftp_file(filename, ftpServer)


import whois
import os
from datetime import datetime
def whois_lookup(url):
    # Test if domain exists
    try:
        domainInfo = whois.whois(url)
        # Input info of domain in text file
        filename = "domainInfo.txt"
        filePath = os.getcwd()+"/"+filename
        appendSearch = whois_data(domainInfo)
        if os.path.isfile(filePath):
            file = open(filename, "a")
            for x in appendSearch:
                file.write(x)
            file.close()
        else:
            file = open(filename, "w")
            for x in appendSearch:
                file.write(x)
            file.close()
        
        print("Domain info can be found in domainInfo.txt")
            
    except Exception:
        print("Domain not registered")
    

def whois_data(domainInfo):
    appendSearch = []
    appendSearch.append("\n")
    appendSearch.append("Searched: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\n")
    if (isinstance(domainInfo.domain_name,str)):
        appendSearch.append("Domain Name: " + domainInfo.domain_name+"\n")
    else:
        appendSearch.append("Domain Name: " + domainInfo.domain_name[0]+"\n")
    appendSearch.append("Domain Org: " + domainInfo.org+"\n")
    appendSearch.append("Domain Registrar: " +domainInfo.registrar+"\n")
    appendSearch.append("Domain Country: " + domainInfo.country+"\n")

    return appendSearch

if __name__ == '__main__':
    # FTP Testing
    run_ftp()

    # Whois
    whois_lookup("instagram123.com")
