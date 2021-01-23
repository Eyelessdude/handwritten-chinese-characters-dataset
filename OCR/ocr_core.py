import os
import cv2
import pytesseract

rootPath = './TestDataset'

for subDir, dirs, files in os.walk(rootPath):
    for directory in dirs:
        correctlyRecognizedCounter = 0
        groundTruth = directory
        files = os.listdir(os.path.join(rootPath, groundTruth))
        for file in files:
            imagePath = os.path.join(rootPath, groundTruth, file)
            image = cv2.imread(imagePath)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            threshold = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)[1]
            text = pytesseract.image_to_string(threshold, lang='chi_tra', config="--psm 10")
            if text.strip() == groundTruth:
                correctlyRecognizedCounter += 1

        dirAccuracy = (correctlyRecognizedCounter / len(files)) * 100
        print('Accuracy for dir {} is {}'.format(directory, dirAccuracy))
