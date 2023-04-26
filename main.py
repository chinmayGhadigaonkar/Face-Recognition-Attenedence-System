from cProfile import label
from tkinter import *
from  tkinter import ttk
from PIL import Image, ImageTk
from setuptools import Command
from attendence import Attandace_Detail
from Face_recognition import Face_Recognition
from train_data import Train_Data
from ecdnetta import Attendance
import os
 
class Face_Recognization_System:
    def __init__(self,root):
        self.root = root 
        self.root.geometry("1590x790+0+0")
        self.root.title("Face Recognization")

        # Upper image
        img =Image.open(r"img\Top_img.jpg" )
        img = img.resize((530,130),	
Image.Resampling.LANCZOS)
        self.photoImage = ImageTk.PhotoImage(img)
        self.img_l1 = Label(self.root,image=self.photoImage)
        self.img_l1.place(x=0,y=0,height=130,width=530)

        img1 =Image.open(r"img/3.jpg" )
        img1 = img1.resize((530,130), 	
Image.Resampling.LANCZOS)
        self.photoImage1 = ImageTk.PhotoImage(img1)
        self.img_l2 = Label(self.root,image=self.photoImage1)
        self.img_l2.place(x=530,y=0,height=130,width=530)

        img2 =Image.open("face.jpg" )
        img2 = img2.resize((530,130), 	
Image.Resampling.LANCZOS)
        self.photoImage2 = ImageTk.PhotoImage(img2)
        self.img_l3 = Label(self.root,image=self.photoImage2)
        self.img_l3.place(x=1060,y=0,height=130,width=530)

        # Bg images 
        bg =Image.open(r"img\Fc.jpg")
        bg = bg.resize((1590,660), 	
Image.Resampling.LANCZOS)
        self.photoImage3 = ImageTk.PhotoImage(bg)
        self.img_l4 = Label(self.root,image=self.photoImage3)
        self.img_l4.place(x=0,y=130,height=660,width=1590)

        # heading 
        self.l_heading= Label(self.img_l4, text="Student Attendence Mangement System" ,background="blue",font="comicsansms 32 bold",borderwidth=3 , fg= "White",relief=SUNKEN)
        self.l_heading.place(x=0,y=0,width=1590 ,height=60)


        # body 
        # body-top
        # Section1
        img_b2 =Image.open(r"img\Stu_detail.png")
        img_b2 = img_b2.resize((400,180), 	
Image.Resampling.LANCZOS)
        self.photoImage4 = ImageTk.PhotoImage(img_b2)
        self.img_l5 = Button(self.img_l4,image=self.photoImage4,command=self.student_detail)
        self.img_l5.place(x=100,y=100,height=180,width=400)

        self.l_btn1= Button(self.img_l4, text="Student Detail",command=self.student_detail,background="White",font=('Times New Roman',12,'bold'),borderwidth=3 , fg= "White",relief=SUNKEN,bg="Blue")
        self.l_btn1.place(x=100,y=280,width=400 ,height=40)
        
        # Section 2
        img_b3 =Image.open("face_recog.jpg")
        img_b3 = img_b3.resize((400,180), 	
Image.Resampling.LANCZOS)
        self.photoImage5 = ImageTk.PhotoImage(img_b3)
        self.img_l5 = Button(self.img_l4,image=self.photoImage5,command=self.face_recogniation)
        self.img_l5.place(x=600,y=100,height=180,width=400)
   

        self.l_btn2= Button(self.img_l4, text="Face Recognization  ",command=self.face_recogniation , background="White",font=('Times New Roman',12,'bold'),borderwidth=3 , fg= "White",relief=SUNKEN,bg="Blue")
        self.l_btn2.place(x=600,y=280,width=400 ,height=40)

        # Section 3 
        img_b4 =Image.open(r"img\attendance.jpg")
        img_b4 = img_b4.resize((400,180), 	
Image.Resampling.LANCZOS)
        self.photoImage6 = ImageTk.PhotoImage(img_b4)
        self.img_l5 = Label(self.img_l4,image=self.photoImage6)
        self.img_l5.place(x=1100,y=100,height=180,width=400)

        self.l_btn3= Button(self.img_l4, text="Attendance" ,background="White",font=('Times New Roman',12,'bold'),borderwidth=3 , fg= "White",relief=SUNKEN,bg="Blue" ,command= self.Attendence)
        self.l_btn3.place(x=1100,y=280,width=400 ,height=40)


        # Body-Bottom
        img_b4 =Image.open(r"img\training data.png" )
        img_b4 = img_b4.resize((400,180),	
Image.Resampling.LANCZOS)
        self.photoImage7 = ImageTk.PhotoImage(img_b4)
        self.img_l6 = Label(self.img_l4,image=self.photoImage7  )
        self.img_l6.place(x=100,y=350,height=180,width=400)

        self.l_btn4= Button(self.img_l4, text="Train Data" , command=self.Train_Data, background="White",font=('Times New Roman',12,'bold'),borderwidth=3 , fg= "White",relief=SUNKEN,bg="Blue")
        self.l_btn4.place(x=100,y=530,width=400 ,height=40)


        img_b5 =Image.open(r"img\Photos.png" )
        img_b5 = img_b5.resize((400,180),	
Image.Resampling.LANCZOS)
        self.photoImage8 = ImageTk.PhotoImage(img_b5)
        self.img_l7 = Button(self.img_l4,image=self.photoImage8 , command = self.open_img)
        self.img_l7.place(x=600,y=350,height=180,width=400)

        self.l_btn5= Button(self.img_l4, text="Photos" ,background="White",font=('Times New Roman',12,'bold'),borderwidth=3 , fg= "White",relief=SUNKEN,bg="Blue",command=self.open_img)
        self.l_btn5.place(x=600,y=530,width=400 ,height=40)

        img_b6 =Image.open(r"img\exit.jpg" )
        img_b6 = img_b6.resize((400,180), 	
Image.Resampling.LANCZOS)
        self.photoImage9 = ImageTk.PhotoImage(img_b6)
        self.img_l6 = Button(self.img_l4,image=self.photoImage9,command=self.clickExitButton)
        self.img_l6.place(x=1100,y=350,height=180,width=400)

        self.l_btn6= Button(self.img_l4, text="Exit" ,background="White",font=('Times New Roman',12,'bold'),borderwidth=3 , fg= "White",relief=SUNKEN,bg="Blue" ,command=self.clickExitButton)
        self.l_btn6.place(x=1100,y=530,width=400 ,height=40)

      

      


    def student_detail(self):
      self.new_window =Toplevel(self.root)
      self.app =Attandace_Detail(self.new_window)
    
    def face_recogniation(self):
      self.new_window=Toplevel(self.root)
      self.app = Face_Recognition(self.new_window)

    def Train_Data(self):
      self.new_window=Toplevel(self.root)
      self.app = Train_Data(self.new_window)
    def Attendence(self):
      self.new_window=Toplevel(self.root)
      self.app = Attendance(self.new_window)

    def open_img(self):
      os.startfile("Data")

    def clickExitButton(self):
        exit()


    
    




if __name__ == "__main__":
  root =Tk()
  obj = Face_Recognization_System(root)
  root.mainloop()




# def face_data(self):
#     self.new_window=Toplevel(self.root)
#     self.app=Face_Recognition(self.new_window)
