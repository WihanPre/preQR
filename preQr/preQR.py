import pyqrcode
import png
from pyqrcode import QRCode

qr_string = input("Enter url here: ")

url  = pyqrcode.create(qr_string)

url.png("Desktop\\qr.png", scale = 8)
