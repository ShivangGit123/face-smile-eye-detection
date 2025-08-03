import cv2

face_cascade = cv2.CascadeClassifier("C:\\Users\\Dell\\Desktop\\OpenCV\\haarcascade_frontalface_alt.xml")
smile_cascade = cv2.CascadeClassifier("C:\\Users\\Dell\\Desktop\\OpenCV\\haarcascade_smile.xml")
eyes_cascade = cv2.CascadeClassifier("C:\\Users\\Dell\\Desktop\\OpenCV\\haarcascade_eye.xml")\

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    face  = face_cascade.detectMultiScale(gray , 1.1 , 5)

    for(x,y,w,h) in face:
        cv2.rectangle(frame , (x,y) , (x+w , y+h) , (0,250,0) , 2)

        roi_gray = gray[y:y+h , x:x+w]
        roi_color = frame[y:y+h , x:x+w]    

        eyes = eyes_cascade.detectMultiScale(roi_gray , 1.01 ,5)
        if len(eyes) >0:
            cv2.putText(frame , "Eyes Detected " , (x,y-40) , cv2.FONT_HERSHEY_DUPLEX, 0.6 , (255,100,0) , 2)

                        
        smile = smile_cascade.detectMultiScale(roi_gray , 1.5 ,20)
        if len(smile) >0:
            cv2.putText(frame , "Smiling" , (x,y-10) , cv2.FONT_HERSHEY_DUPLEX,0.6 , (0,0,255) , 2)

   
    cv2.imshow("Face Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    