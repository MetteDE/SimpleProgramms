import pathlib 
import os 


def get_path():
    # get the Video folder path
    video_path = pathlib.Path.home() / 'Videos\YT_Downloader'
    isExist = os.path.exists(video_path)

    # creates new folder in Video if not already there
    if not isExist: 
        os.makedirs(F"{video_path}")
        print("Created new directory!")
    return video_path

