from pyzbar import pyzbar
from PIL import Image
import os
import webbrowser
import time
while True:
	try:	
		qr1 = input('Okunacak dosyanın uzantısıyla beraber ismini girin (örnek isim.png) : ')
		qr = pyzbar.decode(Image.open(qr1))
		break
	except FileNotFoundError:
		os.system('cls')
		print('Dosya Bulunamadı! Lütfen tekrar deneyin.')
qrinf = qr[0].data.decode('ascii')

if qrinf.startswith('https://') :
	while True:
		cont = input('linki acmak istiyor musunuz ? Y/n : ')
		if cont == 'Y' or cont =='y':
			webbrowser.open_new(qrinf)
			break		
		elif cont == 'N' or cont =='n':
			print('Qr icerigi : {}'.format(qrinf))
			break
		else:
			os.system('cls')
			print('Hatalı bir değer girdiniz! Lütfen Tekrar deneyin.')
else:
	print('Qr icerigi : {}'.format(qrinf))
time.sleep(2)
print("\n Çıkış yapılıyor...")
time.sleep(3)
os.system('exit')