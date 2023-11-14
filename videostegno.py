from stegano import lsb
from os.path import isfile,join

import time                                                                 
import cv2
import numpy as np
import math
import os
import shutil
from subprocess import call,STDOUT

from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os

import numpy as np
import pandas as pand
import os
import cv2
from matplotlib import pyplot as plt

from math import log10, sqrt


  

  

     

root=Tk()
root.title(" BATCH 36 ")
root. geometry("700x700+150+180")
root. resizable(False, False)

root. configure(bg="AntiqueWhite2")
#root.iconbitmap("cmrrico.ico")
root.iconbitmap("sun.ico")

logo=PhotoImage(file="l.png")

Label (root, image=logo).place(x=10,y=5)

def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        value = 100
    else:
        max_pixel = 255.0
        psnr = 20 * log10(max_pixel / sqrt(mse))
        value = psnr
    text5.insert(END, "\n")
    text5.insert(END, value)
    
def frame_extraction(video,k):
    if not os.path.exists("./tmp"):
        os.makedirs("tmp")
    temp_folder="./tmp"
    print("[INFO] tmp directory is created")

    vidcap = cv2.VideoCapture(video)
    count = 0

    while True:
        success, image = vidcap.read()
        if not success:
            break
        #if(count==k):
        cv2.imwrite(os.path.join(temp_folder, "{:d}.png".format(count)), image)
        
        #break
            
        
        count += 1

def encode_string(input_string,root="./tmp/"):
    k=int(text11.get(1.0,END))
    print(type(k))
    f_name="{}{}.png".format(root,k)
    i1=cv2.imread(f_name)
    secret_enc=lsb.hide(f_name,input_string)
    
    secret_enc.save(f_name)
    i2=cv2.imread(f_name)
    PSNR(i1,i2)
    #print(lsb.reveal(f_name))
    print("saved")
    #clean_tmp()
    

def clean_tmp(path="./tmp"):
    if os.path.exists(path):
        shutil.rmtree(path)
        print("[INFO] tmp files are cleaned up")

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select VIDEO File',filetype=(("mp4","*.mp4"),("MOV","*.mov"), ("All file","*.txt")))


def Hide():
    input_string = text1.get(1.0,END)
    text1.delete(1.0, END)
    k=int(text11.get(1.0,END))
    
    frame_extraction(filename,k)
    call(["ffmpeg", "-i",filename, "-q:a", "0", "-map", "a", "tmp/audio.mp3", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
    

    
    encode_string(input_string)
    call(["ffmpeg", "-i", "tmp/%d.png" , "-vcodec", "png", "tmp/video.mp4", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
    
    
    call(["ffmpeg", "-i", "tmp/video.mp4", "-i", "tmp/audio.mp3", "-codec", "copy", "video.mp4", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
    
    #clean_tmp()
    text5.insert(END, "\nENCODED SUCCESFULLY")
    
    

def Show():
    text1.delete(1.0, END)
    k=int(text21.get(1.0,END))
    frame_extraction(filename,k)
    root="./tmp/"
    
    f_name="{}{}.png".format(root,k)
    secret_dec=lsb.reveal(f_name)
    
    clean_tmp()
    
   
            
          
    
    ss=secret_dec
    
    
    text2.insert(END, ss)
    text5.delete(1.0, END)
    text5.insert(END, "DECODED SUCCESFULLY")




Label (root, text= "VIDEO STEGANOGRAPHY" ,bg="AntiqueWhite2" ,fg="black", font="arial 25 bold") .place(x=150,y=20)
Label (root, text= "ENCODE" ,bg="AntiqueWhite2" ,fg="black", font="arial 25 bold") .place(x=90,y=130)
Label (root, text= "DECODE" ,bg="AntiqueWhite2" ,fg="black", font="arial 25 bold") .place(x=420,y=130)
f=Frame(root, bd=3, bg= "white" ,width=330, height=100,relief=GROOVE)
f.place(x=10,y=220)
Label (root, text= "Enter Text" ,bg="AntiqueWhite2" ,fg="black", font="arial 20 ") .place(x=10,y=180)
fm=Frame(root, bd=3, bg= "white" ,width=330, height=100,relief=GROOVE)
fm.place(x=10,y=350)
Label (root, text= "Enter Frameno" ,bg="AntiqueWhite2" ,fg="black", font="arial 15 ") .place(x=10,y=320)
lb1=Label(f,bg="pink")
lb1.place(x=40,y=20)

frame21=Frame(root, bd=3,width=330,height=100,bg="white", relief=GROOVE)
frame21.place(x=350,y=350)
frame31=Frame(root, bd=3,width=330,height=100,bg="white", relief=GROOVE)
frame31.place(x=350,y=220)
text1=Text(f, font="Robote 20" ,bg="white" ,fg="black" ,relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=90)
text11=Text(fm, font="Robote 20" ,bg="white" ,fg="black" ,relief=GROOVE,wrap=WORD)
text11.place(x=0,y=0,width=320,height=120)
text2=Text(frame21, font="Robote 20" ,bg="white" ,fg="red" ,relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=320,height=160)
Label (root, text= "Enter Frameno" ,bg="AntiqueWhite2" ,fg="black", font="arial 20 ") .place(x=350,y=180)
Label (root, text= "Hidden Text" ,bg="AntiqueWhite2" ,fg="black", font="arial 15 ") .place(x=350,y=320)
text21=Text(frame31, font="Robote 20" ,bg="white" ,fg="green" ,relief=GROOVE,wrap=WORD)
text21.place(x=0,y=0,width=320,height=160)
scrollbar1=Scrollbar(f)
scrollbar1.place(x=310,y=0,height=30)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


#third Frame
frame3=Frame (root, bd=3, bg="AntiqueWhite2" ,width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=460)

Button (frame3, text="Open Video" ,width=10, height=2, font="arial 14 bold",command=showimage ).place(x=20,y=30)
#Button (frame3, text="Save Image" ,width=10, height=2, font= "arial 14 bold",command=save ).place(x=180,y=30)
Label(frame3, text= "video" ,bg="AntiqueWhite2",fg="black").place(x=20,y=5)

#fourth Frame
frame4=Frame(root, bd=3, bg="AntiqueWhite2" ,width=330,  height=100,relief=GROOVE)
frame4. place(x=360,y=460)
      
Button (frame3, text="Hide Data" ,width=10, height=2, font="arial 14 bold",command=Hide).place(x=180,y=30)
Button (frame4, text="Open Video" ,width=10, height=2, font="arial 14 bold",command=showimage ).place(x=20,y=30)
Button (frame4, text="Show Data",width=10, height=2, font="arial 14 bold",command=Show).place(x=180,y=30)
Label (frame4, text="video",bg="AntiqueWhite2",fg="black").place(x=20,y=5)


frame5=Frame(root, bd=3, bg="black" ,width=630,  height=100,relief=GROOVE)
frame5.place(x=30,y=580)
text5=Text(frame5, font="Robote 20" ,bg="black" ,fg="white" ,relief=GROOVE,wrap=WORD)
text5.place(x=0,y=0,width=630,height=100)


root.mainloop()
