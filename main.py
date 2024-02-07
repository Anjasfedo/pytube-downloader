import tkinter  # Import the tkinter module for GUI creation.
import customtkinter  # Import a custom tkinter module.
from pytube import YouTube  # Import the YouTube class from the pytube module.

def download_vid():  # Define a function to download a video.
    yt_link = link.get()  # Get the YouTube link from the entry field.
        
    youtube_obj = YouTube(yt_link, on_progress_callback=on_progress)  # Create a YouTube object with the link.

    video = youtube_obj.streams.get_highest_resolution()  # Get the highest resolution stream of the video.
    
    title.configure(text=youtube_obj.title, text_color="white")  # Set the title label with the video's title.
    
    downloaded_label.configure(text="")  # Clear any previous download status label.
    
    try:  # Try downloading the video.
        video.download()  # Download the video.
        downloaded_label.configure(text="Downloaded")  # Set the download status label to "Downloaded".
    except:  # If an error occurs during download.
        downloaded_label.configure(text="Download Error", text_color="red")  # Set the download status label to indicate an error.
    
def on_progress(stream, chunk, byte_remaining):  # Define a function to update download progress.
    total_size = stream.filesize  # Get the total size of the video.
    
    bytes_downloaded = total_size - byte_remaining  # Calculate the bytes downloaded so far.

    percentage = bytes_downloaded / total_size * 100  # Calculate the percentage of download completion.
    
    percent = str(int(percentage))  # Convert the percentage to a string.

    progress_label.configure(text=f"{percent}%")  # Update the progress label with the percentage.
    
    progress_bar.set(float(percentage) / 100)  # Update the progress bar with the percentage.

customtkinter.set_appearance_mode("System")  # Set the appearance mode of the custom tkinter.
customtkinter.set_default_color_theme("blue")  # Set the default color theme of the custom tkinter.

app = customtkinter.CTk()  # Create a custom tkinter application instance.
app.geometry("720x480")  # Set the dimensions of the application window.
app.title("Youtube Downloader")  # Set the title of the application window.

title = customtkinter.CTkLabel(app, text="Insert youtube link")  # Create a label for inserting YouTube link.
title.pack(padx=10, pady=10)  # Pack the label into the application window.

url = tkinter.StringVar()  # Create a tkinter string variable.
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url)  # Create an entry field for YouTube link.
link.pack()  # Pack the entry field into the application window.

downloaded_label = customtkinter.CTkLabel(app, text="")  # Create a label for download status.
downloaded_label.pack()  # Pack the download status label into the application window.

progress_label = customtkinter.CTkLabel(app, text="0%")  # Create a label for download progress.
progress_label.pack()  # Pack the progress label into the application window.

progress_bar = customtkinter.CTkProgressBar(app, width=400)  # Create a progress bar.
progress_bar.set(0)  # Set the initial value of the progress bar.
progress_bar.pack(padx=10, pady=10)  # Pack the progress bar into the application window.

download_btn = customtkinter.CTkButton(app, text="Download", command=download_vid)  # Create a download button.
download_btn.pack(padx=10, pady=10)  # Pack the download button into the application window.

app.mainloop()  # Run the application main loop.
