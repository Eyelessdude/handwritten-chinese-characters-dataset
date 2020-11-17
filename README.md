# Handwritten Chinese Characters (Hanzi) Dataset



Folders CASIA-HWDB_Test and CASIA-HWDB_Train contain pictures of sample data taken from
https://www.kaggle.com/pascalbliem/handwritten-chinese-character-hanzi-datasets


Script CSVHandler.py is used for creating test_china.csv and train_china.csv
It converts each picture to array, where the values are pixel's represantation in gray scale.
Each row is a different .png file of handwritten character.
First column "label" is given as a UTF-8 name of chinese letter, which is taken from name of subdirectory,
in which character is included.
