import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


hsv_mask_folder = 'HSV_data/masks'
mask_folder = 'Data_Original/masks'
full_mask_folder = 'Mask_Full'
image_folder = 'Data_Original/images'

# if not os.path.exists(full_mask_folder):
#     os.makedirs(full_mask_folder)
    
# # Lấy danh sách các tệp tin trong thư mục mask
# mask_files = sorted([f for f in os.listdir(mask_folder) if os.path.isfile(os.path.join(mask_folder, f))])
# # Lấy danh sách các tệp tin trong thư mục HSV_mask
# hsv_mask_files = sorted([f for f in os.listdir(hsv_mask_folder) if os.path.isfile(os.path.join(hsv_mask_folder, f))])

# # So sánh từng ảnh trong hai thư mục
# for i in tqdm(range(len(mask_files))):
#     mask_path = os.path.join(mask_folder, mask_files[i])
#     hsv_mask_path = os.path.join(hsv_mask_folder, hsv_mask_files[i])
#     full_mask_path = os.path.join(full_mask_folder, mask_files[i])

#     if os.path.exists(hsv_mask_path):
#         # Mở ảnh mask và HSV_mask
#         mask_img = Image.open(mask_path).convert('L')
#         hsv_mask_img = Image.open(hsv_mask_path).convert('L')
        
#         # Thay đổi các giá trị pixel khác nhau thành 2
#         mask_arr = np.array(mask_img)
#         hsv_mask_arr = np.array(hsv_mask_img)
#         diff_mask = np.where(mask_arr != hsv_mask_arr, 2, mask_arr)

#         # Lưu ảnh mới vào thư mục full_mask
#         Image.fromarray(diff_mask).save(full_mask_path)

# Hiển thị 2 ảnh cùng tên
example = 'IMG_6149_JPG_jpg.rf.05cfb0a7b58208b76943d04bc009b70a.png'
img1 = Image.open(os.path.join(mask_folder, example))
img2 = Image.open(os.path.join(full_mask_folder,example))
img3 = Image.open(os.path.join(hsv_mask_folder,example))
img4 = Image.open(os.path.join(image_folder,example.replace('.png','.jpg')))

print(np.unique(img1),np.unique(img2))

plt.subplot(221), plt.imshow(img1), plt.title("Mask")
plt.subplot(222), plt.imshow(img2), plt.title("Full Mask")
plt.subplot(223), plt.imshow(img3), plt.title("HSV Mask")
plt.subplot(224), plt.imshow(img4), plt.title("Original")
plt.show()