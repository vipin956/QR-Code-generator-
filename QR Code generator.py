import pyqrcode  #pyqrcode =  it is used for qr code generation

url = input("Enter a URL to generate QR code: \n") #enter any url from web

QR = pyqrcode.create(url) # url creation 
QR.png("webqr.png", scale=8)  #scale is ued for parameter