import argparse
import requests, tarfile, os, sys, subprocess
from tqdm import tqdm
#oneshot_url = "https://cv.iri.upc-csic.es/Dataset/rgb/rgb_woman16_20.tar.gz"
sample_url = "https://cv.iri.upc-csic.es/Dataset/3DPeople_sample.tar.xz"
rgb_url    = "https://cv.iri.upc-csic.es/Dataset/links/rgb.txt"  
seg_url    = "https://cv.iri.upc-csic.es/Dataset/links/seg_cloth.txt" 
chpt_path  = "./datasets/cloth"

def main():
    ### set dir --------------------
    train_rgb = os.path.join(chpt_path, "train_images")
    train_seg = os.path.join(chpt_path, "train_labels")
    test_rgb  = os.path.join(chpt_path, "test_images")
    test_seg  = os.path.join(chpt_path, "test_labels")
    one_rgb   = os.path.join(test_rgb, '02')
    one_seg   = os.path.join(test_seg, '02')
    dirs = [chpt_path, train_rgb,train_seg, test_rgb,test_seg, one_rgb,one_seg] 
    _ = [os.makedirs(dir) for dir in dirs if not os.path.isdir(dir)] 
    ### set train --------------------
    for url in [u for u in requests.get(rgb_url).text.split("\n") if u][:1]:  #Debug mode
        download_file(url, train_rgb)
        unzip_file(url, train_rgb)
    for url in [u for u in requests.get(seg_url).text.split("\n") if u][:1]:  #Debug mode
        download_file(url, train_seg)
        unzip_file(url, train_seg)
    ### set test --------------------
    download_file(sample_url, chpt_path)
    unzip_file(sample_url, chpt_path)
    try:
        sample_dir  = os.path.join(chpt_path, os.path.basename(sample_url).split('.')[0])
        sample_dirs = [p for p in os.walk(sample_dir)]
        sample_rgb  = [p for p in sample_dirs if 'rgb'   in os.path.basename(p[0])][0][0]
        sample_seg  = [p for p in sample_dirs if 'cloth' in os.path.basename(p[0])][0][0]
        subprocess.call(['mv', sample_rgb, os.path.join(test_rgb, os.path.basename(sample_rgb))])
        subprocess.call(['mv', sample_seg, os.path.join(test_seg, os.path.basename(sample_seg))])
        ### set 1shot ---------------------
        subprocess.call(['cp', 'one_rgb.jpg',os.path.join(one_rgb, '0001.jpg')])
        subprocess.call(['cp', 'one_seg.png',os.path.join(one_seg, '0001.png')])
        
    except:
        import traceback
        traceback.print_exc()
        

def download_file(url, dir='./'): 
    session  = requests.Session()
    response = session.get(url, stream=True)
    destination  = os.path.join(dir, os.path.basename(url) )
    content_size = int(response.headers["content-length"])
    try:
        print('download %s'%destination) 
        CHUNK_SIZE = 32768
        pbar = tqdm(total=content_size, unit="B", unit_scale=True)
        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:
                    pbar.update(len(chunk))
                    f.write(chunk)
        pbar.close()
    except:
        import traceback
        traceback.print_exc()
def unzip_file(url, dir='./'):
    destination  = os.path.join(dir, os.path.basename(url) )
    extension    = extension = os.path.basename(url).split('.', 1)[1]
    try: 
        print('decompress %s Please waiting 10m(;_;)'% os.path.basename(url))
        if 'zip' in extension:
            with zipfile.ZipFile(destination, "r") as f:
                f.extractall(dir)
        elif 'tar.gz' in extension or 'tgz' in extension:
            subprocess.call(['tar', '-C', dir, '-zxvf', destination])
        elif 'tar' in extension:
            subprocess.call(['tar', '-C', dir, '-xvf', destination])
        os.remove(destination)
    except:
        import traceback
        traceback.print_exc()
if __name__=="__main__":
    main() 
