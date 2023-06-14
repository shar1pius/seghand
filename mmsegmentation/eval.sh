# python tools/test.py \
#        /home/ubuntu/code/setup/confs/study/food_detect/EgoHOS/mmsegmentation/work_dirs/twohands_cb_to_obj1/twohands_cb_to_obj1.py \
#        /home/ubuntu/code/setup/confs/study/food_detect/EgoHOS/mmsegmentation/work_dirs/twohands_cb_to_obj1/best_mIoU_iter_22000.pth \
#        --eval mIoU

# python tools/test.py \
#        /home/ubuntu/code/setup/confs/study/food_detect/EgoHOS/mmsegmentation/work_dirs/seg_twohands/seg_twohands.py \
#        /home/ubuntu/code/setup/confs/study/food_detect/EgoHOS/mmsegmentation/work_dirs/seg_twohands/best_mIoU_iter_64000.pth \
#        --eval mIoU

python tools/test.py \
       /home/ubuntu/code/setup/confs/study/food_detect/EgoHOS/mmsegmentation/work_dirs/seg_handobj1/seg_handobj1.py \
       /home/ubuntu/code/setup/confs/study/food_detect/EgoHOS/mmsegmentation/work_dirs/seg_handobj1/best_mIoU_iter_96000.pth \
       --eval mIoU
