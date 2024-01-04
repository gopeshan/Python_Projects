import qrcode

def generate_qrcode(url):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    # Add data (URL) to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Generate an image with specified colors
    qr_image = qr.make_image(fill_color="red", back_color="white")

    # Save the generated QR code image
    qr_image.save("url_qrcode.png")

    # Display the QR code data
    print("QR Code Data:", qr.data_list)

if __name__ == "__main__":
    input_URL = "https://www.google.com/"
    generate_qrcode(input_URL)
