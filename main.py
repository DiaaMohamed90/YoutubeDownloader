import customtkinter as ct 
from tkinter.filedialog import askdirectory
from pytube import YouTube
import os 
from tkinter import * 
from PIL import Image , ImageTk
import threading
from tkinter import messagebox
from tkinter import ttk

PATH = os.path.dirname(os.path.realpath(__file__))
def load_image(path,image_size):
    return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size,image_size)))

def select_path():
    global path_name
    path_name = askdirectory()
def check_what_to_download():
    if type_menu.get() == 'Audio':
        print('Audio Selected')
        download_best_audioquality()
    if type_menu.get()=='Video':
        print('Video Selected')
        download_best_videoquality()
def download_best_audioquality():
    progressbar.pack(pady=12,padx=10)
    progressbar.start()
    yt = YouTube(url_link_entry.get())
    best_quality_audio = yt.streams.filter(only_audio=True).desc().first()
    best_quality_audio.download(path_name)
    messagebox.showinfo('Done','Finished')
    progressbar.stop()
def download_best_videoquality():
    progressbar.pack(pady=12,padx=10)
    progressbar.start()
    yt = YouTube(url_link_entry.get())
    best_quality_video_resulotions = yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc()
    best_quality_video_resulotions.download(path_name)
    messagebox.showinfo('Done','Finished')
    progressbar.stop()
ct.set_appearance_mode("light") 
app = ct.CTk()
app.geometry("400x580")
app.resizable(False,False)
app.title("Youtube Downloader")
app.iconbitmap('youtube.ico')
frame_1 = ct.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

main_image = load_image('/images/youtube.png',20)
main_image_label = ct.CTkLabel(frame_1,image=main_image,text='')
main_image_label.pack(pady=6,padx=10)

label_1 = ct.CTkLabel(master=frame_1, justify=LEFT,text="Youtube Downloader..",font=('calbri',8,'bold'))
label_1.pack(pady=3, padx=10)

url_link_entry = ct.CTkEntry(master=frame_1,justify=LEFT,width=400,placeholder_text='Enter Youtube Url Here',font=('calbri',10,'bold'))
url_link_entry.pack(pady=12,padx=10)


choose_path_btn = ct.CTkButton(frame_1,text="Choose Path",width=200,height=20,fg_color='green',font=('calbri',10,'bold'),command=threading.Thread(target=select_path).start)
choose_path_btn.pack(pady=12,padx=10)



type_menu = ct.CTkOptionMenu(frame_1, values=["Audio", "Video"],width=160,font=('calbri',10,'bold'))
type_menu.pack(pady=12, padx=10)





#loadingLabel = ct.CTkLabel(frame_1, text="Loading...", text_font=("Agency FB", 30))
#loadingPercent = ct.CTkLabel(frame_1, text="0", fg="green", text_font=("Agency FB", 30))
progressbar = ttk.Progressbar(frame_1, orient="horizontal", length=500, mode='indeterminate')
download_btn = ct.CTkButton(frame_1,text="Download",fg_color='red',font=('calbri',10,'bold'),command=threading.Thread(target=check_what_to_download).start)
download_btn.pack(pady=20,padx=10)

authlabel = ct.CTkLabel(frame_1,text='Made By Diaa Mohamed',font=('calbri',12,'bold'))
authlabel.pack(side=BOTTOM)
app.mainloop()


