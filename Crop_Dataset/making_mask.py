import os
from pycocotools import mask
import cv2
import numpy as np
import json
import shutil

mask_dir = 'masks'
if not os.path.exists(mask_dir):
    os.makedirs(mask_dir)


img_folder = 'images'
if not os.path.exists(img_folder):
    os.makedirs(img_folder)

# Đường dẫn đến file COCO JSON
ann_file = '_annotations.coco.json'

# Đọc file COCO JSON
with open(ann_file, 'r') as f:
    annotations = json.load(f)


# Vòng lặp qua từng ảnh trong tập dữ liệu
for img_info in annotations['images']:
    # Đọc ảnh vào
    img = cv2.imread(os.path.join(img_folder, img_info['file_name']))

    # Khởi tạo ảnh nhị phân với kích thước bằng với ảnh gốc và giá trị pixel mặc định là 0
    binary_mask = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)

    # Vòng lặp qua từng đối tượng trong ảnh
    for ann in annotations['annotations']:
        if ann['image_id'] == img_info['id']:
            # Tạo mask của đối tượng
            rle = mask.frPyObjects(ann['segmentation'], img.shape[0], img.shape[1])
            mask_arr = mask.decode(rle)
            mask_arr = np.sum(mask_arr, axis=2)
            mask_arr = np.where(mask_arr > 0, 1, 0).astype(np.uint8)

            # Thêm mask của đối tượng vào ảnh nhị phân
            binary_mask = cv2.bitwise_or(binary_mask, mask_arr)

    # Lưu ảnh nhị phân
    print( img_info['file_name'])
    cv2.imwrite(os.path.join('masks', 'MSK_' + img_info['file_name'].rsplit('.',1)[0] + '.png'), binary_mask)
    

for filename in os.listdir('.'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        shutil.move(filename, os.path.join('images', filename))