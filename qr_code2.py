# Different QR-code Generator 
import qrcode
from PIL import Image
qr =  qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data("Enter Your Link Here") #Replace with your link
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("Image2.png")  #QR-Code image name