import sys
import cv2
import os
from sys import platform
import argparse
import time
from pathlib import Path
import numpy as np
import pyopenpose as op


def generate_keypoints(infile, show):

    datum = op.Datum()
    imageToProcess = cv2.imread(infile)
    datum.cvInputData = imageToProcess
    opWrapper.emplaceAndPop(op.VectorDatum([datum]))

    # print("Body keypoints: \n" + str(datum.poseKeypoints))
    print('Body keypoints shape:', datum.poseKeypoints.shape)
    # print('Image shape:', datum.cvOutputData.shape)

    image = datum.cvOutputData
    data = {}

    # show the keypoints of the FIRST person only
    # for x, y, score in datum.poseKeypoints[0]:
    #     if score != 0:
    #         image = cv2.circle(image, (int(x), int(y)), radius=5, color=(0, 255, 255), thickness=-1)

    if show:
        cv2.imshow("OpenPose 1.7.0 - Tutorial Python API", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        outfile_data, outfile_pix = generate_outfile(infile=infile)

        data['keypoints'] = datum.poseKeypoints
        data['dimension'] = datum.cvOutputData.shape

        np.save(outfile_data, data)
        cv2.imwrite(outfile_pix, image)

        print('Saving data to', outfile_data)
        print('Saving pix to', outfile_pix)


def generate_outfile(infile):

    # out directories
    outdir = os.path.join('output')

    dirname = infile[infile.find('/') + 1:infile.rfind('/')]

    outdir_data = os.path.join(outdir, 'data', dirname)
    outdir_pix = os.path.join(outdir, 'pix', dirname)

    if not os.path.exists(outdir_data):
        os.makedirs(outdir_data)

    if not os.path.exists(outdir_pix):
        os.makedirs(outdir_pix)

    fname = infile[infile.rfind('/') + 1:infile.rfind('.')]
    outfile_npy = os.path.join(outdir_data, '{}_keypoints.npy'.format(fname))
    outfile_pix = os.path.join(outdir_pix, '{}_rendered.png'.format(fname))

    return outfile_npy, outfile_pix


if __name__ == '__main__':

    # python extract_keypoints_pyopenpose.py --input datasets/

    parser = argparse.ArgumentParser(description='Extract the keypoints')
    parser.add_argument("--input", help="Process a directory of images. Read all standard formats (jpg, png, bmp, etc.).")
    args = parser.parse_args()

    params = dict()
    params["model_folder"] = "models/"

    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    # time the execution time
    start = time.time()

    if os.path.isfile(args.input):
        generate_keypoints(infile=args.input, show=True)

    elif os.path.isdir(args.input):
        for path in Path(args.input).rglob('*.jpg'):
            try:
                generate_keypoints(infile=str(path), show=False)
            except:
                continue

    end = time.time()
    print("OpenPose demo successfully finished. Total time: " + str(end - start) + " seconds")