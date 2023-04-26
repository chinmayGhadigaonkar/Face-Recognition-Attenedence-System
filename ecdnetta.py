from cProfile import label
from tkinter import *
from  tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
#import mysq.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root 
        self.root.geometry("1590x790+0+0")
        self.root.title("Face Recognization")
        

        #  ==== variable ===

        self.var_att_id= StringVar()
        self.var_att_roll= StringVar()
        self.var_att_name= StringVar()
        self.var_att_dep= StringVar()
        self.var_att_time= StringVar()
        self.var_att_date= StringVar()
        self.var_att_attendence= StringVar()
         


        #Image
        img=Image.open("face.jpg")
        image=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        #Image
        img1=Image.open("face.jpg")
        image1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        # Bg images 
        bg =Image.open(r"img\Student_bg_img.jpg")
        bg = bg.resize((1590,660), Image.ANTIALIAS)
        self.photoImage3 = ImageTk.PhotoImage(bg)
        self.img_l4 = Label(self.root,image=self.photoImage3)
        self.img_l4.place(x=0,y=130,height=660,width=1590)


         # heading 
        self.l_heading= Label(self.img_l4, text="Attendance" ,background="Navy",font="comicsansms 25 bold",borderwidth=3 , fg= "yellow",relief=SUNKEN)
        self.l_heading.place(x=0,y=0,width=1590 ,height=50)

         # Frame
        self.main_frame =Frame(self.img_l4,bd=2,background="White")
        self.main_frame.place(x=20,y=60 ,width=1550,height=580)

        # Frame
        self.left_frame =LabelFrame(self.main_frame,bd=2,background="white",relief=RIDGE ,text="Attendance Detail",font="comicsansms 10 bold")
        self.left_frame.place(x=10,y=10 ,width=765,height=550)

        left_inside_frame =Frame(self.left_frame,bd=2,relief=RIDGE,background="White")
        left_inside_frame.place(x=0,y=130 ,width=800,height=400)


        #========Label======================
        #==========Attendance======================
        attendance_Id = Label(left_inside_frame ,text="Attendance_Id:",font="comicsansms 12 bold ",background="white")
        attendance_Id.grid(row=1 ,column=1,padx=3 ,pady=3)

        attendance_Id_input= Entry(left_inside_frame ,textvariable=self.var_att_id ,font="comicsansms 12 bold ")
        attendance_Id_input.grid(row=1 ,column=2)

        #=======================Name======================
        name = Label(left_inside_frame ,text="Name:",font="comicsansms 12 bold ",background="white")
        name.grid(row=1 ,column=3,padx=3 ,pady=3)

        name_input= Entry(left_inside_frame ,textvariable=self.var_att_name ,font="comicsansms 12 bold ")
        name_input.grid(row=1 ,column=4)

        #========================date======================

        date = Label(left_inside_frame ,text="Date:",font="comicsansms 12 bold ",background="white")
        date.grid(row=3 ,column=3,padx=3 ,pady=3)

        date_input= Entry(left_inside_frame ,textvariable=self.var_att_date,font="comicsansms 12 bold ")
        date_input.grid(row=3 ,column=4)

        #===========================Department=========================
        Department = Label(left_inside_frame ,text="Department:",font="comicsansms 12 bold ",background="white")
        Department.grid(row=2 ,column=3,padx=3 ,pady=3)

        Department_input= Entry(left_inside_frame,textvariable=self.var_att_dep ,font="comicsansms 12 bold ")
        Department_input.grid(row=2 ,column=4)

        #============================Time================================

        Time = Label(left_inside_frame,text="Time:",font="comicsansms 12 bold ",background="white")
        Time.grid(row=3 ,column=1,padx=3 ,pady=3)

        Time_input= Entry(left_inside_frame ,textvariable=self.var_att_time  ,font="comicsansms 12 bold ")
        Time_input.grid(row=3 ,column=2)

        #===========================Roll_No==================================

        Roll_No = Label(left_inside_frame ,text="Roll_No:",font="comicsansms 12 bold ",background="white")
        Roll_No.grid(row=2 ,column=1,padx=3 ,pady=3)

        Roll_No_input= Entry(left_inside_frame ,textvariable=self.var_att_roll,font="comicsansms 12 bold ")
        Roll_No_input.grid(row=2 ,column=2)

        #============================attendance=============================

        attendance = Label(left_inside_frame  ,text="Attendance Status",font="comicsansms 12 bold ",background="white")
        attendance.grid(row=4 ,column=1,padx=3 ,pady=3)

        self.atten_combo = ttk.Combobox(left_inside_frame ,textvariable=self.var_att_attendence , font="comicsansms 12  bold " ,state="readonly")
        self.atten_combo["values"] =["Status", "Present","Absent"] 
        self.atten_combo.current(0)
        self.atten_combo.grid(row=4, column=2 ,padx=3 ,pady=3 ,sticky=W)

        #==========================Button===============================

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=780,height=60)

        Btn_save = Button (btn_frame,text="Import csv",background="White",font="comicsansms 11 bold",borderwidth=3 , fg= "White",relief=SUNKEN,bg="Blue",height=3,width=20 ,command= self.importCSV )
        Btn_save.grid( row= 7 ,column=1 )

        Btn_2 = Button (btn_frame,text="Update",background="White",font="comicsansms 11 bold",borderwidth=3 , fg= "White",relief=SUNKEN,bg="Blue",height=3,width=20 )
        Btn_2.grid( row= 7 ,column=3 )

        Btn_save = Button (btn_frame,text="Export",background="White",font="comicsansms 11 bold",borderwidth=3 , fg= "White",relief=SUNKEN,bg="Blue",height=3,width=20 ,command= self.exportCsv)
        Btn_save.grid( row= 7 ,column=2 )

        Btn_save = Button (btn_frame,text="Reset",background="White",font="comicsansms 11 bold",borderwidth=3 , fg= "White",relief=SUNKEN,bg="Blue",height=3,width=20 ,command=self.reset)
        Btn_save.grid( row= 7 ,column=4 )


        #==========================Right Frame====================================
        self.right_frame =LabelFrame(self.main_frame,bd=2,background="white",relief=RIDGE ,text="Attendance Detail",font="comicsansms 10 bold")
        self.right_frame.place(x=785,y=10 ,width=750,height=580)


        table_frame=Frame(self.right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=735,height=445)

        #================================Scroll Bar================================================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>" ,self.get_cursor)
        



        # Leftframe content 
        img4 =Image.open("face.jpg" )
        img4 = img4.resize((765,130), Image.ANTIALIAS)
        self.photoImage4 = ImageTk.PhotoImage(img4)
        self.Le_img_l3 = Label(self.left_frame,image=self.photoImage4)
        self.Le_img_l3.place(x=0 ,y=0,height=80,width=765)

    def fetchData(self,rows):
      self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
      for i in rows:
        self.AttendanceReportTable.insert("",END ,values=i)

  #  ====== Import CSV Data  =====
    def importCSV(self):
      global mydata
      mydata.clear()
      fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File",".csv"),("All File",".")),parent=self.root)
      with open(fln) as myfile:
        csvread = csv.reader(myfile,delimiter=",")
        for i in csvread:
          mydata.append(i)
        self.fetchData(mydata)

  #  ====== Export CSV Data  =====
    def exportCsv(self):
      try:
        if len(mydata)<1:
          messagebox.showerror("No Data Found to Export", parent=self.root)
          return False
        fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File",".csv"),("All File",".")),parent=self.root)
        with open(fln,mode="w",newline="") as myfile:
          export_write = csv.writer(myfile,delimiter=",")
          for i in mydata:
            export_write.writerow(i)
            messagebox.showinfo("Data Export ","Your Data exported  to" +os.path.basename(fln)+"sucessfully ")
      except Exception as es:
        messagebox.showerror("Error",f"Due to : {str(es)} )" ,parent=self.root)    


    def get_cursor(self ,event=""):
      cursor_row= self.AttendanceReportTable.focus()
      content = self.AttendanceReportTable.item(cursor_row)
      row =content['values']
      self.var_att_id.set(row[0])   
      self.var_att_roll.set(row[1]) 
      self.var_att_name.set(row[2]) 
      self.var_att_dep.set(row[3]) 
      self.var_att_time.set(row[4]) 
      self.var_att_date.set(row[5]) 
      self.var_att_attendence.set(row[6])    

    def reset(self ):
      self.var_att_id.set("")   
      self.var_att_roll.set("") 
      self.var_att_name.set("") 
      self.var_att_dep.set("") 
      self.var_att_time.set("") 
      self.var_att_date.set("") 
      self.var_att_attendence.set("")    




           



if __name__ == "__main__":
  root =Tk()
  obj = Attendance(root)
  root.mainloop()