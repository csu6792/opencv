import cv2

cap = cv2.VideoCapture(0) # webcam #0
#cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280); #default 640
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720); #default 480

while 1:
    ret, frame = cap.read()
    print(frame.shape)

    cv2.imshow('CAM', frame)
    key=cv2.waitKey(10)
    if key==27: # press [Esc] key
        break

cap.release()
cv2.destroyAllWindows()
