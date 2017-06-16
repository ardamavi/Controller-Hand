# Arda Mavi
import os
import cv2
import platform
from time import sleep
from game_control import *
from predict import predict
from keras.models import model_from_json

def create_data(label, img_len):
    dataset_path = 'Data/Train_Data/{0}'.format(label)
    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path)
    cap = cv2.VideoCapture(0)
    count = 0
    while 1:
        if count >= img_len:
            break
        sleep(0.1)
        ret, img = cap.read()
        cv2.imwrite('{0}/{1}.jpg'.format(dataset_path, count), img)
        count += 1
    cap.release()

def main():
    # Get Model:
    model_file = open('Data/Model/model.json', 'r')
    model = model_file.read()
    model_file.close()
    model = model_from_json(model)
    model.load_weights("Data/Model/weights.h5")

    # Get camera:
    cap = cv2.VideoCapture(0)

    # Open game in browser:
    open_game(browser='chrome', url='http://apps.thecodepost.org/trex/trex.html')

    while 1:
        # Get image from camera:
        ret, img = cap.read()
        Y = predict(model, img)
        if Y == 0:
            release()
        elif Y == 1:
            press()
    cap.release()

if __name__ == '__main__':
    main()
