import os

from PRAO import *
from tqdm import tqdm

import glob

files = sorted(glob.glob('*_profiles.txt'))

for  name in tqdm(files):
    print(os.path.basename(name))
