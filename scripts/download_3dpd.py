import requests, zipfile, os, sys, subprocess
from tqdm import tqdm
test_url = "https://cv.iri.upc-csic.es/Dataset/rgb/rgb_woman06_10.tar.gz"
def main():
    rgb_url = "https://cv.iri.upc-csic.es/Dataset/links/rgb.txt"  
    seg_url = "https://cv.iri.upc-csic.es/Dataset/links/seg_cloth.txt" 
    chpt_path = "./datasets"
    rgb_dir = os.path.join(chpt_path, "cloth/train_images")
    seg_dir = os.path.join(chpt_path, "cloth/train_labels")
    dirs = [chpt_path, rgb_dir, seg_dir]  
    ### make file
    _=[os.makedirs(dir) for dir in dirs if not os.path.isdir(dir)] 
    ### download_file
    for url in [u for u in requests.get(rgb_url).text.split("\n") if u][:1]:  #Debug mode
        download_file(url, rgb_dir)
        #unzip_file()

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
def unzip_file(file_name, unzip_path):
    zip_ref = zipfile.ZipFile(file_name, 'r')
    zip_ref.extractall(unzip_path)
    zip_ref.close()
    os.remove(file_name)
if __name__=="__main__":
    main() 
