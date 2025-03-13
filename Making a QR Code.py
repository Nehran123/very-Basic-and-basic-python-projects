import qrcode

QR=qrcode.make("https.Something.com")
QR.save("Something2.png")
print("This QR Code has been saved")