import requests
import ntpath
import os
from tqdm import tqdm
import tarfile

from config import dataset_url


def download():
    name = ntpath.basename(dataset_url)

    print(name)
    
    if not os.path.exists(name):

        r = requests.get(dataset_url, stream=True)

        total_size = int(r.headers.get('content-length', 0))
        block_size = 1024
        t=tqdm(total=total_size, unit='iB', unit_scale=True)

        with open(name, 'wb') as f:
            for data in r.iter_content(block_size):
                t.update(len(data))
                f.write(data)
        t.close()
        if total_size != 0 and t.n != total_size:
            print("ERROR, something went wrong")

        tf = tarfile.open(name)

        print("Dataset ready.")

    else:
        print ("File already exists.")
