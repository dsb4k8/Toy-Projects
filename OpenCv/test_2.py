import numpy as np
import cv2

def gray(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

if __name__ == '__main__':

    cap = cv2.VideoCapture("Drone flight over Skid Row LA - See what happens!.mp4")
    frame_no = 0
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


# When everything done, release the capture







