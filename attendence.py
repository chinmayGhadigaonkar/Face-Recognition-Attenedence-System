from cProfile import label
from cgitb import text
from email import message
from email.headerregistry import Address
from msilib.schema import tables
from multiprocessing.sharedctypes import Value
from pydoc import TextDoc
from sqlite3 import Row
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
# from tkinter.tix import COLUMN
from turtle import circle, width
from PIL import Image, ImageTk
import cv2
import os
from cv2 import QT_NEW_BUTTONBAR
import mysql.connector
from numpy import rint


class Attandace_Detail:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1590x790+0+0")
        self.root.title("Face Recognization")

    # Upper image
        img = Image.open(r"img\images.jpeg")
        img = img.resize((530, 130), Image.Resampling.LANCZOS)
        self.photoImage = ImageTk.PhotoImage(img)
        self.img_l1 = Label(self.root, image=self.photoImage)
        self.img_l1.place(x=0, y=0, height=130, width=530)

        img1 = Image.open(r"img\bg_Student_Detail.jpg")
        img1 = img1.resize((530, 130), 	Image.Resampling.LANCZOS)
        self.photoImage1 = ImageTk.PhotoImage(img1)
        self.img_l2 = Label(self.root, image=self.photoImage1)
        self.img_l2.place(x=530, y=0, height=130, width=530)

        img2 = Image.open(r"img\Attandance.jpg")
        img2 = img2.resize((530, 130), 	Image.Resampling.LANCZOS)
        self.photoImage2 = ImageTk.PhotoImage(img2)
        self.img_l3 = Label(self.root, image=self.photoImage2)
        self.img_l3.place(x=1060, y=0, height=130, width=530)

        # Bg images
        bg = Image.open(r"img\Student_bg_img.jpg")
        bg = bg.resize((1590, 660),	
Image.Resampling.LANCZOS)
        self.photoImage3 = ImageTk.PhotoImage(bg)
        self.img_l4 = Label(self.root, image=self.photoImage3)
        self.img_l4.place(x=0, y=130, height=660, width=1590)

        # heading
        self.l_heading = Label(self.img_l4, text="STUDENTS DETAIL ", background="Navy",
                         font=('Times New Roman',25,'bold'), borderwidth=3, fg="yellow", relief=SUNKEN)
        self.l_heading.place(x=0, y=0, width=1590, height=50)

        # Frame
        self.main_frame = Frame(self.img_l4, bd=2, background="White")
        self.main_frame.place(x=20, y=60, width=1550, height=580)

        # Frame
        self.left_frame = LabelFrame(self.main_frame, bd=2, background="white",
                                     relief=RIDGE, text="Student Detail", font=('Times New Roman',10,'bold'))
        self.left_frame.place(x=10, y=10, width=765, height=550)

        self.right_frame = LabelFrame(self.main_frame, bd=2, background="white",
                                      relief=RIDGE, text="Student Detail", font=('Times New Roman',10,'bold'))
        self.right_frame.place(x=785, y=10, width=755, height=550)

        # Leftframe content
        img4 = Image.open(r"img\images.jpeg")
        img4 = img4.resize((755, 130), 	Image.Resampling.LANCZOS)
        self.photoImage4 = ImageTk.PhotoImage(img4)
        self.Le_img_l3 = Label(self.left_frame, image=self.photoImage4)
        self.Le_img_l3.place(x=0, y=0, height=100, width=755)
    #   Current course
        self.Current_course = LabelFrame(
            self.left_frame, text="Current Course", relief=RIDGE, font=('Times New Roman',10,'bold'), background="white")
        self.Current_course.place(x=10, y=100, height=100, width=745)

     # vaiable
        self.Deparment_1 = StringVar()
        self.class_var = StringVar()
        self.year_1 = StringVar()
        self.semester_1 = StringVar()
        self.student_id_1 = StringVar()
        self.student_name_1 = StringVar()
        self.division_1 = StringVar()
        self.Roll_No_1 = StringVar()
        self.gender_1 = StringVar()
        self.Email_1 = StringVar()
        self.Phone_no_1 = StringVar()
        self.Address_1 = StringVar()
        self.Teacher_name_1 = StringVar()
        self.photos_var =StringVar()

        self.Dept = Label(self.Current_course,
                          text="Department :", font=('Times New Roman',13,'bold'),background="white")
        self.Dept.grid(row=1, column=1, padx=35, pady=3)

        dep_combo = ttk.Combobox(self.Current_course, textvariable=self.Deparment_1,font=('Times New Roman',12,'bold'), state="readonly")
        dep_combo["values"] = ["Select Deparment",
                               "Computer", "IT", "ECS", "EXTC"]
        dep_combo.current(0)
        dep_combo.grid(row=1, column=2, padx=2, pady=3, sticky=W)

        self.Class = Label(self.Current_course, text="Class :",
                           font=('Times New Roman',12,'bold'),background="white")
        self.Class.grid(row=1, column=3, padx=10, pady=2)

        Class_combo = ttk.Combobox(
            self.Current_course, textvariable=self.class_var, font=('Times New Roman',12,'bold'), state="readonly")
        Class_combo["values"] = ["Select Class",
                                 "FE", "SE", "TE", "Final year"]
        Class_combo.current(0)
        Class_combo.grid(row=1, column=4, padx=10, pady=2, sticky=W)

        self.year = Label(self.Current_course, text="Year :",
                          font=('Times New Roman',12,'bold') ,background="white")
        self.year.grid(row=2, column=1, padx=10, pady=3)

        year_combo = ttk.Combobox(self.Current_course, font=('Times New Roman',12,'bold'),
                                  state="readonly", background="white", textvariable=self.year_1)
        year_combo["values"] = ["Select Year",
                                "2020-21", "2021-22", "2022-23", "2023-24"]
        year_combo.current(0)
        year_combo.grid(row=2, column=2, padx=4, pady=3, sticky=W)

        self.Semester = Label(self.Current_course,
                              text="Semester :", font=('Times New Roman',12,'bold') ,background="white")
        self.Semester.grid(row=2, column=3, padx=10, pady=3)

        Semester_combo = ttk.Combobox(
            self.Current_course, font=('Times New Roman',12,'bold'), state="readonly", textvariable=self.semester_1)
        Semester_combo["values"] = ["Select Semester", "Semester-1", "Semester-2",
                                    "Semester-3", "Semester-4", "Semester-5", "Semester-6", "Semester-7", "Semester-8"]
        Semester_combo.current(0)
        Semester_combo.grid(row=2, column=4, padx=10, pady=3, sticky=W)

        # Class student information
        
        self.Student_info = LabelFrame(self.left_frame, text="Student information",
                                       relief=RIDGE, font=('Times New Roman',12,'bold'), background="white")
        self.Student_info.place(x=10, y=210, height=315, width=745)

        Studentid = Label(self.Student_info, text="Student Id :",
                          font=('Times New Roman',12,'bold'), background="white")
        Studentid.grid(row=1, column=1, padx=2, pady=2)
        Studentid_input = Entry(
        self.Student_info, font=('Times New Roman',12,'bold'), textvariable=self.student_id_1,highlightthickness=1, highlightcolor= "Black",highlightbackground = "grey")
        # Studentid_input.grid(row=1, column=2)
        Studentid_input.grid(row=1, column=2, padx=5, pady=3)

        Studentname = Label(self.Student_info, text="Student Name:",
                            font=('Times New Roman',12,'bold'), background="white")
        Studentname.grid(row=1, column=3, padx=5, pady=3)
        Studentname_input = Entry(
            self.Student_info, font=('Times New Roman',12,'bold'), textvariable=self.student_name_1 ,highlightthickness=1, highlightcolor= "Black",highlightbackground = "grey")
        Studentname_input.grid(row=1, column=4 )

        StudentDivsion = Label(self.Student_info, text=" Division:",
                               font=('Times New Roman',12,'bold'), background="white")
        StudentDivsion.grid(row=2, column=1, padx=5, pady=3)
        StudentDivsion_input = Entry(
            self.Student_info, font=('Times New Roman',12,'bold'), textvariable=self.division_1 ,highlightthickness=1, highlightcolor= "Black",highlightbackground = "grey")
        StudentDivsion_input.grid(row=2, column=2)

        StudentRoll = Label(self.Student_info, text=" Roll No :",
                            font=('Times New Roman',12,'bold'), background="white")
        StudentRoll.grid(row=2, column=3, padx=5, pady=3)
        StudentRoll_input = Entry(
            self.Student_info, font=('Times New Roman',12,'bold'), textvariable=self.Roll_No_1 ,highlightthickness=1, highlightcolor= "Black",highlightbackground = "grey")
        StudentRoll_input.grid(row=2, column=4)

        StudentGender = Label(self.Student_info, text=" Gender :",
                              font=('Times New Roman',12,'bold'), background="white")
        StudentGender.grid(row=3, column=1, padx=5, pady=3)
        # StudentGender_input = Entry(
        #     self.Student_info, font=('Times New Roman',12,'bold'), textvariable=self.gender_1 ,highlightthickness=1, highlightcolor= "Black",highlightbackground = "grey")
        # StudentGender_input.grid(row=3, column=2)


        STUDENT_GENDER_combo = ttk.Combobox(self.Student_info, font=('Times New Roman',12,'bold'),
                                  state="readonly", background="white", textvariable=self.gender_1 ,width=18)
        STUDENT_GENDER_combo["values"] = ["Select Gender",
                                "Male", "Female", "Other"]
        STUDENT_GENDER_combo.current(0)
        STUDENT_GENDER_combo.grid(row=3, column=2,  padx=5, sticky=W)

        StudentEmail = Label(self.Student_info, text=" Email:",
                             font=('Times New Roman',12,'bold'), background="white")
        StudentEmail.grid(row=3, column=3, padx=5, pady=3)
        StudentEmail_input = Entry(
            self.Student_info, font=('Times New Roman',12,'bold'), textvariable=self.Email_1 ,highlightthickness=1, highlightcolor= "Black",highlightbackground = "grey")
        StudentEmail_input.grid(row=3, column=4)

        StudentPhone_no = Label(self.Student_info, text=" Phone No: ",
                                font=('Times New Roman',12,'bold'), background="white")
        StudentPhone_no.grid(row=4, column=1, padx=5, pady=3)
        StudentPhone_no_input = Entry(
            self.Student_info, font=('Times New Roman',12,'bold'), textvariable=self.Phone_no_1 ,highlightthickness=.5, highlightcolor= "Black",highlightbackground = "grey")
        StudentPhone_no_input.grid(row=4, column=2)

        StudentAdress = Label(self.Student_info, text="Address:",
                              font=('Times New Roman',12,'bold'), background="white")
        StudentAdress.grid(row=4, column=3, padx=5, pady=3)
        StudentAdress_input = Entry(
            self.Student_info, font=('Times New Roman',12,'bold'), textvariable=self.Address_1 ,highlightthickness=.5, highlightcolor= "Black",highlightbackground = "grey")
        StudentAdress_input.grid(row=4, column=4)

        Student_Teachername = Label(
        self.Student_info, text="Teacher Name:", font=('Times New Roman',12,'bold'), background="white")
        Student_Teachername.grid(row=5, column=1, padx=5, pady=3)
        Student_Teachername_input = Entry(
        self.Student_info, font=('Times New Roman',12,'bold'), textvariable=self.Teacher_name_1 ,highlightthickness=.5, highlightcolor= "Black",highlightbackground = "grey")
        Student_Teachername_input.grid(row=5, column=2)
        

        R_button = ttk.Radiobutton(self.Student_info ,text="Take photo sample", variable=self.photos_var,value="Yes")
        R_button.grid( row=6 ,column=1 ,padx=5 ,pady=3)

        R2_button = ttk.Radiobutton(self.Student_info ,text=" No photo sample",  variable=self.photos_var,value="No")
        R2_button.grid( row=6 ,column=2 ,padx=3 ,pady=3)

        Btn_save = Button(self.Student_info, text="SAVE", background="White", font=('Times New Roman',11,'bold'),
                          borderwidth=3, fg="White", relief=SUNKEN, bg="Blue", height=2, width=19, command=self.add_data)
        Btn_save.grid(row=7, column=1)

        Btn_update = Button(self.Student_info, text="UPDATE", background="White",font=('Times New Roman',11,'bold'),
                            borderwidth=3, fg="White", relief=SUNKEN, bg="Blue", height=2, width=19 ,command=self.update_data)
        Btn_update.grid(row=7, column=2)

        Btn_delete = Button(self.Student_info, text="DELETE", background="White", font=('Times New Roman',11,'bold'),
                            borderwidth=3, fg="White", relief=SUNKEN, bg="Blue", height=2, width=19,command=self.delete_date)
        Btn_delete.grid(row=7, column=3)

        Btn_reset = Button(self.Student_info, text="RESET", background="White", font=('Times New Roman',11,'bold'),
                           borderwidth=3, fg="White", relief=SUNKEN, bg="Blue", height=2, width=19 ,command=self.reset_data )
        Btn_reset.grid(row=7, column=4)

        Btn_takephoto = Button(self.Student_info, text="TAKE PHOTO SAMPLE", background="White",
                               font=('Times New Roman',11,'bold'), borderwidth=3, fg="White", relief=SUNKEN, bg="Blue", command=self.capture_img)
        Btn_takephoto.place(x=0, y=240, height=50, width=360)

        Btn_update_photo = Button(self.Student_info, text="UPDATE PHOTO SAMPLE", background="White",
                                  font=('Times New Roman',12,'bold'), borderwidth=3, fg="White", relief=SUNKEN, bg="Blue", command=self.capture_img )
        Btn_update_photo.place(x=360, y=240, height=50, width=370)

        # self.right_frame =LabelFrame(self.main_frame,bd=2,background="white",relief=RIDGE ,text="Student Detail",font="comicsansms 10 bold")
        # self.right_frame.place(x=785,y=10 ,width=755,height=550)

        # img5 =Image.open(r"C:\Users\NEW\Desktop\Mini project chinmay\New folder 1\img\images.jpeg" )
        # img5 = img5.resize((755,130), Image.ANTIALIAS)
        # self.photoImage5 = ImageTk.PhotoImage(img5)
        # self.Le_img_l4 = Label(self.right_frame,image=self.photoImage5)
        # self.Le_img_l4.place(x=0 ,y=0,height=100,width=755)

        img_R7 = Image.open(r"img\images.jpeg")
        img_R7 = img_R7.resize((755, 130), Image.Resampling.LANCZOS)
        self.photoImage_4_R = ImageTk.PhotoImage(img_R7)
        self.Re_img_r3 = Label(self.right_frame, image=self.photoImage_4_R)
        self.Re_img_r3.place(x=0, y=0, height=120  , width=755)






        # ======= Search system =========# 
        Search_frame =LabelFrame(self.right_frame ,bd=2 ,background="White", relief=RIDGE, text="Search System ",font=('Times New Roman',10,'bold') )
        Search_frame.place(x=10 ,y= 125 ,width=730 ,height=70)


        Search_label= Label(Search_frame,text="Search By ", font=('Times New Roman',15,'bold') ,background="red" ,foreground="White",width=8 )
        Search_label.grid(row=0,column=0 , padx=10,pady=5,sticky=W )

        
        sear_combo = ttk.Combobox(Search_frame, font=('Times New Roman',12,'bold'), state="readonly",width=20 )
        sear_combo["values"] = ["Select ","id",
                               "Roll no ", "Phone_no"]
        sear_combo.current(0)
        sear_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        Student_Search_input = Entry(
        Search_frame, font=('Times New Roman',12,'bold'),highlightthickness=.5, highlightcolor= "Black",highlightbackground = "grey",width=15)
        Student_Search_input.grid(row=0, column=2 ,padx=3)
         




        Btn_search = Button(Search_frame, text="Search", background="White", font=('Times New Roman',10,'bold'),
                          borderwidth=3, fg="White", relief=SUNKEN, bg="Blue", width=15)
        Btn_search.grid(row=0, column=3 , padx=2)

        Btn_search_all = Button(Search_frame, text="Search All", background="White",font=('Times New Roman',10,'bold'),
                            borderwidth=3, fg="White", relief=SUNKEN, bg="Blue", width=15)
        Btn_search_all.grid(row=0, column=4  , padx=2)


        


        # ======== Table frame =============

        tabele_frame = Frame(self.right_frame, bd=2 ,background="white" )
        tabele_frame.place(x=10 ,y=200 ,height= 322,width=730)
 
        scroll_x =ttk.Scrollbar( tabele_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tabele_frame ,orient=VERTICAL)

        self.student_table  = ttk.Treeview(tabele_frame,column=(
            "Dept","course","year","sem","id","name","div","roll","gender","gmail", "phone","address" ,"teacher","photos"
        ),xscrollcommand=scroll_x.set,yscrollcommand= scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y) 
        scroll_x.config(command= self.student_table.xview)
        scroll_y.config(command= self.student_table.yview)


        self.student_table.heading("Dept",text="Department" ) 
        self.student_table.heading("course",text="Class" ) 
        self.student_table.heading("year",text="Year" ) 
        self.student_table.heading("sem",text="Semester" ) 
        self.student_table.heading("id",text="Student_id" ) 
        self.student_table.heading("name",text="Name" ) 
        self.student_table.heading("div",text="Div" ) 
        self.student_table.heading("roll",text="Roll no" ) 
        self.student_table.heading("gender",text="Gender" ) 
        self.student_table.heading("gmail",text="Gmail" ) 
        self.student_table.heading("phone",text="Phone no" ) 
        self.student_table.heading("address",text="Address" )
        self.student_table.heading("teacher",text="Teacher" )
        self.student_table.heading("photos",text="Photo Sample" )


        self.student_table.column("Dept",width=100 ) 
        self.student_table.column("course",width=100) 
        self.student_table.column("year",width=100  ) 
        self.student_table.column("sem",width=100  ) 
        self.student_table.column("id",width=100  ) 
        self.student_table.column("name",width=100 ) 
        self.student_table.column("div",width=100  ) 
        self.student_table.column("roll",width=100 ) 
        self.student_table.column("gender",width=100  ) 
        self.student_table.column("gmail",width=100 ) 
        self.student_table.column("phone",width=100  ) 
        self.student_table.column("address",width=100  )
        self.student_table.column("teacher",width=100 )
        self.student_table.column("photos",width=100 )


        self.student_table["show"] = "headings"
        self.student_table.pack(fil=BOTH ,expand=1)
        self.student_table.bind("<ButtonRelease>" ,self.get_cursor)
        self.fetch_data()
         





    def add_data(self):
        if self.Deparment_1.get() == "Select Department" or self.student_id_1.get() == "" or self.student_name_1.get() == "":
            messagebox.showerror("Error", "All field are required")

        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost', user='root', password='rootpassword', port="3310", database='new')
                my_cursor = conn.cursor()
                my_cursor.execute("Insert into attandance_management_system values(%s ,%s, %s, %s, %s ,%s, %s ,%s, %s, %s, %s ,%s, %s,%s)", (
                    self.Deparment_1.get(),
                    self.class_var.get(),
                    self.year_1.get(),
                    self.semester_1.get(),
                    self.student_id_1.get(),
                    self.student_name_1.get(),
                    self.division_1.get(),
                    self.Roll_No_1.get(),
                    self.gender_1.get(),
                    self.Email_1.get(),
                    self.Phone_no_1.get(),
                    self.Address_1.get(), 
                    self.Teacher_name_1.get(),
                    self.photos_var.get()))

                messagebox.showinfo(
                    "Sucess", "Student detail has been added sucessfully", parent=self.root)
                print("connection sucessful")
                conn.commit()
                self.fetch_data( )
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f" Due to :{str(es)}", parent=self.root)
                # print(es, self.Deparment_1.get(), self.class_var.get(), self.year_1.get(), self.semester_1.get(), self.student_id_1.get(), self.student_name_1.get(), self.division_1.get(), self.Roll_No_1.get(), self.gender_1.get(), self.Email_1.get(), self.Phone_no_1.get(),
                #       self.Address_1.get(), self.Teacher_name_1.get())
    

    # ======fetch data =======

    def fetch_data(self):
        conn = mysql.connector.connect(
                    host='localhost', user='root', password='rootpassword', port="3310", database='new')
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from  attandance_management_system")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.close()

    #   ====get cursor ====
    def get_cursor(self,event=""):
        cursor_focus= self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.Deparment_1.set(data[0])
        self.class_var.set(data[1])
        self.year_1.set(data[2])
        self.semester_1.set(data[3]) 
        self.student_id_1.set(data[4])
        self.student_name_1.set(data[5]) 
        self.division_1.set(data[6]) 
        self.Roll_No_1.set(data[7])
        self.gender_1.set(data[8]) 
        self.Email_1.set(data[9]) 
        self.Phone_no_1.set(data[10])
        self.Address_1.set(data[11]) 
        self.Teacher_name_1.set(data[12])
        self.photos_var.set(data[13])

    #  ======Update Function
    def update_data(self):
        if self.Deparment_1.get() == "Select Department" or self.student_id_1.get() == "" or self.student_name_1.get() == "":
            messagebox.showerror("Error", "All field are required")
        else:
            try:
                Update =messagebox.askyesno("Update","Do you want to update this Student datails " ,parent =self.root)
                if Update>0:
                    conn = mysql.connector.connect(
                    host='localhost', user='root', password='rootpassword', port="3310", database='new')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update attandance_management_system  set Department=%s,class_var=%s,year=%s,semester=%s,student_name=%s,division=%s,Roll_No=%s,gender=%s,Email=%s,Phone_no=%s,Address=%s, Teacher_name=%s,Photos=%s where student_id =%s", 
                    (
                    self.Deparment_1.get(),
                    self.class_var.get(),
                    self.year_1.get(),
                    self.semester_1.get(),
                    
                    self.student_name_1.get(),
                    self.division_1.get(),
                    self.Roll_No_1.get(),
                    self.gender_1.get(),
                    self.Email_1.get(),
                    self.Phone_no_1.get(),
                    self.Address_1.get(), 
                    self.Teacher_name_1.get(),
                    self.photos_var.get(),
                    self.student_id_1.get()))
        
                else: 
                    if  not Update:
                        return
                messagebox.showinfo("Success","Student Details sucessfully update completed",parent= self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es :
                messagebox.showerror("Error", f" Due to :{str(es)}", parent=self.root)
    

    #  Delete fuction 
    def delete_date(self):
        if self.student_id_1.get()=="":
            messagebox.showerror("Error","Student id must required",parent = self.root)
        else: 
            try:
                delete = messagebox.askyesno("Student Delete page","Do you want to delete this student",parent= self.root)
                if delete>0:
                    conn = mysql.connector.connect(
                    host='localhost', user='root', password='rootpassword', port="3310", database='new')
                    my_cursor = conn.cursor()
                    sql = "delete from  attandance_management_system where student_id =%s"
                    val = (self.student_id_1.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details sucessfully Deleted",parent= self.root)
            except Exception as es :
                messagebox.showerror("Error", f" Due to :{str(es)}", parent=self.root)

    # ===== Reset ====

    def reset_data(self):
        self.Deparment_1.set("Select Department"),
        self.class_var.set("Select class"),
        self.year_1.set("Select year"),
        self.semester_1.set("Select Semester") ,
        self.student_id_1.set(""), 
        self.student_name_1.set("") ,
        self.division_1.set("") ,
        self.Roll_No_1.set(""), 
        self.gender_1.set("Select Gender") ,
        self.Email_1.set(""), 
        self.Phone_no_1.set(""),
        self.Address_1.set("") ,
        self.Teacher_name_1.set(""),
        self.photos_var.set("")








        

    
        
                    
        # genrate data set 

    def capture_img(self):
        if self.Deparment_1.get() == "Select Department" or self.student_id_1.get() == "" or self.student_name_1.get() == "":
            messagebox.showerror("Error", "All field are required" ,parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost', user='root', password='rootpassword', port="3310", database='new')
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from  attandance_management_system")
                myresult = my_cursor.fetchall()

                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update attandance_management_system  set Department=%s,class_var=%s,year=%s,semester=%s,student_name=%s,division=%s,Roll_No=%s,gender=%s,Email=%s,Phone_no=%s,Address=%s, Teacher_name=%s,Photos=%s where student_id =%s", 
                        (self.Deparment_1.get(),
                        self.class_var.get(),
                        self.year_1.get(),
                        self.semester_1.get(),
                        self.student_name_1.get(),
                        self.division_1.get(),
                        self.Roll_No_1.get(),
                        self.gender_1.get(),
                        self.Email_1.get(),
                        self.Phone_no_1.get(),
                        self.Address_1.get(), 
                        self.Teacher_name_1.get(),
                        self.photos_var.get(), 
                        self.student_id_1.get()==id+1))
                conn.commit()
                self.reset_data()
                self.fetch_data()
                conn.close()

                #  ============ load predefine data on face from opencv===
                face_classifier= cv2.CascadeClassifier("face_recog.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces= face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor =1.3
                    # minimum neighbor= 5

                    for(x,y,w,h)in faces:
                        face_cropped=img[y:y+h ,x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id=0


                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None :
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

                        file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result ","Generating data set compled !!!!")
            except Exception as es :
                messagebox.showerror("Error", f" Due to :{str(es)}", parent=self.root)

                print(es)
        
        # search 

        












































        # self.cam = cv2.VideoCapture(0)

        # cv2.namedWindow("test")

        # img_counter = 0

        # while True:
        #     ret, frame = self.cam.read()
        #     if not ret:
        #         print("failed to grab frame")
        #         break
        #     cv2.imshow("test", frame)

        #     k = cv2.waitKey(1)
        #     if k % 256 == 27:
        #         # ESC pressed
        #         print("Escape hit, closing...")
        #         break
        #     elif k % 256 == 32:
        #         # SPACE pressed and convert img ito grey img
        #         grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #         path = r"C:\Users\NEW\Desktop\Mini project chinmay\New folder 1\new\GetIMG"
        #         img_name = "opencv_frame_{}.png".format(img_counter)

        #         # to save image in file
        #         cv2.imwrite(os.path.join(path, img_name), grey)
        #         print("{} written!".format(img_name))
        #         img_counter += 1

        # self.cam.release()

        # cv2.destroyAllWindows()
        










        # self.left_frame =LabelFrame(self.main_frame,bd=2,background="white",relief=RIDGE ,text="Student Detail",font="comicsansms 10 bold")
        # self.left_frame.place(x=10,y=10 ,width=765,height=550)
    # def back_button(self):
    #     Attandace_Detail.destroy()
    #     Button.destroy()
        

if __name__ == "__main__":
    root = Tk()
    obj = Attandace_Detail(root)
    root.mainloop()
