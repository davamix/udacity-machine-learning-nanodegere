# Script to distribute randomly the images from dataset into the folders of train, validation and test.
# Also create a csv file with the labels for train and validation images
# https://stackoverflow.com/questions/17412439/how-to-split-data-into-trainset-and-testset-randomly

# Usage:
# dataset-splitter.py  70 20 5
#   percentage of data for Train(70), Validation(20) and Test(5)

# Behaviour:
# Split the percentage of images from the original dataset folder into the three different sets of Train, Validation and Test on data folder
# This will create a csv file in train and validation folders with the labels

import os
import argparse
import random
import csv
from shutil import copyfile

PARASITIZED_IMAGES_PATH = '../data/cell_images/Parasitized'
UNINFECTED_IMAGES_PATH = '../data/cell_images/Uninfected'
TRAIN_PARASITIZED_IMAGES_PATH = '../data/train/parasitized'
TRAIN_UNINFECTED_IMAGES_PATH = '../data/train/uninfected'
VALIDATION_PARASITIZED_IMAGES_PATH = '../data/validation/parasitized'
VALIDATION_UNINFECTED_IMAGES_PATH = '../data/validation/uninfected'
TEST_PARASITIZED_IMAGES_PATH = '../data/test/parasitized'
TEST_UNINFECTED_IMAGES_PATH = '../data/test/uninfected'
TRAIN_LABELS_PATH = '../data/train_labels.csv'
VALIDATION_LABELS_PATH = '../data/validation_labels.csv'

# Get the specified amount of images from the path
def get_files_from_path(path, amount):
    files = []

    for r, d, f in os.walk(path):
        for idx_img in range(amount):
            if '.png' in f[idx_img]: 
                files.append(f[idx_img])

    return files

# Return a list of [original_image_name, new_name_with_id, is_parasitized]
def create_target_image(image_paths, is_parasitized, last_id = 1):
    target_images = []
    for img_path in image_paths:
        name = "cell_{}.png".format(str(last_id))
        target_images.append([img_path, name, int(is_parasitized)])
        last_id = last_id + 1

    return target_images, last_id

# Copy the specified amount_of_images from the source_path to the destination_path
def copy_images(amount_of_images, target_images, source_path, destination_path, last_index = 0):
    # The copied images will be return in order to create the file with labels easily
    copied_images = []

    for x in range(amount_of_images):
        # o: original name
        # n: new name (with id)
        o, n, _ = target_images[last_index]
        src = os.path.join(source_path, o)
        dst = os.path.join(destination_path, n)
        
        copyfile(src, dst)

        copied_images.append(target_images[last_index])

        last_index = last_index + 1
    
    return last_index, copied_images

# Create the csv file or append data with the image names and labels from target_images
def create_csv_with_labels(file_name, target_images):
    with open(file_name, mode='a', newline='') as csv_file:
        header_names = ['image_id', 'is_parasitized']
        writer = csv.DictWriter(csv_file, fieldnames=header_names)
        
        # Only add header once
        if csv_file.tell() == 0:
            writer.writeheader()

        for img in target_images:
            writer.writerow({'image_id': img[1], 'is_parasitized': str(img[2])})


# Arguments builder
parser = argparse.ArgumentParser()
parser.add_argument('train', help='Percentage of images for train', type=int)
parser.add_argument('validation', help='Percentage of images for validation', type=int)
parser.add_argument('test', help='Percentage of images for test', type=int)

# Parse the arguments
args = parser.parse_args()
train_amount_percentage = args.train # Amount of images as percentage to use in training
validation_amoun_percentage = args.validation # Amount of images as percentage to use in validation
test_amount_percentage = args.test # Amount of images as percentage to use in testing

# Calculate the number of images to use
train_amount = int(train_amount_percentage * len(next(os.walk(PARASITIZED_IMAGES_PATH))[2]) / 100)
validation_amount = int(validation_amoun_percentage * len(next(os.walk(PARASITIZED_IMAGES_PATH))[2]) / 100)
test_amount = int(test_amount_percentage * len(next(os.walk(PARASITIZED_IMAGES_PATH))[2]) / 100)

# Get the list of paths of the images for parasitized and uninfected images
parasitized_images = get_files_from_path(PARASITIZED_IMAGES_PATH, train_amount + validation_amount + test_amount)
uninfected_images = get_files_from_path(UNINFECTED_IMAGES_PATH, train_amount + validation_amount + test_amount)

# Create the structure with target images [original_name, name_with_id, is_parasitized]
target_parasitized_images, last_id = create_target_image(parasitized_images, True)
target_uninfected_images, _ = create_target_image(uninfected_images, False, last_id)

# Shuffle the images in order to use different set of images for every test
random.shuffle(target_parasitized_images)
random.shuffle(target_uninfected_images)

# Copy Parasitized images to train folder and adding labels
print("-> Copying {} train images...".format(train_amount))
last_index, target = copy_images(train_amount, target_parasitized_images, PARASITIZED_IMAGES_PATH, TRAIN_PARASITIZED_IMAGES_PATH)
print("-> Adding train labels...")
create_csv_with_labels(TRAIN_LABELS_PATH, sorted(target, key = lambda x: x[1]))

# Copy Parasitized images to validation folder and adding labels
print("-> Copying {} validation images...".format(validation_amount))
last_index, target = copy_images(validation_amount, target_parasitized_images, PARASITIZED_IMAGES_PATH, VALIDATION_PARASITIZED_IMAGES_PATH, last_index=last_index)
print("-> Adding validation labels...")
create_csv_with_labels(VALIDATION_LABELS_PATH, sorted(target, key = lambda x: x[1]))

# Copy Parasitized images to test folder
print("-> Copying {} test images...".format(test_amount))
_ = copy_images(test_amount, target_parasitized_images, PARASITIZED_IMAGES_PATH, TEST_PARASITIZED_IMAGES_PATH, last_index=last_index)

# Copy Uninfected images to train folder and adding labels
print("-> Copying {} train images...".format(train_amount))
last_index, target = copy_images(train_amount, target_uninfected_images, UNINFECTED_IMAGES_PATH, TRAIN_UNINFECTED_IMAGES_PATH)
print("-> Adding train labels...")
create_csv_with_labels(TRAIN_LABELS_PATH, sorted(target, key = lambda x: x[1]))

# Copy Uninfected images to validation folder and adding labels
print("-> Copying {} validation images...".format(validation_amount))
last_index, target = copy_images(validation_amount, target_uninfected_images, UNINFECTED_IMAGES_PATH, VALIDATION_UNINFECTED_IMAGES_PATH, last_index=last_index)
print("-> Adding validation labels...")
create_csv_with_labels(VALIDATION_LABELS_PATH, sorted(target, key = lambda x: x[1]))

# Copy Parasitized images to test folder
print("-> Copying {} test images...".format(test_amount))
_ = copy_images(test_amount, target_uninfected_images, UNINFECTED_IMAGES_PATH, TEST_UNINFECTED_IMAGES_PATH, last_index=last_index)
