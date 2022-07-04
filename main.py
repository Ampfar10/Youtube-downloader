import youtube_dl
import pyfiglet
from colorama import init, Fore
init(autoreset=True)

print(Fore.RED + pyfiglet.figlet_format("Youtube",font ='larry3d')+ Fore.RESET)
print("             Youtube downloader version 2.0")
print("                Coded by Ampfar😀")
print("\n")

video_url = input("Enter Video Url: ")
type = input("Would you like to download Mp3or Mp4: ")


def download_ytvid_as_mp3():
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))
#download_ytvid_as_mp3()

def download_ytvid_as_mp4():
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{video_info['title']}.mp4"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))
#download_ytvid_as_mp3()

if type == "mp3":
    download_ytvid_as_mp3()
    video1 = input("Would you like to download mp4 as well: ")
    if video1 == "yes" or video1 == "yes":
        download_ytvid_as_mp4()
    elif video1 == "no" or video1 == "No":
        print("Goodbye!!")
        pass

elif type == "mp4":
    download_ytvid_as_mp4()
    music1 = input("Would you like to download mp3 as well: ")
    if music1 == "yes" or music1 == "yes":
        download_ytvid_as_mp3()
    elif music1 == "no" or music1 == "No":
        print("Goodbye!!")
        pass

