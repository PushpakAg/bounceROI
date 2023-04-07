import cv2
import time
snipH = 50
snipW = 150
snipCR = int(snipH/2)
snipCC = int(snipW/2)
changeInRow = 1
changeInCols = 1
myCam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
myCam.set(cv2.CAP_PROP_FRAME_WIDTH,640)
myCam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
myCam.set(cv2.CAP_PROP_FPS,30)
myCam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore, frames = myCam.read()
    ROI = frames[int(snipCR-snipH/2):int(snipCR+snipH/2), int(snipCC-snipW/2):int(snipCC+snipW/2)]
    frames = cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
    frames = cv2.cvtColor(frames,cv2.COLOR_GRAY2BGR)
    frames[int(snipCR-snipH/2):int(snipCR+snipH/2), int(snipCC-snipW/2):int(snipCC+snipW/2)] = ROI
    snipCR+=changeInRow
    snipCC+=changeInCols
    if (snipCR-snipH/2) <= 0 or (snipCR+snipH/2) >= 480:
        changeInRow*=-1
    if (snipCC-snipW/2) <= 0 or (snipCC+snipW/2) >= 640:
        changeInCols*=(-1)
    cv2.imshow("demo", frames)
    cv2.moveWindow("demo",0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
myCam.release()
