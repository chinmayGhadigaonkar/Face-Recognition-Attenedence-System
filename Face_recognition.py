from cProfile import label
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
import mysql.connector
import cv2
from datetime import datetime
from time import strftime 
import os
# import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1590x790+0+0")
        self.root.title("Face Recognition System")

        # ==============================Labe; from traindata========================================
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=(
            "times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1590, height=45)

        img_top = Image.open(r"img\Fc.jpg")
        img_top = img_top.resize((650, 800), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=800)

        img_bottom = Image.open(r"face.jpg")
        img_bottom = img_bottom.resize((950, 800), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=800)

        # ==========button===========================
        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", font=(
            "times new roman", 18, "bold"), bg="blue", fg="white", command=self.face_recog)
        b1_1.place(x=365, y=620, width=200, height=40)


    def face_recog(self):
        def draw_boundry(img, classifier, scalefactor, minNeighbours, color, text, clf):
            grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            feature = classifier.detectMultiScale(
                grey_img, scalefactor, minNeighbours)

            coords = []

            for (x, y, w, h) in feature:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(grey_img[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host='localhost', user='root', password='rootpassword', port="3310", database='new')
                my_cursor = conn.cursor()

                

                my_cursor.execute(
                    "select student_name from attandance_management_system  where  student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute(
                    "select Department from attandance_management_system  where  student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute(
                    "select Roll_No from attandance_management_system  where  student_id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)
                my_cursor.execute(
                    "select student_id from attandance_management_system  where  student_id="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)
                
                if confidence > 77:
                    cv2.putText(
                        img, f"Id:{i}", (x, y-85), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                    cv2.putText(
                        img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                    cv2.putText(
                        img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                    cv2.putText(
                        img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                    self.mark_attendance(i,r,n,d)

                

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

                coords = [x, y, w, y]
            return coords

        def recognizer(img, clf, faceCascade):
            coords = draw_boundry(img, faceCascade, 1.1,
                                  10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("face_recog.xml")

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img1 = recognizer(img, clf, faceCascade)
            cv2.imshow("Welcome to face recognition", img1)

            if cv2.waitKey(1) == 13:
                break
                
        video_cap.release()
        cv2.destroyAllWindows()

    # def mark_attendance(self,i,r,n,d):
    #     already_in_file = set()
    #     with open('atten.csv','r+',newline="\n") as f:
    #         for line in f:
    #             already_in_file.add(line.split(",")[0])
    #     if((i not in already_in_file) and (r not in already_in_file) and (n not in already_in_file) and (d not in already_in_file)):
    #         with open('atten.csv','r+',newline="\n") as f:    
    #             now=datetime.now()
    #             d1=now.strftime("%d/%m/%Y")
    #             dtString=now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")


    def mark_attendance(self,i,r,n,d):
        already_in_file = set()
        with open('atten.csv','r+',newline="\n") as f:
            for line in f:
                already_in_file.add(line.split(",")[0])
            if((i not in already_in_file) and (r not in already_in_file) and (n not in already_in_file) and (d not in already_in_file)):  
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
