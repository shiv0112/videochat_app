import cv2
cap=cv2.VideoCapture(0)

while True:
   ret, photo = cap.read()
   cv2.imshow("Video",photo)
   if cv2.waitKey(10) == 13:
      break

cv2.destroyAllWindows()
cap.release()