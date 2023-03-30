from PIL import Image
import os
import numpy as np


image_dir = "RGB_zero"

if not os.path.exists('RGB_random'):
    os.makedirs('RGB_random')

# Đường dẫn đến thư mục chứa ảnh đã chỉnh sửa
output_dir = "RGB_random"

# Điều chỉnh độ lệch chuẩn của phân phối Gaussian
scale = 50

for image_file in os.listdir(image_dir):
    if image_file.endswith(".jpg"):
        # Đọc ảnh và tính giá trị trung bình của tất cả các pixel trong ảnh
        image_path = os.path.join(image_dir, image_file)
        image = Image.open(image_path)
        avg_pixel = np.mean(np.asarray(image), axis=(0, 1))

        # Thay thế các pixel có giá trị (R, G, B) = (0, 0, 0)
        pixels = image.load()
        width, height = image.size
        for x in range(width):
            for y in range(height):
                if pixels[x, y] == (0, 0, 0):
                    # Sinh giá trị từ phân phối Gaussian sử dụng giá trị trung bình đã tính toán
                    value = np.random.normal(avg_pixel, scale=scale)
                    value = np.clip(value, 0, 255).astype(np.uint8)
                    pixels[x, y] = tuple(value)

        # Lưu ảnh vào thư mục output_dir
        output_path = os.path.join(output_dir, image_file)
        image.save(output_path)
