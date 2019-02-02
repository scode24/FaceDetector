import os
import time

import schedule

import sendEmailWithAttachment


def job():
    count = 0
    imgList = []
    for img in os.listdir(os.getcwd()):
        if count == 5:
            count = 0
            print(imgList)
            sendEmailWithAttachment.sendEmail(imgList)
            for imgToDel in imgList:
                os.remove(imgToDel)
            imgList.clear()
        if '.png' in img:
            imgList.append(img)
            count = count + 1
    if len(imgList) > 0:
        print(imgList)
        sendEmailWithAttachment.sendEmail(imgList)
        imgList.clear()

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
