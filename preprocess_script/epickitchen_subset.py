from shutil import copyfile
import glob
import pdb
import os
import random
from tqdm import tqdm

train_img_dir = '/home/ubuntu/code/setup/confs/study/food_detect/EgoHOS/data/train/image'
train_lbl_dir = '/home/ubuntu/code/setup/confs/study/food_detect/EgoHOS/data/train/label'
val_img_dir = '/home/ubuntu/code/setup/confs/study/food_detect/EgoHOS/data/val/image'
val_lbl_dir = '/home/ubuntu/code/setup/confs/study/food_detect/EgoHOS/data/val/label'
testin_img_dir = '/home/ubuntu/code/setup/confs/study/food_detect/EgoHOS/data/test_indomain/image'
testin_lbl_dir = '/home/ubuntu/code/setup/confs/study/food_detect/EgoHOS/data/test_indomain/label'
testout_img_dir = '/home/ubuntu/code/setup/confs/study/food_detect/EgoHOS/data/test_outdomain/image'
testout_lbl_dir = '/home/ubuntu/code/setup/confs/study/food_detect/EgoHOS/data/test_outdomain/label'

epic_img_dir = '/home/ubuntu/code/setup/confs/study/food_detect/EgoHOS/epic_data/image'
epic_lbl_dir = '/home/ubuntu/code/setup/confs/study/food_detect/EgoHOS/epic_data/label'

imgdirs = [train_img_dir,train_lbl_dir,val_lbl_dir,val_img_dir, testout_img_dir, testin_img_dir, testout_lbl_dir, testin_lbl_dir]
fname_list = []
for imgdir in imgdirs:
    for file in glob.glob(imgdir + '/*'):
        fname = os.path.basename(file)
        if 'epic' in fname:
            if 'label' in file:
                dst_lbl_file = os.path.join(epic_lbl_dir, fname)
                copyfile(file,dst_lbl_file)
            else:
                dst_img_file = os.path.join(epic_img_dir, fname)
                copyfile(file, dst_img_file)





