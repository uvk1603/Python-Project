import qrcode
from PIL import Image

# taking image which user wants
Logo_link = 'python.png'
logo = Image.open(Logo_link)

# taking base width
base_width = 150
# adjust image size
size = (base_width/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(size)))
logo = logo.resize((base_width, hsize), Image.ANTIALIAS)

# taking url or text
url = 'http://www.vnrvjiet.ac.in/'
QRcode.add_data(url)
QRcode.make()
# taking color name from user
QRcolor = 'Purple'

# adding color to QR code
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="white").convert('RGB')

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
    (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# save the QR code generated
QRimg.save('logo.png')
print('QR code generated!')
