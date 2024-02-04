import tkinter 
import customtkinter
from pytube import YouTube

def download_vid():
    yt_link = link.get()
        
    youtube_obj = YouTube(yt_link)

    youtube_obj = youtube_obj.streams.get_highest_resolution()
    
    try:
        youtube_obj.download()
    except:
        print("Invalid Youtube link")
    
    print("Downloaded")
        


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Insert youtube link")
title.pack(padx=10, pady=10)

url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url)
link.pack()

download_btn = customtkinter.CTkButton(app, text="Download", command=download_vid)
download_btn.pack(padx=10, pady=10)

app.mainloop()
