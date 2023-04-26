from cProfile import label
from cgitb import text
from email.headerregistry import Address
from pydoc import TextDoc
from sqlite3 import Row
import string
from tkinter import *
from  tkinter import ttk
from tkinter.tix import COLUMN
from turtle import circle, width
from PIL import Image, ImageTk
 
class Attandace_Detail:
    def __init__(self,root):
        self.root = root 
        self.root.geometry("1590x790+0+0")
        self.root.title("Face Recognization")

    # Upper image
        img =Image.open(r"img\Top_img.jpg" )
        img = img.resize((530,130), Image.ANTIALIAS)
        self.photoImage = ImageTk.PhotoImage(img)
        self.img_l1 = Label(self.root,image=self.photoImage)
        self.img_l1.place(x=0,y=0,height=130,width=530)

        img1 =Image.open(r"img\Top.jpg" )
        img1 = img1.resize((530,130), Image.ANTIALIAS)
        self.photoImage1 = ImageTk.PhotoImage(img1)
        self.img_l2 = Label(self.root,image=self.photoImage1)
        self.img_l2.place(x=530,y=0,height=130,width=530)

        img2 =Image.open(r"img\Top.jpg" )
        img2 = img2.resize((530,130), Image.ANTIALIAS)
        self.photoImage2 = ImageTk.PhotoImage(img2)
        self.img_l3 = Label(self.root,image=self.photoImage2)
        self.img_l3.place(x=1060,y=0,height=130,width=530)

    
        # Bg images 
        bg =Image.open(r"img\Top_img.jpg")
        bg = bg.resize((1590,660), Image.LANCZOS)
        self.photoImage3 = ImageTk.PhotoImage(bg)
        self.img_l4 = Label(self.root,image=self.photoImage3)
        self.img_l4.place(x=0,y=130,height=660,width=1590)

         # heading 
        self.l_heading= Label(self.img_l4, text="Students Details" ,background="Navy",font="comicsansms 25 bold",borderwidth=3 , fg= "yellow",relief=SUNKEN)
        self.l_heading.place(x=0,y=0,width=1590 ,height=50)

        # Frame
        self.main_frame =Frame(self.img_l4,bd=2,background="White")
        self.main_frame.place(x=20,y=60 ,width=1550,height=580)

        # Frame
        self.left_frame =LabelFrame(self.main_frame,bd=2,background="white",relief=RIDGE ,text="Student Detail",font="comicsansms 10 bold")
        self.left_frame.place(x=10,y=10 ,width=765,height=550)

        self.right_frame =LabelFrame(self.main_frame,bd=2,background="white",relief=RIDGE ,text="Student Detail",font="comicsansms 10 bold")
        self.right_frame.place(x=785,y=10 ,width=755,height=550)

        # Leftframe content 
        img4 =Image.open("face.jpg" )
        img4 = img4.resize((765,130), Image.ANTIALIAS)
        self.photoImage4 = ImageTk.PhotoImage(img4)
        self.Le_img_l3 = Label(self.left_frame,image=self.photoImage4)
        self.Le_img_l3.place(x=0 ,y=0,height=80,width=765)
    
        self.Current_course= LabelFrame(self.left_frame , text="Current Course", relief=RIDGE ,font="comicsansms 10 bold" , background="white" )
        self.Current_course.place(x=10 , y=80 ,height=100 ,width=745 )

        self.Dept = Label(self.Current_course , text= "Deparment :", font="comicsansms 12 bold ")
        self.Dept.grid(row=0 ,column=0,padx=10 ,pady=3)

        dep_combo = ttk.Combobox(self.Current_course , font="comicsansms 12 bold " ,state="readonly")
        dep_combo["values"] =["Select Deparment", "Computer","IT","ECS","EXTC"] 
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1 ,padx=5 ,pady=3 ,sticky=W)

        self.Class = Label(self.Current_course , text= "Class :", font="comicsansms 12 bold ")
        self.Class.grid(row=0 ,column=3,padx=10 ,pady=3)


        Class_combo = ttk.Combobox(self.Current_course , font="comicsansms 12  bold " ,state="readonly")
        Class_combo["values"] =["Select Class", "FE","SE","TE","Final year"] 
        Class_combo.current(0)
        Class_combo.grid(row=0, column=4 ,padx=3 ,pady=3 ,sticky=W)


        self.year = Label(self.Current_course , text= "Year :", font="comicsansms 12 bold ")
        self.year.grid(row=1 ,column=0,padx=2 ,pady=3)


        year_combo = ttk.Combobox(self.Current_course , font="comicsansms 12  bold " ,state="readonly" ,background="white")
        year_combo["values"] =["Select Year", "2020-21","2021-22","2022-23","2023-24"] 
        year_combo.current(0)
        year_combo.grid(row=1, column=1 ,padx=3 ,pady=3 ,sticky=W)  


        self.Semester = Label(self.Current_course , text= "Semester :", font="comicsansms 12 bold ")
        self.Semester.grid(row=1 ,column=3,padx=3 ,pady=3)


        Semester_combo = ttk.Combobox(self.Current_course , font="comicsansms 12  bold " ,state="readonly")
        Semester_combo["values"] =["Select Semester", "Semester-1","Semester-2","Semester-3","Semester-4" ,"Semester-5" ,"Semester-6","Semester-7","Semester-8"] 
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=4 ,padx=3 ,pady=3 ,sticky=W)
        # Class student information 
        self.Student_info= LabelFrame(self.left_frame , text="Student information", relief=RIDGE ,font="comicsansms 10 bold" , background="white" )
        self.Student_info.place(x=10 , y=190 ,height=330 ,width=745 )


        Studentid = Label(self.Student_info ,text="StudentId",font="comicsansms 12 bold ",background="white")
        Studentid.grid(row=1 ,column=1,padx=3 ,pady=3)
        studentvalue= IntVar()
        studentnamevalue = StringVar()
        CLassdivisonvalue =StringVar()
        RollNoValue = IntVar()
        GenderValue = StringVar()
        Emailvalue =StringVar()
        Phonevalue =IntVar()
        AddressValue =StringVar()
        Teachervalue =StringVar()

        Studentid_input= Entry(self.Student_info,font="comicsansms 12 bold ",textvariable=studentvalue)
        Studentid_input.grid(row=1 ,column=2)

        Studentname = Label(self.Student_info ,text="Student name",font="comicsansms 12 bold ",background="white")
        Studentname.grid(row=1 ,column=3,padx=5 ,pady=3)
        Studentname_input= Entry(self.Student_info,font="comicsansms 12 bold ",textvariable=studentnamevalue)
        Studentname_input.grid(row=1 ,column=4)

        StudentDivsion = Label(self.Student_info ,text=" Divsion",font="comicsansms 12 bold ",background="white")
        StudentDivsion.grid(row=2 ,column=1,padx=5 ,pady=3)
        StudentDivsion_input= Entry(self.Student_info,font="comicsansms 12 bold ",textvariable=CLassdivisonvalue)
        StudentDivsion_input.grid(row=2 ,column=2)


        StudentRoll = Label(self.Student_info ,text=" Roll",font="comicsansms 12 bold ",background="white")
        StudentRoll.grid(row=2 ,column=3,padx=5 ,pady=3)
        StudentRoll_input= Entry(self.Student_info,font="comicsansms 12 bold ",textvariable=RollNoValue)
        StudentRoll_input.grid(row=2 ,column=4)


        StudentGender = Label(self.Student_info ,text=" Gender",font="comicsansms 12 bold ",background="white")
        StudentGender.grid(row=3 ,column=1,padx=5 ,pady=3)
        StudentGender_input= Entry(self.Student_info,font="comicsansms 12 bold ",textvariable=GenderValue)
        StudentGender_input.grid(row=3 ,column=2)


        StudentEmail = Label(self.Student_info ,text=" Email",font="comicsansms 12 bold ",background="white")
        StudentEmail.grid(row=3 ,column=3,padx=5 ,pady=3)
        StudentEmail_input= Entry(self.Student_info,font="comicsansms 12 bold ",textvariable=Emailvalue)
        StudentEmail_input.grid(row=3 ,column=4)


        StudentPhone_no = Label(self.Student_info ,text=" Phone No ",font="comicsansms 12 bold ",background="white")
        StudentPhone_no.grid(row=4 ,column=1,padx=5 ,pady=3)
        StudentPhone_no_input= Entry(self.Student_info,font="comicsansms 12 bold ",textvariable=Phonevalue)
        StudentPhone_no_input.grid(row=4 ,column=2)


        StudentAdress = Label(self.Student_info ,text="Address",font="comicsansms 12 bold ",background="white")
        StudentAdress.grid(row=4 ,column=3,padx=5 ,pady=3)
        StudentAdress_input= Entry(self.Student_info,font="comicsansms 12 bold ",textvariable=AddressValue)
        StudentAdress_input.grid(row=4 ,column=4)


        Student_Teachername = Label(self.Student_info ,text="Teacher name",font="comicsansms 12 bold ",background="white")
        Student_Teachername.grid(row=5 ,column=1,padx=5 ,pady=3)
        Student_Teachername_input= Entry(self.Student_info,font="comicsansms 12 bold ",textvariable=Teachervalue)
        Student_Teachername_input.grid(row=5 ,column=2)


        R_button = Radiobutton(self.Student_info ,text=" Take photo sample",font="comicsansms 10 bold " , background="white" )
        R_button.grid( row=6 ,column=1 ,padx=5 ,pady=3)

        R2_button = Radiobutton(self.Student_info ,text=" No photo sample",font="comicsansms 10 bold " , background="white")
        R2_button.grid( row=6 ,column=2 ,padx=3 ,pady=3)


        Btn_save = Button (self.Student_info,text="Save",background="White",font="comicsansms 11 bold",borderwidth=3 , fg= "White",relief=SUNKEN,bg="Blue",height=2,width=19)
        Btn_save.grid( row= 7 ,column=1 )

        Btn_save = Button (self.Student_info,text="Reset",background="White",font="comicsansms 11 bold",borderwidth=3 , fg= "White",relief=SUNKEN,bg="Blue",height=2,width=19)
        Btn_save.grid( row= 7 ,column=2 )

        Btn_save = Button (self.Student_info,text="Delete",background="White",font="comicsansms 11 bold",borderwidth=3 , fg= "White",relief=SUNKEN,bg="Blue",height=2,width=19)
        Btn_save.grid( row= 7 ,column=3 )

        Btn_save = Button (self.Student_info,text="Reset",background="White",font="comicsansms 11 bold",borderwidth=3 , fg= "White",relief=SUNKEN,bg="Blue",height=2,width=19)
        Btn_save.grid( row= 7 ,column=4 )

        Btn_save = Button (self.Student_info,text="Take photo sample",background="White",font="comicsansms 11 bold",borderwidth=3 , fg= "White",relief=SUNKEN,bg="Blue")
        Btn_save.place( x=0, y=240,height=40,width=370)

        Btn_save = Button (self.Student_info,text="Update Phot sample",background="White",font="comicsansms 11 bold",borderwidth=3 , fg= "White",relief=SUNKEN,bg="Blue")
        Btn_save.place( x=360 ,y=240,height=40,width=370)


                # ========================Generate data set or take photo samples   ===============================================================================================

        # def generate_dataset(self):




        

        # ===============================================Load Predefined data on face frontals from opencv=========================================================


      #  face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    #     def face_cropped(imp):
    #         gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #         faces=face_classifier.detectMultiScale(gray,1.3,5)
    #         #scaling factor=1.3
    #         #Minimum Neighbor=5

    #         for (x,y,w,y) in faces:
    #             face_cropped=img[y:y+h,x:x+w]
    #             return face_cropped

    #     cap=cv2.VideoCapture(0)
    #     img_id=0
    #     while True:
    #         ret,my_frame=cap.read()
    #         if face_cropped(my_frame) is not None:
    #             img_id+=1
    #         face=cv2.resize(face_cropped(my_frame),(450,450))
    #         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
    #         file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
    #         cv2.imwrite(file_name_path)
    #         cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
    #         cv2.imshow("Cropped Face",face)

    #         if cv2.waitKey(1)==13 or int(img_id)==100:
    #             break
    #     cap.release()
    #     cv2.destroyAllWindows()
    #     messagebox.showinfo("Result","Generating data sets completed!!!!")
    # except    




if __name__ == "__main__":
    root=Tk()
    obj=Attandace_Detail(root)
    root.mainloop()