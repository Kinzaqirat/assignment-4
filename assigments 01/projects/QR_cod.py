# import qrcode

# img=qrcode.make("Hello world")
# img.save("qr_code.png")


import cv2
img=cv2.imread("qr_code.png")
data=cv2.QRCodeDetector()
vl1,vl2,vl3=data.detectAndDecode(img)
print(vl1)
