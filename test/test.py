import cv2
cap = cv2.VideoCapture(1)
while 1:
    _,img = cap.read()
    cv2.imshow("",img)
    cv2.waitKey(1)