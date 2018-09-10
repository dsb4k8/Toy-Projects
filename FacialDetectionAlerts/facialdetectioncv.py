import numpy as np
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import cv2
import time
import sys
import os


sys.path.append('/usr/local/lib/python2.7/site-packages')

os.system("sudo modprobe bcm2835-v4l2")
# This Script is written as a proof of concept. 

# - When this script is ran, the built-in camera should turn on and listen for a face. When a face is detected, an image is captured, saved locally, and emailed to the specified email address.

# - I have included implicit substitution instructions in the file path parameters. DO NOT RUN WITH UPDATING CAPITALIZED INFORMATION in script.
# - High level Flow:
    # 1) Load haarcascade files
    # 2) Implement face detection usign files as reference
    # 3) If a face is detected:
        # - capture image of face and save it locally
       # Else:
        # - continue camera refresh
    # 4) Initialize smtp object and stablish connection to email server using SMTP
    # 5) Start TlS Encryption
    # 5) Input login credentials
    # 6) Create attachment with locally stored image
    # 7) Send Email to same address
#                                                       -Diego Brown
#                                                       -9/4/2018

    

if __name__=="__main__":
    


    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#    eye_cascade  = cv2.CascadeClassifier("haarcascade_eye.xml")

#    smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")
    

    # START CAPUTRE
    cap = cv2.VideoCapture(0)
    
    # LISTEN, LOCATE, AND SAVE FACIAL STRUCTURES
    
    while True:
        ret, img = cap.read()
        #Low RAM: Reducing size of frame image to speed up Frame Rate/ reduce computational expendature
	ret = cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,320)
	ret = cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,240)
	#my case is flipped 180 (upside down)
	img = cv2.flip(img, 0)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,  1.2, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y), (x+w, y+h), (255,0,0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color= img[y:y+h, x:x+w]

            # To Save in same directory, leave as file name only
            cv2.imwrite("Capture/result.jpg", img)
            break

        cv2.imshow("img", img)
	#Quick kill if face is detected from haarcascade
	if faces != ():
	    break
        #Manual kill if face is not detected
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    # Input a second location to save image file
    cv2.imwrite("last_capture.jpg",  img)
    cap.release()
    cv2.destroyAllWindows


    # Configuration for gmail email address

    ###############################################################################
    # FOR SMTP AND PORT INFROMATION: GOOGLE =>>  <YOUR EMAIL PROVIDER> smtp settings
    # THIS SHOULD RESOLVE ANY CONNECTION ERRORS
    # PLEASE SUBMIT ISSUE REPORT IF YOU CANNOT RESOLVE THIS CONNECTION
    ###############################################################################

    eobj = smtplib.SMTP("smtp.gmail.com", 587)
    
    print eobj.starttls()


    # Get Email Login info
    print 
    print "You must first log in"
    print 
    
    # For security, I have opted to make this an open variable
    #NOTE THIS SCRIPT WILL RETURN AN ERROR OF EMAILLOGIN AND EMAILPASSWORD ARE NOT UPDATED 
    emailLogin = "ChangeThisStringToYourEmail@gmail.com"
    emailPassword = "AndHereGoesYourPasswordForGmail.com"
    
    # WHOLE PATH
    attachment = open("last_capture.jpg", "rb")
    # ONLY FILE
    filename = "last_capture.jpg"

    part = MIMEBase("application", "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    msg = MIMEMultipart()
    part.add_header("Content-Disposition", "attachment; filename= %s" % filename)
    msg.attach(part)
    text = msg.as_string()


    print eobj.login(emailLogin, emailPassword)

    print "Face Detected"
    eobj.sendmail(emailLogin, emailLogin, text)
    print "Notifications and Attachments Have Been Sent To The Owner Of This Computer."
    print "If you would like to email the owner, directly, please email: {} ".format(emailLogin)
    print"_________________________________________"

