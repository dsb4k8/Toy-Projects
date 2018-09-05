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
    


    face_cascade = cv2.CascadeClassifier("/YOUR/PATH/TO/haarcascades/haarcascade_frontalface_default.xml")

    eye_cascade  = cv2.CascadeClassifier("/YOUR/PATH/TO/haarcascades/haarcascade_eye.xml")

    smile_cascade = cv2.CascadeClassifier("/YOUR/PATH/TO/haarcascades/haarcascade_.xml")
    

    # START CAPUTRE
    cap = cv2.VideoCapture(0)
    
    # LISTEN, LOCATE, AND SAVE FACIAL STRUCTURES
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y), (x+w, y+h), (255,0,0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color= img[y:y+h, x:x+w]

            # To Save in same directory, leave as file name only
            cv2.imwrite("result.jpg", img)
            break
            
            eyes = eye_cascade.detectMultiScale(roi_gray)

            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0),2)

        cv2.imshow("img", img)
        
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    # Input a second location to save image file
    cv2.imwrite("/WHERE/TO/SAVE/A/SECOND/COPY/CALLED/this_is_an_example.jpg", img)
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
    emailLogin = raw_input("Please Enter Your Email Address: ")
    emailPassword = raw_input("Please Enter Your Password: ")
    
    # WHOLE PATH
    attachment = open("/PATH/TO/YOUR/FILENAME.EXTENSION", "rb")
    # ONLY FILE
    filename = "FILENAME.EXTENSION"

    part = MIMEBase("application", "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    msg = MIMEMultipart()
    part.add_header("Content-Disposition", "attachment; filename= %s" % filename)
    msg.attach(part)
    text = msg.as_string()


    print eobj.login(emailLogin, emailPassword)

    print "Face Detected: {}".format(time.now())
    eobj.sendmail(emailLogin, emailLogin, text)
    print "Notifications and Attachments Have Been Sent To The Owner Of This Computer."
    print "If you would like to email the owner, directly, please email: {} ".format(emailLogin)
    print"_________________________________________"

