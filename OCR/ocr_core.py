import pytesseract
import cv2
import os
import argparse
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image being processed")
ap.add_argument("-l", "--lang", type=str, help="Language of the text on the image", default="chi_tra")
ap.add_argument("-p", "--psm", type=int, help="Page segmentation mode", default=10)
args = vars(ap.parse_args())

filename = args["image"]

image = cv2.imread(filename)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)[1]

cv2.imwrite("{}.png".format(os.getpid()), threshold)

text = pytesseract.image_to_string(threshold, lang=args["lang"], config="--psm {}".format(args["psm"]))

print(text)
img = Image.open(filename)
img.show()
