import tkinter 
import customtkinter
from pytube import YouTube

def download_vid():
    yt_link = link.get()
        
    youtube_obj = YouTube(yt_link, on_progress_callback=on_progress)

    video = youtube_obj.streams.get_highest_resolution()
    
    title.configure(text=youtube_obj.title, text_color="white")
    
    downloaded_label.configure(text="")
    
    try:
        video.download()
        downloaded_label.configure(text="Downloaded")
    except:
        downloaded_label.configure(text="Download Error", text_color="red")
    
def on_progress(stream, chunk, byte_remaining):
    total_size = stream.filesize
    
    bytes_downloaded = total_size - byte_remaining

    percentage = bytes_downloaded / total_size * 100
    
    percent = str(int(percentage))

    progress_label.configure(text=f"{percent}%")
    
    progress_bar.set(float(percentage) / 100)
    

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

downloaded_label = customtkinter.CTkLabel(app, text="")
downloaded_label.pack()

progress_label = customtkinter.CTkLabel(app, text="0%")
progress_label.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

download_btn = customtkinter.CTkButton(app, text="Download", command=download_vid)
download_btn.pack(padx=10, pady=10)

app.mainloop()
