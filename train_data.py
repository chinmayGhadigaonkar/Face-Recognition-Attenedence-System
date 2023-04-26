from cProfile import label
from tkinter import *
from  tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
# import mysql.connector
import cv2
import os
import numpy as np
# import numpy as np


class Train_Data:
    def __init__(self,root):
      self.root=root
      self.root.geometry("1590x790+0+0")
      self.root.title("Train Data ")

    # Upper image
      img = Image.open(r"img\t1.gif")
      img = img.resize((530, 130), Image.Resampling.LANCZOS)
      self.photoImage = ImageTk.PhotoImage(img)
      self.img_l1 = Label(self.root, image=self.photoImage)
      self.img_l1.place(x=0, y=0, height=130, width=530)

      img1 = Image.open(r"img\t2.png")
      img1 = img1.resize((530, 130), 	Image.Resampling.LANCZOS)
      self.photoImage1 = ImageTk.PhotoImage(img1)
      self.img_l2 = Label(self.root, image=self.photoImage1)
      self.img_l2.place(x=530, y=0, height=130, width=530)

      img2 = Image.open(r"img\t3.jpg")
      img2 = img2.resize((530, 130), 	Image.Resampling.LANCZOS)
      self.photoImage2 = ImageTk.PhotoImage(img2)
      self.img_l3 = Label(self.root, image=self.photoImage2)
      self.img_l3.place(x=1060, y=0, height=130, width=530)


      #==============================Labe; from traindata========================================
      # title_lbl=Label(self.root,text="Train Data",font=("times new roman",35,"bold"),bg="white",fg="black")
      # title_lbl.place(x=0,y=130,width=1590,height=45)



      img_top=Image.open(r"C:\Users\NEW\Desktop\Mini project chinmay\New folder 1\new\img\bg-train.webp")
      img_top=img_top.resize((1590,660),Image.ANTIALIAS)
      self.photoimg_top=ImageTk.PhotoImage(img_top)

      f_lbl=Label(self.root,image=self.photoimg_top)
      f_lbl.place(x=0,y=130,width=1590,height=660)


      # img_bottom=Image.open(r"face.jpg")
      # img_bottom=img_bottom.resize((950,800),Image.ANTIALIAS)
      # self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

      # f_lbl=Label(self.root,image=self.photoimg_bottom)
      # f_lbl.place(x=650,y=55,width=950,height=800)

      #==========button===========================
      b1_1=Button(self.root,text="Train Data",cursor="hand2",font=("times new roman",18,"bold"),bg="Red",fg="white" ,command=self.train_classifier)
      # b1_1.place(x=750,y=620,width=1590,height=40)
      b1_1.place(x=0,y=430,width=1590,height=60)


      # Exit page
      # def clickExitButton(self):
      #  exit()

    def train_classifier(self):
      data_dir =("Data")
      path = [os.path.join(data_dir,file)for file in os.listdir(data_dir)]

      faces = []
      ids=[]
      for image in path:
        img = Image.open(image).convert("L") # convert img into grey scale
        imageNp =np.array(img,'uint8')
        id =int(os.path.split(image)[1].split('.')[1])

        faces.append(imageNp)
        ids.append(id)
        cv2.imshow("Training",imageNp)
        cv2.waitKey(1)==13
      
      ids =np.array(ids)

      # =========== Train classifier  =======
      clf=cv2.face.LBPHFaceRecognizer_create()
      clf.train(faces,ids)

      clf.write("classifier.xml")
      cv2.destroyAllWindows()
      messagebox.showinfo("Data tain sucessfully " ,"data train sucessfully")








if __name__ == "__main__":
    root=Tk()
    obj=Train_Data(root)
    root.mainloop()