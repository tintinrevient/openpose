import os
import argparse
import subprocess
import glob

# python estimate_poses.py --input input/

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='OpenPose')
    parser.add_argument('--input', help='Path to the input directory')
    args = parser.parse_args()

    for root, dirs, files in os.walk(args.input):
        for name in dirs:

            indir = os.path.join(root, name)

            # indir is only the directory with .jpg files
            first_in_indir = glob.glob(os.path.join(indir, '*'))[0]
            if(os.path.isdir(first_in_indir)):
                continue

            fname = indir[indir.find('/')+1:]
            outdir = os.path.join('output', fname)

            print('indir:', indir)
            print('outdir:', outdir)

            if not os.path.exists(outdir):
                os.makedirs(outdir)

            bash_command = subprocess.run(['./build/examples/openpose/openpose.bin',
                                           '--image_dir', indir,
                                           '--write_images', outdir], check=True, text=True)