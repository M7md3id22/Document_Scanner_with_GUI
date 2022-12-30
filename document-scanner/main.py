import cv2
from tkinter import (ttk,Tk,PhotoImage,Canvas, filedialog, colorchooser,RIDGE,
                     GROOVE,ROUND,Scale,HORIZONTAL)
import numpy as np
from tkinter import *
from os import path
from PIL import ImageTk, Image


def drawRec(biggestNew, mainFrame):
        cv2.line(mainFrame, (biggestNew[0][0][0], biggestNew[0][0][1]), (biggestNew[1][0][0], biggestNew[1][0][1]), (0, 255, 0), 20)
        cv2.line(mainFrame, (biggestNew[0][0][0], biggestNew[0][0][1]), (biggestNew[2][0][0], biggestNew[2][0][1]), (0, 255, 0), 20)
        cv2.line(mainFrame, (biggestNew[3][0][0], biggestNew[3][0][1]), (biggestNew[2][0][0], biggestNew[2][0][1]), (0, 255, 0), 20)
        cv2.line(mainFrame, (biggestNew[3][0][0], biggestNew[3][0][1]), (biggestNew[1][0][0], biggestNew[1][0][1]), (0, 255, 0), 20)

class FrontEnd:
    def __init__(self, master):
        self.master = master
        self.menu_initialisation()
        
    def menu_initialisation(self):
        self.master.geometry('750x630+250+10')
        self.master.title('document scanning with Python (Tkinter and OpenCV)')
        
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()

        self.logo = PhotoImage(file='nub.PNG').subsample(5,5)
        print(self.logo)
        ttk.Label(self.frame_header, image=self.logo).grid(
        row=0, column=0, rowspan=2)
       
        
        ttk.Label(self.frame_header, text='Team : Mohamed Eid 191060040').grid(
            row=0, column=2, columnspan=1)
        ttk.Label(self.frame_header, text=', Amr Mohamed 191060093').grid(
            row=0, column=3, columnspan=1)
        ttk.Label(self.frame_header, text=', Ahmed Nageh 191060127').grid(
            row=0, column=4, columnspan=1)
        ttk.Label(self.frame_header, text=', Gamal Ali 191060082').grid(
            row=0, column=5, columnspan=1)
        ttk.Label(self.frame_header, text='Computer Vision Project').grid(
            row=1, column=1, columnspan=2)
        ttk.Label(self.frame_header, text='Supervised by : Dr-Ahmed Donkol , Eng Ahmed abdulmoaty').grid(
            row=2, column=1, columnspan=3)
        
        
        
        self.frame_menu = ttk.Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(relief=RIDGE, padding=(50, 15))
        
        ttk.Button(
            self.frame_menu, text="Upload An Image", command=self.upload_action).grid(
            row=0, column=0, columnspan=2, padx=5, pady=5, sticky='sw')
        ttk.Button(
            self.frame_menu, text="original img", command=self.img_show).grid(
            row=1, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="GrayImg", command=self.img_show1).grid(
            row=2, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="BlurredFrame", command=self.img_show2).grid(
            row=3, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="CannyFrame", command=self.img_show3).grid(
            row=4, column=0, columnspan=2,  padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="ContourFrame", command=self.img_show4).grid(
            row=5, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="CornerFrame", command=self.img_show5).grid(
            row=6, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="perspective transform", command=self.img_show6).grid(
            row=7, column=0, columnspan=2, padx=5, pady=5, sticky='sw')
        ttk.Button(
            self.frame_menu, text="Save As", command=self.save_action).grid(
            row=9, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        self.canvas = Canvas(self.frame_menu, bg="black", width=480, height=640)
        self.canvas.grid(row=0, column=3, rowspan=10)
        
        self.side_frame = ttk.Frame(self.frame_menu)
        self.side_frame.grid(row=0, column=4, rowspan=10)
        self.side_frame.config(relief=GROOVE, padding=(50,15))

   
            
    def img_show (self):
        self.display_image(self.edited_image)
    def img_show1 (self):
        self.original_image = cv2.resize(self.original_image, (int(480*2), int(640*2)))
        GrayImg = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        GrayImg = cv2.resize(GrayImg, (480, 640))
        self.display_image(GrayImg)

    def img_show2 (self):
        self.original_image = cv2.resize(self.original_image, (int(480*2), int(640*2)))
        GrayImg = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        BlurredFrame = cv2.GaussianBlur(GrayImg, (5, 5), 1)
        BlurredFrame = cv2.resize(BlurredFrame, (480, 640))
        self.display_image(BlurredFrame)
        
    def img_show3 (self):
        self.original_image = cv2.resize(self.original_image, (int(480*2), int(640*2)))
        GrayImg = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        BlurredFrame = cv2.GaussianBlur(GrayImg, (5, 5), 1)
        CannyFrame = cv2.Canny(BlurredFrame, 190, 190)
        CannyFrame = cv2.resize(CannyFrame, (480, 640))
        self.display_image(CannyFrame)
        
    def img_show4 (self):
        self.original_image = cv2.resize(self.original_image, (int(480*2), int(640*2)))
        GrayImg = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        BlurredFrame = cv2.GaussianBlur(GrayImg, (5, 5), 1)
        CannyFrame = cv2.Canny(BlurredFrame, 190, 190)
        contours, _ = cv2.findContours(CannyFrame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        ContourFrame = self.original_image.copy()
        ContourFrame = cv2.drawContours(ContourFrame, contours, -1, (255, 0, 255), 4)
        ContourFrame = cv2.resize(ContourFrame, (480, 640))
        self.display_image(ContourFrame)

    def img_show5 (self):
        self.original_image = cv2.resize(self.original_image, (int(480*2), int(640*2)))
        w, h = 480, 640
        imgWarp = self.original_image.copy()
        GrayImg = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        BlurredFrame = cv2.GaussianBlur(GrayImg, (5, 5), 1)
        CannyFrame = cv2.Canny(BlurredFrame, 190, 190)
        contours, _ = cv2.findContours(CannyFrame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        ContourFrame = self.original_image.copy()
        ContourFrame = cv2.drawContours(ContourFrame, contours, -1, (255, 0, 255), 4)
        CornerFrame = self.original_image.copy()
        maxArea = 0
        biggest = []
        for i in contours :
            area = cv2.contourArea(i)
            if area > 500 :
                peri = cv2.arcLength(i, True)
                edges = cv2.approxPolyDP(i, 0.02*peri, True)
                if area > maxArea and len(edges) == 4 :
                    biggest = edges
                    maxArea = area
        if len(biggest) != 0 :
            
            biggest = biggest.reshape((4, 2))
            biggestNew = np.zeros((4, 1, 2), dtype= np.int32)
            add = biggest.sum(1)
            biggestNew[0] = biggest[np.argmin(add)]
            biggestNew[3] = biggest[np.argmax(add)]
            dif = np.diff(biggest, axis = 1)
            biggestNew[1] = biggest[np.argmin(dif)]
            biggestNew[2] = biggest[np.argmax(dif)]
            drawRec(biggestNew, CornerFrame)
            CornerFrame = cv2.drawContours(CornerFrame, biggestNew, -1, (255, 0, 255), 25)
            CornerFrame = cv2.resize(CornerFrame, (480, 640))
            self.display_image(CornerFrame)

    def img_show6 (self):
        self.original_image = cv2.resize(self.original_image, (int(480*2), int(640*2)))
        w, h = 480, 640
        imgWarp = self.original_image.copy()
        GrayImg = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        BlurredFrame = cv2.GaussianBlur(GrayImg, (5, 5), 1)
        CannyFrame = cv2.Canny(BlurredFrame, 190, 190)
        contours, _ = cv2.findContours(CannyFrame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        ContourFrame = self.original_image.copy()
        ContourFrame = cv2.drawContours(ContourFrame, contours, -1, (255, 0, 255), 4)
        CornerFrame = self.original_image.copy()
        maxArea = 0
        biggest = []
        for i in contours :
            area = cv2.contourArea(i)
            if area > 500 :
                peri = cv2.arcLength(i, True)
                edges = cv2.approxPolyDP(i, 0.02*peri, True)
                if area > maxArea and len(edges) == 4 :
                    biggest = edges
                    maxArea = area
        if len(biggest) != 0 :
            
            biggest = biggest.reshape((4, 2))
            biggestNew = np.zeros((4, 1, 2), dtype= np.int32)
            add = biggest.sum(1)
            biggestNew[0] = biggest[np.argmin(add)]
            biggestNew[3] = biggest[np.argmax(add)]
            dif = np.diff(biggest, axis = 1)
            biggestNew[1] = biggest[np.argmin(dif)]
            biggestNew[2] = biggest[np.argmax(dif)]
            drawRec(biggestNew, CornerFrame)
            CornerFrame = cv2.drawContours(CornerFrame, biggestNew, -1, (255, 0, 255), 25)
            pts1 = np.float32(biggestNew)
            pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            imgWarp = cv2.warpPerspective(self.original_image, matrix, (w, h))
            self.edited_image=imgWarp
        self.display_image(self.edited_image)
        
        
    def upload_action(self):
        self.canvas.delete("all")
        self.filename = filedialog.askopenfilename()
        self.original_image = cv2.imread(self.filename)

        self.edited_image = cv2.imread(self.filename)
        self.filtered_image = cv2.imread(self.filename)
        self.display_image(self.edited_image)

    def save_action(self):
        original_file_type = self.filename.split('.')[-1]
        filename = filedialog.asksaveasfilename()
        filename = filename + "." + original_file_type

        save_as_image = self.edited_image
        cv2.imwrite(filename, save_as_image)
        self.filename = filename

    def refresh_side_frame(self):
        try:
            self.side_frame.grid_forget()
        except:
            pass

        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>")
        self.display_image(self.edited_image)
        self.side_frame = ttk.Frame(self.frame_menu)
        self.side_frame.grid(row=0, column=4, rowspan=10)
        self.side_frame.config(relief=GROOVE, padding=(50, 15))

    def display_image(self, image=None):
        self.canvas.delete("all")
        if image is None:
            image = self.edited_image.copy()
        else:
            image = image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channels = image.shape
        ratio = height / width

        new_width = width
        new_height = height

        if height > 640 or width > 480:
            if ratio < 1:
                new_width = 480
                new_height = int(new_width * ratio)
            else:
                new_height = 640
                new_width = int(new_height * (width / height))

        self.ratio = height / new_height
        self.new_image = cv2.resize(image, (new_width, new_height))

        self.new_image = ImageTk.PhotoImage(Image.fromarray(self.new_image))

        self.canvas.config(width=new_width, height=new_height )
        self.canvas.create_image(new_width / 2, new_height / 2,  image=self.new_image)

mainWindow = Tk()
FrontEnd(mainWindow)
mainWindow.mainloop()
cv2.waitKey(0)