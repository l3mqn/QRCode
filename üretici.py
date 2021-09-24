import qrcode

with open("qricerik.txt","r") as dosya:
	for link in dosya:
		input_data = link

qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode001.png')