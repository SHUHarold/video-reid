import glob
import os
import shutil
import os.path as osp

img_paths = glob.glob(r'*/*/*.jpg')
for img_path in img_paths:
    src_img = img_path
    mid_list = img_path.split('/')
    id_four = '0' * (4 - len(mid_list[1]))
    dst_img = mid_list[0] + '/' + mid_list[1] + '/' + id_four + mid_list[1] + '_' + mid_list[-1]
    shutil.move(src_img, dst_img)
