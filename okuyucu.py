from pyzbar import pyzbar
from PIL import Image
import os
import webbrowser
import time
qr = pyzbar.decode(Image.open('qrcode001.png'))

qrinf = qr[0].data.decode('ascii')

if qrinf.startswith('https://') :
	cont = input('linki acmak istiyor musunuz ? Y/n : ')
	if cont == 'Y' or cont =='y':
		webbrowser.open_new(qrinf)		
	elif cont == 'N' or cont =='n':
		print('Qr icerigi : {}'.format(qrinf))
	else :
		print('Cikis Yapiliyor...')
		time.sleep(1)
		os.system('exit')
else:
	print('Qr icerigi : {}'.format(qrinf))
time.sleep(5)