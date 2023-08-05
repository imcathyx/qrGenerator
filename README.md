How to Use the QR Code Generator Program:

1. Download everything in this repository except the README file.
2. Create a folder on your desktop and rename it as "QRcode."
3. Drag all downloaded files into the "QRcode" folder. Also, create a subfolder within "QRcode" called "qrGenerated."
4. Edit the "qrLinks.xlsx" file to customize the file names and website links of the QR codes you want to generate. Be careful not to change the names of “qrLinks.xlsx”, “qrGenerator.py”, and “qrLogo.png”. Also, please refrain from modifying cells A1 and B1 of "qrLinks.xlsx."
5. In "qrLinks.xlsx," the first column (col A) is used to input desired file names for each generated QR code, and the second column (col B) is for the website each code should link to. Make sure to delete any test data in these columns. Ensure that all file names do not contain spaces or "/", as it may lead to issues in QR code generation. If any QR codes are not generated, you will receive notifications in the terminal.
6. All generated QR codes will be saved in the "qrGenerated" folder. Do not change the name or location of this folder. Before generating new QR codes, always clear the files in this folder to avoid confusion.
7. Once you have filled "qrLinks.xlsx" with the QR code information, you can run the "qrGenerator.py" file.

To Run qrGenerator.py:

1. Click "Run Without Debugging." If all the required libraries are present, the QR codes should be generated correctly in the "qrGenerated" folder.
2. In case of any issues, you may need to run the following commands in the VSCode terminal:
   1. pip install pandas
   2. pip install qrcode
   3. pip install pillow

Please ensure that you have Python and pip preinstalled on your system. If not, follow the instructions below for installing Python and pip:

## Installing Python and piip (Credit to ChatGPT)

### Windows:
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

4. **Verify Pip Installation:**
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

4. **Install Pip:**
   - macOS should come with `pip` or `pip3` installed by default. To verify, open Terminal and type `pip --version` or `pip3 --version`.
