import cv2

while 1:
    img = cv2.imread('image.jpg')  #load image

    cv2.imshow('image', img)
    key=cv2.waitKey(10)
    if key==27: # press [Esc] key
        break

cap.release()
cv2.destroyAllWindows()
