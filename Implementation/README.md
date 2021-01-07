# Data for training


We decided to reduce the huge dataset for training purposes.
We have selected 100 different chinese characters to train the neural network on them.
They are located in folders Selected_to_test/train. 


Script CSVHandler.py is used for creating test_selected_china.csv and train_selected_china.csv
It converts each picture to array, where the values are pixel's represantation in gray scale.
Each row is a different .png file of handwritten character.
First column "label" is given as a UTF-8 name of chinese letter, which is taken from name of subdirectory,
in which character is included.
At the beginnig we've used method to rename all subfolders to the conventional form "CharX"