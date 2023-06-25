import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
  
class MyGUI: 
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600") 
        self.root.iconbitmap('phone_call.ico')

        self.top_frame = tk.Frame(self.root)
        self.bottom_frame = tk.Frame(self.root)

        self.img_bg = Image.open('stairs.jpg')
        img = self.img_bg.resize((200, 200))
        self.image_bg = ImageTk.PhotoImage(img)

        self.img_fg = Image.open('stairs.jpg')
        img = self.img_fg.resize((200, 200))
        self.image_fg = ImageTk.PhotoImage(img)
 
        self.label1 = tk.Label(self.top_frame, text="Label 1", background='blue', image=self.image_bg)
        self.label2 = tk.Label(self.top_frame, text="label 2", background='red', image=self.image_fg)
        self.label3 = tk.Label(self.top_frame, text="label 3", background='green' )

        self.label1.pack(side='left', expand=True, fill='both')
        self.label2.pack(side='left', expand=True, fill='both')
        self.label3.pack(side='left', expand=True, fill='both') 

        self.button_bg = tk.Button(self.bottom_frame, text="Select Background", font=('Arial', 12), command=self.select_background)
        self.button_fg = tk.Button(self.bottom_frame, text="Select Foreground", font=('Arial', 12), command=self.select_foreground)
        self.button_save = tk.Button(self.bottom_frame, text="Save Image", font=('Arial', 12), command=self.save_image) 
         
        self.button_bg.pack(padx=5, pady=5, side='left', expand=True, fill='both')
        self.button_fg.pack(padx=5, pady=5, side='left', expand=True, fill='both')
        self.button_save.pack(padx=5, pady=5, side='left', expand=True, fill='both')

        self.top_frame.pack(fill='both')
        self.bottom_frame.pack(fill='both')

        self.root.columnconfigure(0, weight=2)
        self.root.columnconfigure(1, weight=2)
        self.root.columnconfigure(2, weight=3)

        self.frame = tk.Frame(self.root, width=300, height=300)
        self.frame.place(anchor='center', relx=0.5, rely=0.5)    
        self.frame.pack()   
          
       
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.aboutus = tk.Menu(self.menubar, tearoff=0)
         

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.aboutus, label="About")

        self.filemenu.add_command(label="Close", command=exit)
        self.aboutus.add_command(label="About the App", command=self.about_us )

        self.root.config(menu=self.menubar) 
 
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))   
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))
    
    def shortcut(self, event):  
        if  event.state == 4 and event.keysym == 'Return':
            self.show_message()

    def on_closing(self):
        print("Hello World!")
        self.root.destroy()

    def print_message(self):
        print("Carpe diem!")

    def select_background(self):
        file_path = filedialog.askopenfilename()
        print(file_path)        

        self.img_bg = Image.open(file_path).convert("RGBA")
        res2 = self.img_bg.resize((200, 200))
        self.image_bg = ImageTk.PhotoImage(res2)
 
        self.label1.config(image = self.image_bg)

    def select_foreground(self):
        file_path = filedialog.askopenfilename()
        print(file_path)        

        self.img_fg = Image.open(file_path).convert("RGBA")
        res = self.img_fg.resize((200, 200))
        self.image_fg = ImageTk.PhotoImage(res)

        self.label2.config(image = self.image_fg)
        

    def change_bg(self):
        self.label1.config(background='red')

    def save_image(self):
        print("Saving image")
        base = self.img_bg
        img = self.img_fg
        base.paste(img, (0, 0), img)

        self.base_tk = ImageTk.PhotoImage(base)
        
        self.label3.config(image=self.base_tk)
  
        base.save("superimposed.png") 


    def about_us(self):

        messagebox.showinfo(title="About the App", message=
            "You wanna join a video call but too conscious of the camera Worry no more, your static avatar is here to help you stay present on those mundane meetings. Created by marketpanda, architect. Glory to God to the highest"
        )
        

MyGUI()