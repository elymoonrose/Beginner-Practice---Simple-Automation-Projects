# This will allow you to download any YouTube video at the highest quality possible
# to your computer. Just run the code in your terminal, copy and paste a YouTube URL and hit enter.
# Don't forget to install the Pytube package in case you haven't already.

import tkinter as tk
from tkinter import filedialog
from pytube import YouTube


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded succesfully!")
    except Exception as e:
        print(e)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
        return folder


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Download started...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")
