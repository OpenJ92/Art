from class_run import RUN
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-PDF')
parser.add_argument('-VideoPATH')
parser.add_argument('-OFN')
args = parser.parse_args()

video_list = [args.VideoPATH + '/' + file_ for file_ in os.listdir(args.VideoPATH)]

RUN(args.PDF, args.OFN, video_list).runv2()
