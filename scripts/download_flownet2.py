import os
from download_gdrive import *
os.system('cd models/networks/flownet2_pytorch/; bash install.sh; cd ../../../')

file_id = '1E8re-b6csNuo-abg1vJKCDjCzlIam50F'
chpt_path = './models/networks/flownet2_pytorch/'
destination = os.path.join(chpt_path, 'FlowNet2_checkpoint.pth.tar')
download_file_from_google_drive(file_id, destination) 