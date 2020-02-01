import urllib.request, requests, zipfile, os

rgb_url = "https://cv.iri.upc-csic.es/Dataset/links/rgb.txt"
seg_url = "https://cv.iri.upc-csic.es/Dataset/links/seg_cloth.txt"
rgb_dir = "./datasets/cloth/train_images"  
seg_dir = "./datasets/cloth/train_labels"  


def unzip_file(file_name, unzip_path):
    zip_ref = zipfile.ZipFile(file_name, 'r')
    zip_ref.extractall(unzip_path)
    zip_ref.close()
    os.remove(file_name)

def download_file(url, dir):
    urls = requests.get(url).text.split("\n")
    urls = urls[0]
    for i, u in enumerate(urls):
        urllib.request.urlretrieve(u, os.path.join(dir,"%s"%i)) 
    

def download_file_from_csic(id, destination):
    print("download from %s and %s"%(rgb_url, seg_url))
    download_file(rgb_url, rgb_dir)
#    download_file(seg_url, seg_dir) 
     

def main():
    file_id   = ''
    chpt_path = './datasets/' 
    if not os.path.isdir(chpt_path):
        os.makedirs(chpt_path)
    destination = os.path.join(chpt_path, 'datasets.zip')
    download_file_from_csis(file_id, destination)
#    unzip_file(destination, chpt_path)

main() 
