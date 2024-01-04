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
    # Get user input for the URL
    input_URL = input("Enter the URL to generate a QR code: ").strip()

    # Validate the URL (you can add more robust URL validation if needed)
    if not input_URL.startswith(("http://", "https://")):
        input_URL = "http://" + input_URL

    generate_qrcode(input_URL)
