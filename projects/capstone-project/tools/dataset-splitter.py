# Script to distribute randomly the images from dataset into the folders of train, validation and test.
# https://stackoverflow.com/questions/17412439/how-to-split-data-into-trainset-and-testset-randomly

# Usage:
# dataset-splitter.py  70 20 5
#   percentage of data for Train(70), Validation(20) and Test(5)

# Behaviour:
# Split the percentage of images from the original dataset folder into the three different sets of Train, Validation and Test on data folder

import os
import argparse
import random
from shutil import copyfile

PARASITIZED_IMAGES_PATH = '../data/cell_images/Parasitized'
UNINFECTED_IMAGES_PATH = '../data/cell_images/Uninfected'
TRAIN_PARASITIZED_IMAGES_PATH = '../data/train/parasitized'
TRAIN_UNINFECTED_IMAGES_PATH = '../data/train/uninfected'
VALIDATION_PARASITIZED_IMAGES_PATH = '../data/validation/parasitized'
VALIDATION_UNINFECTED_IMAGES_PATH = '../data/validation/uninfected'
TEST_PARASITIZED_IMAGES_PATH = '../data/test/parasitized'
TEST_UNINFECTED_IMAGES_PATH = '../data/test/uninfected'

def get_files_from_path(path):
    files = []

    for r, d, f in os.walk(path):
        for file in f:
            if '.png' in file:
                files.append(file)

    return files

def copy_images(amount_of_images, source_path, destination_path, images_source, last_index = 0):
    for x in range(amount_of_images):
        image_name = "cell_{}.png".format(str(x + 1))
        src = os.path.join(source_path, images_source[last_index])
        dst = os.path.join(destination_path, image_name)
        last_index = last_index + 1

        copyfile(src, dst)

    return last_index

# Arguments builder
parser = argparse.ArgumentParser()
parser.add_argument('train', help='Percentage of images for train', type=int)
parser.add_argument('validation', help='Percentage of images for validation', type=int)
parser.add_argument('test', help='Percentage of images for test', type=int)

# Parse the arguments
args = parser.parse_args()
train_amount = args.train
validation_amount = args.validation
test_amount = args.test

# Get a list of all images files for parasitized and uninfected images
parasitized_images = get_files_from_path(PARASITIZED_IMAGES_PATH)
uninfected_images = get_files_from_path(UNINFECTED_IMAGES_PATH)

# Shuffle the images in order to use different set of images for every test
random.shuffle(parasitized_images)
random.shuffle(uninfected_images)

## PARASITIZED IMAGES ##

# Calculate the amount of parasitized images to copy based on the argument
train_to_copy = train_amount * len(parasitized_images) / 100
validation_to_copy = validation_amount * len(parasitized_images) / 100
test_to_copy = test_amount * len(parasitized_images) / 100

# Split Parasitized images
image_index = 0

print("Splitting Parasitized images...")

print("-> Copying {} train images...".format(train_to_copy))
last_index = copy_images(train_to_copy, PARASITIZED_IMAGES_PATH, TRAIN_PARASITIZED_IMAGES_PATH, parasitized_images)
print("-> Copying {} validation images...".format(validation_to_copy))
last_index = copy_images(validation_to_copy, PARASITIZED_IMAGES_PATH, VALIDATION_PARASITIZED_IMAGES_PATH, parasitized_images, last_index)
print("-> Copying {} test images...".format(test_to_copy))
last_index = copy_images(test_to_copy, PARASITIZED_IMAGES_PATH, TEST_PARASITIZED_IMAGES_PATH, parasitized_images, last_index)


## UNINFECTED IMAGES ## 

# Calculate the amount of unifected images to copy based on the argument
train_to_copy = train_amount * len(uninfected_images) / 100
validation_to_copy = validation_amount * len(uninfected_images) / 100
test_to_copy = test_amount * len(uninfected_images) / 100

# Split Uninfected images
image_index = 0

print("Splitting Uninfected images...")

print("-> Copying {} train images...".format(train_to_copy))
last_index = copy_images(train_to_copy, UNINFECTED_IMAGES_PATH, TRAIN_UNINFECTED_IMAGES_PATH, uninfected_images)
print("-> Copying {} validation images...".format(validation_to_copy))
last_index = copy_images(validation_to_copy, UNINFECTED_IMAGES_PATH, VALIDATION_UNINFECTED_IMAGES_PATH, uninfected_images, last_index)
print("-> Copying {} test images...".format(test_to_copy))
last_index = copy_images(test_to_copy, UNINFECTED_IMAGES_PATH, TEST_UNINFECTED_IMAGES_PATH, uninfected_images, last_index)