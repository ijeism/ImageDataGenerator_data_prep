# ImageDataGenerator_data_prep
Organizes a directory of raw, labelled images (class deductable from img path) into required structure for use with Tensorflow ImageDataGenerator.

## Installation

1) Clone this repository.
2) Load your data. Make sure the data is contained in one folder and that its class/label is apparent from the image name in the following format: 0__xyz.jpg vs 1__xyz.jpg, where 0 denotes a negative example and 1 a positive one.
3) From the cloned repository, run `!python organize_idg.py -s {SOURCE_PATH}`.

## Example notebook
And example of structuring data to make it suitable for use with Tensorflow's ImageDataGenerator can be seen in [this Notebook](https://github.com/ijeism/ImageDataGenerator_data_prep/blob/master/image_recognition_structure_data_for_ImageDataGenerator.ipynb).


