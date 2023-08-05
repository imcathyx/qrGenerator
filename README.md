# qrGenerator
To use this program, download the folder in this repository and put it in your desktop. rename the folder as QRcode.
In the folder, the relevant files for editing are qrGenerator.py, qrLinks, and qrLogo.png
If you need to make changes to the qrLogo, make sure the naming is exactly the same as "qrLogo.png"
In qrLinks, the first column (col A) is used to input desired file names for each qr code generated, and the second column (col B) is the website each code should link to. when using, make sure to delete the test data in these columns! DO NOT change cells A1 and B1 or the program will crash!!!!!!! 
make sure that all the file names do not include spaces or "/", or the QR code cannot be generated properly. This will not end the program, but you will see which QR codes werent generated in the terminal!
all the QR codes generated will be in the qrGenerated folder. PLEASE DONT CHANGE THE NAME OR LOCATION OF THIS FOLDER. before running this program, make sure to clear all content from this folder!
after the qrLinks.xlsx file have been filled with the qr code information, you can run the qrGenerator.py file!
open the qrGenerator.py file and select run without debugging on VS code to see if all the necessary libraries are installed
if not, you might have to run the following in the terminal:
1. pip install pandas
2. pip install qrcode
3. pip install pillow
With these installed, you should be able to run the file. To run, click "run without debugging" in VScode.


This is assuming you have python and pip preinstalled. for instructions on these, see below:

Installing python and pip (credit chatgpt)
## Windows:
1. **Download Python:**
   - Go to the official Python website: https://www.python.org/downloads/
   - Scroll down to the latest stable release of Python (e.g., Python 3.9.x).
   - Click on the "Download" link for Windows (either 32-bit or 64-bit, depending on your system architecture).

2. **Run the Installer:**
   - Once the download is complete, run the installer (the downloaded file will have a name like `python-3.9.x.exe`).
   - Check the box "Add Python x.x to PATH" during the installation. This will allow you to use Python and pip from the Command Prompt or PowerShell.

3. **Complete the Installation:**
   - Follow the prompts in the installer, and Python will be installed on your system.
   - After the installation is complete, you can open the Command Prompt or PowerShell and type `python` to verify that Python is installed correctly. Type `exit()` to exit the Python interpreter.

4. **Verify pip Installation:**
   - Open the Command Prompt or PowerShell and type `pip`. If pip is installed, you'll see a list of available commands. If not, you may need to add Python to PATH or reinstall Python with the "Add Python x.x to PATH" option checked.
   

## macOS:
1. **Python Pre-Installed:**
   - macOS comes with Python pre-installed. However, it's recommended to install the latest version of Python for development purposes.
   - Go to the official Python website: https://www.python.org/downloads/
   - Scroll down to the latest stable release of Python (e.g., Python 3.9.x).
   - Click on the "Download" link for macOS.

2. **Run the Installer:**
   - Once the download is complete, run the installer (the downloaded file will have a name like `python-3.9.x-macosx10.9.pkg`).
   - Follow the prompts in the installer to complete the installation.

3. **Verify Installation:**
   - Open the Terminal application (can be found in the Utilities folder within Applications).
   - Type `python3` and press Enter to verify that Python is installed. Type `exit()` to exit the Python interpreter.

4. **Install pip:**
   - macOS should come with `pip` or `pip3` installed by default. To verify, open Terminal and type `pip --version` or `pip3 --version`.


