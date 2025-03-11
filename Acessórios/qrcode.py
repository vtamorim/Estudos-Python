import qrcode


data = 'Qr Code using make() function'



img = qrcode.make(data)

img.save("MyQrCode.png")