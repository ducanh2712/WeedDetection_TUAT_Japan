# Code for checking pixel having RGB values = (0,0,0)

from PIL import Image

# Load ảnh từ file
img = Image.open("FIXED/FIXED_RGB_IMG_3667_JPG_jpg.rf.6c082dc781428e4e47ad21a4bb89c526.jpg")

# Lấy kích thước của ảnh
width, height = img.size

# Duyệt qua từng pixel trong ảnh và kiểm tra giá trị của nó
for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        if (r, g, b) == (0, 0, 0):
            print("Image exist (0, 0, 0)")
