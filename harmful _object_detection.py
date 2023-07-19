import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from pymsgbox import *

vid = cv2.VideoCapture('video.mp4')

#Uncomment this line to play gun detection and comment the upper one
# vid = cv2.VideoCapture('video2.mp4')
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)
    # print(label)
    if ("knife" in label or "scissors" in label):
        alert(text='Intruder alert a person is carrying harmful object', title='Alert', button='OK')
        vid.release()
        cv2.destroyAllWindows()
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gun_cascade = cv2.CascadeClassifier('cascade.xml')
    gun = gun_cascade.detectMultiScale(gray,1.3, 5,minSize = (200, 200))
    gun_exist = False
       
    if len(gun) > 0:
        gun_exist = True
           
    for (x, y, w, h) in gun:
          
        frame = cv2.rectangle(frame,
                              (x, y),
                              (x + w, y + h),
                              (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]    

    if gun_exist:
        alert(text='Intruder alert a person is carrying a Gun', title='Alert', button='OK')
    else:
        print("guns NOT detected")

     # Display the resulting frame
    cv2.namedWindow("Video frame", cv2.WINDOW_NORMAL)
  
    # Using resizeWindow()  
    cv2.resizeWindow("Video frame", 1200, 900)
    cv2.imshow('Video frame', frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
  
# After the loop release the cap objectq
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()