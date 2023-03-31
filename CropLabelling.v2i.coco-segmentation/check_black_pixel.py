# Code for checking pixel having RGB values = (0,0,0)

from PIL import Image

# Load ảnh từ file
img = Image.open("RGB_random/Gauss_IMG_3638_JPG_jpg.rf.3b75789f1a760d55039c38aa3dfdc1cc.jpg")

# Lấy kích thước của ảnh
width, height = img.size

# Duyệt qua từng pixel trong ảnh và kiểm tra giá trị của nó
for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        if (r, g, b) == (0, 0, 0):
            print("Image exist (0, 0, 0)")
            break
        break
    break
