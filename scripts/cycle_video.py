import glob
import shutil
import os
import IPython
import os.path as osp

img_folder = 'fusion_full/*/*/*.jpg'
files = glob.glob(img_folder)
video_list = ['3', '4', '6', '7', '8']
for video in video_list:
    for file in files:
        mid = file.split('/')[-1].split('v')[1]
        v_id = mid[0]
        p_id = file.split('/')[-2]
        src_file = file
        if v_id == video:
            dst_g_dir = 'cycle_video/' + v_id + '/gallery/' + p_id
            if not osp.exists(dst_g_dir):
                os.makedirs(dst_g_dir)
            dst_g_file = dst_g_dir + '/' + file.split('/')[-1]
            shutil.copyfile(src_file, dst_g_file)
        else:
            dst_q_dir = 'cycle_video/' + video + '/query/' + p_id
            if not osp.exists(dst_q_dir):
                os.makedirs(dst_q_dir)
            dst_q_file = dst_q_dir + '/' + file.split('/')[-1]
            shutil.copyfile(src_file, dst_q_file)
            
