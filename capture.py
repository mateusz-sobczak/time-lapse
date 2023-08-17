#!/usr/bin/python3

import cv2
import os
import time
from datetime import datetime

# Inicjalizacja kamery
cameras = [cv2.VideoCapture(i) for i in range(8)]

# Ustalenie maksymalnej rozdzielczosci dla kazdej kamery
for camera in cameras:
    #camera.set(cv2.CAP_PROP_FRAME_WIDTH, camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    #camera.set(cv2.CAP_PROP_FRAME_HEIGHT, camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

try:
    while True:
        current_time = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3]
        
        for i, camera in enumerate(cameras):
            ret, frame = camera.read()
            if ret:
                folder_name = f"./cameras/camera_{i}"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                file_name = os.path.join(folder_name, f"{current_time}.jpg")
                cv2.imwrite(file_name, frame)
                print(f"Zdjecie z kamery {i} zapisane: {file_name}")

        time.sleep(180)  # Czekaj 3 minuty

finally:
    # Zwolnienie kamer i zamkniecie okna OpenCV
    for camera in cameras:
        camera.release()
    cv2.destroyAllWindows()
