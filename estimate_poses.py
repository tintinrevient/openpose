import os
import argparse
import subprocess

# python estimate_poses.py --input input/classical/
# python estimate_poses.py --input input/modern/

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='OpenPose')
    parser.add_argument('--input', help='Path to the input directory')
    args = parser.parse_args()

    for root, dirs, files in os.walk(args.input):
        for name in dirs:

            indir = os.path.join(root, name)
            fname = indir[indir.find('/')+1:]
            outdir = os.path.join('output', fname)

            print('indir:', indir)
            print('outdir:', outdir)

            if not os.path.exists(outdir):
                os.makedirs(outdir)

            bash_command = subprocess.run(['./build/examples/openpose/openpose.bin',
                                           '--image_dir', indir,
                                           '--write_images', outdir], check=True, text=True)