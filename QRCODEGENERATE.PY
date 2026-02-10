import qrcode
def generate_qr_code(data):
    filename = "E:\\PROJECT\\QR CODE PROJECT\\qrcode.png"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
def main():
    data = input("Enter the data to encode in the QR code: ")
    generate_qr_code(data)
    print(data)
    print("QR code generated and saved as qrcode.png")
    
if __name__ == "__main__":    main()

