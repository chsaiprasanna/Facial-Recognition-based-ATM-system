from tkinter import *
import tkinter as tk
import face_recognition
import cv2
import numpy
import os
import sys
from tkinter import ttk
from PIL import ImageTk, Image


   

a=Tk()

lb1=Label(a,text="   WELCOME  ",font=("Times",40))
lb1.pack(padx=30,pady=30)

lb2=Label(a,text="   TO YOUR TRUSTED BANK",font=("Times",35))
lb2.pack(padx=40,pady=90)
lb3=Label(a,text="Press NEXT to login through face recognition",font=("Times",25))
lb3.pack(padx=50,pady=140)






def link():
    video_capture = cv2.VideoCapture(0)
    ratan_tata_image = face_recognition.load_image_file("photos/ratan_tata.jpg")
    ratan_tata_encoding= face_recognition.face_encodings(ratan_tata_image)[0]
    SAI1_image=face_recognition.load_image_file("photos/SAI1.jpeg")
    SAI1_encoding=face_recognition.face_encodings(SAI1_image)[0]

    known_face_encoding = [ratan_tata_encoding,SAI1_encoding]
    known_faces_names = ["ratan_tata","SAI1"]
    students =known_faces_names.copy()

    face_locations = []
    face_encodings = []
    face_names = []
    s = True

    i=1
    while i<2:
        
        _,frame = video_capture.read()
        small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
        rgb_small_frame=small_frame[:,:,::-1]
        if s:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings=face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = [ ]
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
                name = ""
                face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
                best_match_index = numpy.argmin(face_distance)
                if matches[best_match_index]:
                    name = known_faces_names[best_match_index]
                face_names.append(name)
                if name in known_faces_names:
                    if name in students:
                        print("Welcome Prasanna")
                        password=int(input("Enter your pin"))
                        if password==4455:
                            balance=3000
                            print("select one operation \n 1.deposit\n2.withdraw\n 3.enquiry")
                            op=int(input("Enter your option"))
                            if op==1:
                                amt=int(input("Enter amount to deposit"))
                                balance+=amt
                                print("Net Balance=",balance)
                                print("**THANK YOU**")
                            elif op==2:
                                amt=int(input("Enter amount to withdraw"))
                                if amt>balance:
                                    print("Insufficient balance")
                                else:
                                    balance-=amt
                                    print("Net Balance=",balance)
                                    print("**THANK YOU**")
                            elif op==3:
                                print("Net Balance=",balance)
                                print("**THANK YOU**")
                                
                            
                              
                                
                        else:
                            print("Wrong pin!!!")
                else:
                    print("***USER NOT FOUND***")
                    i=i+1
                    break
               
                
                    
                
        cv2.imshow("video_live",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



btn1=Button(a,text ="NEXT",command=link)
btn1.pack(padx=100,pady=60)
a.after(10000,lambda:a.destroy())
a.mainloop()
    
video_capture.release()
cv2.destroyAllWindows()



    
