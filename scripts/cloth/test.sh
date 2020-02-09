python test.py  --name cloth \
--dataroot  ./datasets/cloth \
--dataset_mode fewshot_cloth \
--which_epoch 5     \
--gpu_ids     5,6,7 \
--adaptive_spade --warp_ref --spade_combine --remove_face_labels --finetune  \
--seq_lbl_path  ./datasets/cloth/test_labels/segmentation_clothes/woman17/02_04_jump/camera01 \
--seq_img_path  ./datasets/cloth/test_images/rgb/woman17/02_04_jump/camera01/wpskin08_bottom70_glasses01_hair13_shoes19_top23_none_none_background1928