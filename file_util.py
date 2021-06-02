import os
import glob
import re
from shutil import copyfile, move

# indir = os.path.join('datasets', 'nude')
indir = os.path.join('datasets', 'full')

for root, dirs, files in os.walk(indir):

    for dir in dirs:
        dir = os.path.join(root, dir)

        for fname in glob.glob(dir + '/*.jpg'):
            # source file
            src = fname

            # destination file
            slash_list = [m.start() for m in re.finditer(r"/", fname)]
            slash_3rd_pos = slash_list[2]
            dst = fname[:slash_3rd_pos] + fname[fname.rfind('/'):]

            # move
            move(src, dst)

        if len(os.listdir(dir)) == 0:
            os.rmdir(dir)