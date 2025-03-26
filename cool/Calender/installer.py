import os
import requests
from werkzeug.utils import secure_filename

def main(path):
    print("#---Running Calender Installer---#")

    # Download Calender.js
    FileUrl = "https://raw.githubusercontent.com/8nt0n/VaultixStore/refs/heads/main/cool/Calender/Calender.js"
    if download_file(FileUrl, path, "Calender.js") != 0:
        return -1 #return -1 if there was an error downloading

    # Download additional .css file
    FileUrl = "https://raw.githubusercontent.com/8nt0n/VaultixStore/refs/heads/main/cool/Calender/Calender.css"
    if download_file(FileUrl, path, "Calender.css") != 0:
        return -1
    
    return 0

def download_file(url, path, filename):
    """Download a JS file from GitHub, save it, and log the encrypted filename."""


    # Step 1: Download the JS file from GitHub
    response = requests.get(url)
    if response.status_code == 200:
        installer_content = response.text
    else:
        return -1 # Content couldnt be fetched, check Internet connection


    # Step 2: Secure and prepare the filename
    secured_filename = secure_filename(filename)  # Make the filename secure

    # Step 3: Save the installer to the specified directory
    file_path = os.path.join(path, secured_filename)
    with open(file_path, 'w') as file:
        file.write(installer_content)

    return 0
