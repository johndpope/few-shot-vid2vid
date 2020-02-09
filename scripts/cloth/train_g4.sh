python train.py --name cloth \
--dataroot  ./datasets/cloth \
--dataset_mode fewshot_cloth \
--batchSize    30      \
--gpu_ids      1,2,3,4 \
--nThreads     8       \
--adaptive_spade       \
--warp_ref             \
--spade_combine        \
--add_face_D           \
--remove_face_labels   \
--niter_single 100 --niter 200 #--continue_train

### --adaptive_spade base for adaptive weight generation   : use adaptive convolution in the SPADE module
### --warp_ref       base for attention mechanism          : warp the reference image and combine with the synthesized image
### --spade_combine  base for temporal and flow generation : use SPADE to combine with warped image instead of linear combination
### --add_face_D     base for discriminators               : add additional discriminator for face region