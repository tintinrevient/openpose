import os
import argparse
import subprocess
import glob

# python estimate_poses.py --input input/
# python examples/tutorial_api_python/04_keypoints_from_images.py --image_dir test/

if __name__ == '__main__':

    # python extract_keypoints_bin.py --input test/ --output test/

    parser = argparse.ArgumentParser(description='OpenPose')
    parser.add_argument('--input', help='Path to the input directory')
    parser.add_argument('--output', help="Path to the output directory")
    args = parser.parse_args()

    bash_command = subprocess.run(['./build/examples/openpose/openpose.bin',
                                   '--image_dir', args.input,
                                   '--write_images', args.output], check=True, text=True)

