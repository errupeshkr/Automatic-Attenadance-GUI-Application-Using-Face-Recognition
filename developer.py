from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
# from tkinter import messagebox
# import mysql.connector 
# import cv2
# import os
# from turtle import left
#import numpy as np 



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1510x790+0+0")
        self.root.title("Automatic Attendance Management System")
        root.iconbitmap('clgicon.ico')

    # #Tittle of MainFrame
        title_lbl=Label(self.root,text="DEVELOPER" ,font=("times new roman",25,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1410,height=50)
        
    #Top Left photo 
        # img_top=Image.open(r"Project_Image\backand.jpg")
        # img_top=img_top.resize((700,450),Image.Resampling.LANCZOS)
        # self.photoimg_top=ImageTk.PhotoImage(img_top)
        # f_lbl=Label(self.root,image=self.photoimg_top)
        # f_lbl.place(x=0,y=50,width=700,height=450)
    #Top Right photo
        img_top_left=Image.open(r"Project_Image\dev.jpg")
        img_top_left=img_top_left.resize((1400,750),Image.Resampling.LANCZOS)
        self.photoimg_top_left=ImageTk.PhotoImage(img_top_left)
        f_lbl=Label(self.root,image=self.photoimg_top_left)
        f_lbl.place(x=0,y=50,width=1400,height=750)
    #Down photo
        # img_down=Image.open(r"Project_Image\dwnpic.jpg")
        # img_down=img_down.resize((1400,310),Image.Resampling.LANCZOS)
        # self.photoimg_down=ImageTk.PhotoImage(img_down)
        # f_lbl=Label(self.root,image=self.photoimg_down)
        # f_lbl.place(x=0,y=450,width=1400,height=310)

   

    #CDeveloper about labelFrame (170 positon of frame, 280 is height of frame)
        developer_frame=LabelFrame(f_lbl,bd=3,relief=RIDGE,text="About Developer",font=("times new roman",15,"bold"),bg="gold")
        developer_frame.place(x=500,y=5,width=400,height=480)

    #My_image
        img_myImage=Image.open(r"Project_Image\rupeshDeveloper.jpg")
        img_myImage=img_myImage.resize((300,200),Image.Resampling.LANCZOS)
        self.photoimg_myImage=ImageTk.PhotoImage(img_myImage)
    # Label for myImage
        f_lbl=Label(developer_frame,image=self.photoimg_myImage)
        f_lbl.grid(row=0,column=0,padx=25,pady=10,sticky=W)

    #Developer About using Label
        Developer_name=Label(developer_frame,text="My name is Rupesh Kumar",font=("times new roman",15,"bold"),fg="darkblue")
        Developer_name.grid(row=1,column=0,padx=2,pady=1,sticky=W)
        Developer_enroll=Label(developer_frame,text="Enrollment No. 0536CS191044",font=("times new roman",15,"bold"),fg="darkblue")
        Developer_enroll.grid(row=2,column=0,padx=2,pady=1,sticky=W)
        dev_edu=Label(developer_frame,text="I am Student of B.Tech in CSE 7th Sem ",font=("times new roman",15,"bold"),fg="darkblue")
        dev_edu.grid(row=3,column=0,padx=2,pady=1,sticky=W)
        dev_branch=Label(developer_frame,text="Email Id : er.rupesh.kc@gmail.com",font=("times new roman",15,"bold"),fg="darkblue")
        dev_branch.grid(row=5,column=0,padx=2,pady=1,sticky=W)
        dev_from=Label(developer_frame,text="Linkedin :https://www.linkedin.com/in/rupesh-kumar-9b668a1b6",font=("times new roman",12,"bold"),fg="darkblue")
        dev_from.grid(row=6,column=0,padx=2,pady=1,sticky=W)
        dev_from=Label(developer_frame,text="GitHub :https://github.com/errupeshkr",font=("times new roman",15,"bold"),fg="darkblue")
        dev_from.grid(row=7,column=0,padx=2,pady=1,sticky=W)


        

    
        


if __name__ ==  "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()        