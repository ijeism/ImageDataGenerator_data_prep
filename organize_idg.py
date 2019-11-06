import os
import glob
import random
import argparse
from shutil import copyfile


""" Organizes a directory of raw, labelled images (class identifiable from img path)
into required structure for use with Tensorflow ImageDataGenerator.
"""

# Construct argument parser
ap = argparse.ArgumentParser()

ap.add_argument("-s", "--source", required=True, help = "path to source images directory")
ap.add_argument("-p", "--split", default=0.7, type=float, help = "train/test split")

args = vars(ap.parse_args())

# create var names for all arguments
source_dir = args["source"]
SPLIT_SIZE = float(args["split"])

# name directories
!mkdir "POSITIVES/"
!mkdir "NEGATIVES/"
!mkdir "training/POSITIVES/"
!mkdir "training/NEGATIVES/"
!mkdir "testing/POSITIVES/"
!mkdir "testing/NEGATIVES/"

pos_dir = "POSITIVES/"
neg_dir = "NEGATIVES/"
training_pos = "training/POSITIVES/"
training_neg = "training/NEGATIVES/"
test_pos = "testing/POSITIVES/"
test_neg = "testing/NEGATIVES/"



# split positive and negative cases
# Sorts images by class (binary) and moves them into POS and NEG directories, respectively
for filename in os.listdir(source_dir):
    this_file = source_dir + filename
    if filename.split("__")[0] == "0":
        destination = neg_dir + filename
        copyfile(this_file, destination)
    else:
        destination = pos_dir + filename
        copyfile(this_file, destination)

print("There are {} Positives.".format(len(glob.glob(os.path.join(pos_dir, '*')))))
print("There are {} Negatives.".format(len(glob.glob(os.path.join(neg_dir, '*')))))


# define datasets to build (dType, input path, train and test folders)
datasets = [
("POS", pos_dir, training_pos, test_pos),
("NEG", neg_dir, training_neg, test_neg)
]

# loop over train and test datasets
for (dType, input_path, destination_train, destination_test) in datasets:
    # loop over images
    files = []
    for filename in os.listdir(input_path):
        file = input_path + filename
        files.append(filename)

    training_length = int(len(files) * SPLIT_SIZE)
    testing_length = int(len(files) - training_length)
    shuffled_set = random.sample(files, len(files))
    training_set = shuffled_set[0:training_length]
    testing_set = shuffled_set[training_length:]

    # split images from both POS and NEG classes into training and test sets
    for filename in training_set:
        this_file = input_path + filename
        destination = destination_train + filename
        copyfile(this_file, destination)

    for filename in testing_set:
        this_file = input_path + filename
        destination = destination_test + filename
        copyfile(this_file, destination)

    print('Populating Training and Test directories for {}'.format(input_path.split('/')[-1]))
    print('There are {} Training images'.format(len(glob.glob(os.path.join(destination_train, '*')))))
    print('There are {} Test images'.format(len(glob.glob(os.path.join(destination_test, '*')))))
