import numpy as np
import os
import cv2
import argparse


# 1. Body 25 keypoints
keypoint_ids = ['Nose', 'Neck',
             'RShoulder', 'RElbow', 'RWrist', 'LShoulder', 'LElbow', 'LWrist',
             'MidHip',
             'RHip', 'RKnee', 'RAnkle', 'LHip', 'LKnee', 'LAnkle',
             'REye', 'LEye', 'REar', 'LEar',
             'LBigToe', 'LSmallToe', 'LHeel', 'RBigToe', 'RSmallToe', 'RHeel',
             'Background']


def load_keypoints(infile):

    data = np.load(infile, allow_pickle='TRUE').item()

    print('dimension:', data['dimension'])
    print('number of people:', data['keypoints'].shape[0])

    for keypoints in data['keypoints']:

        keypoints = dict(zip(keypoint_ids, keypoints))

        fname = infile.replace('/data/', '/pix/').replace('_keypoints.npy', '_rendered.png')
        image = cv2.imread(fname)

        cv2.line(image, tuple(keypoints['Neck'][0:2]), tuple(keypoints['MidHip'][0:2]), color=(0, 255, 255), thickness=1)

        for id, value in keypoints.items():

            x, y, score = value

            if score != 0:
                image = cv2.circle(image, (int(x), int(y)), radius=5, color=(0, 255, 255), thickness=-1)

        cv2.imshow("OpenPose 1.7.0 - Tutorial Python API", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':

    # python visualize_extracted_keypoints.py --input output/data/modern/Paul\ Delvaux/74313_keypoints.npy

    parser = argparse.ArgumentParser(description='Extract the keypoints')
    parser.add_argument("--input",
                        help="Process a directory of images. Read all standard formats (jpg, png, bmp, etc.).")
    args = parser.parse_args()

    infile = args.input

    load_keypoints(infile=infile)