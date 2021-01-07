import numpy as np
import pandas as pd
import math
from PIL import Image
import PIL.ImageOps 
import glob
import os

class CSVHandler:

    cur = []

    def __init__(self):
        self.directory = ""

    def set_imgs_directory(self, directory):
        self.directory = directory

    def write_to_csv(self, csv_filename):
        f = open(csv_filename, "w+", encoding="utf-8")
        f.write("label")
        for i in range (0, 784):
            f.write(",pixel"+str(i))
        f.write("\n")
        for sub_dir in os.listdir(self.directory + '/'):
            for img_file in glob.glob(self.directory + '/' + sub_dir + '/*.png'): # all pngs from dir
                img = Image.open(img_file).convert("L")
                img = PIL.ImageOps.invert(img)
                img = img.resize((28, 28))
                im2csv = np.array(img).reshape(784)
                f.write(sub_dir)
                f.write(",")
                f.write(",".join(map(str, im2csv)))
                f.write("\n")
        f.close()

    def rename_folders(self):
        i = 0
        for sub_dir in os.listdir('Selected_to_train/'):
            tlist = [sub_dir, str(i)]
            self.cur.append(tlist)
            print(self.cur[i])
            i = i + 1
        for sub_dir in os.listdir('Selected_to_train/'):
            for cnt in self.cur:
                if sub_dir == cnt[0]:
                    os.rename(os.path.join('Selected_to_train/', sub_dir), os.path.join('Selected_to_train/', cnt[1]) )
        for sub_dir in os.listdir('Selected_to_test/'):
            for cnt in self.cur:
                if sub_dir == cnt[0]:
                    os.rename(os.path.join('Selected_to_test/', sub_dir), os.path.join('Selected_to_test/', cnt[1]) )



    def create_data_from_csv(self, csv_filename):
        global x_set, y_set
        file = pd.read_csv(csv_filename)
        y_set = file["label"]
        x_set = file.drop(labels=["label"], axis=1)
        x_set = x_set.values.reshape(x_set.shape[0], 28, 28, 1)
        x_set = x_set.astype('float32')
        x_set /= 255
        return x_set, y_set

# csv = CSVHandler()
# # csv.rename_folders()
# csv.set_imgs_directory('Selected_to_train/')
# csv_train_images_filename = 'train_selected_china.csv'
# csv.write_to_csv(csv_train_images_filename)

# csv2 = CSVHandler()
# csv2.set_imgs_directory('Selected_to_test/')
# csv_train_images_filename = 'test_selected_china.csv'
# csv2.write_to_csv(csv_train_images_filename)