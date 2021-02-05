# -*- coding: utf-8 -*-
import cv2
import os

list = os.listdir('videos/')  # download videos in "videos" folder
extensions = []
filenames = []

# loading file name and extension except for .part file
for item in list:
    filename, fileExtension = os.path.splitext(item)

    if(fileExtension != ".part"):
        filenames.append(filename)
        extensions.append(fileExtension)
        print(item)
print("will be downloaded")

# Download function
for title in list:
    # add directory name to title
    title = "videos/" + title
    vidcap = cv2.VideoCapture(title)
    # variable for checking status
    frame = -1
    count = 0
    # print title which will be captured
    print(title + "will be captured")
    #if frame > int(vidcap.get(1)), stop capture
    while(vidcap.isOpened() and (frame <= int(vidcap.get(1)))):
        frame += 1
        ret, image = vidcap.read()
        # capture video by 60 frame
        if(int(vidcap.get(1)) % 60 == 0):
            print('Saved frame number : ' + str(int(vidcap.get(1))))
            cv2.imwrite("images/frame%d.jpg" % count, image)
            print('Saved frame%d.jpg' % count)
            count += 1
    # close video which is finshed capturing
    vidcap.release()

# print end status
print("end download")
