import os
import pandas as pd
import qrcode
from PIL import Image

def generate_qr_code_with_logo(link, filename):
    # Avoid crashes if links are broken
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img = qr_img.convert("RGBA")

        # Load the logo image with color
        logo_path = os.path.join(os.path.dirname(__file__), "qrLogo.png")
        logo_img = Image.open(logo_path)

        # Calculate the maximum width of the logo to be 20% of the QR code's width
        max_logo_width = qr_img.size[0] * 0.2

        # Calculate the new size for the logo while maintaining its aspect ratio
        width_percent = max_logo_width / float(logo_img.size[0])
        new_logo_height = int(float(logo_img.size[1]) * float(width_percent))
        new_logo_size = (int(max_logo_width), new_logo_height)

        # Resize the logo
        logo_img = logo_img.resize(new_logo_size, Image.LANCZOS)

        # Calculate the center position for the resized logo
        pos = ((qr_img.size[0] - logo_img.size[0]) // 2, (qr_img.size[1] - logo_img.size[1]) // 2)

        # Paste the resized logo on the QR code
        qr_img.paste(logo_img, pos, logo_img)

        # Save the QR code with logo
        save_path = os.path.join(os.path.dirname(__file__), "qrGenerated", filename)
        qr_img.save(save_path)

    except Exception as e:
        print(f"The website corresponding to file {filename} is not found.")
        print(f"Error message: {e}")




def main():
    # Read data from the Excel file
    excel_file = os.path.join(os.path.dirname(__file__), "qrLinks.xlsx")
    data = pd.read_excel(excel_file)

    # Create the qrGenerated folder if it doesn't exist
    generated_folder = os.path.join(os.path.dirname(__file__), "qrGenerated")
    os.makedirs(generated_folder, exist_ok=True)

    # Generate QR codes for each link
    for index, row in data.iterrows():
        filename = row['File Name'] + ".png"
        link = row['Website']
        generate_qr_code_with_logo(link, filename)
        print(f"QR code generated for {filename}")

if __name__ == "__main__":
    main()
