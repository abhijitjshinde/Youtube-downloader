import pytube
from kivy.app import App

def download_video(url, resolution):
    app = App.get_running_app()
    print('i am entered')
    itag = choose_resolution(resolution)
    print('i am at 2nd')
    video = pytube.YouTube(url)
    print('i am at 3rd')    
    stream = video.streams.get_by_itag(itag)
    print('i am at 4th')    
    if stream == None :
        print('i am in none if block')
        msg = "Select Another Quality"
        app.error(msg)
        
    if stream != None and stream.itag==137:
        msg="No Audio Available"
        app.error(msg)
        stream.download()
        
    
    print('i am at end')
    if stream != None:
        stream.download()
        return stream.default_filename

def download_videos(urls, resolution):
    for url in urls:
        download_video(url, resolution)

def download_playlist(url, resolution):
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls, resolution)

def choose_resolution(resolution):
    if resolution in ["Low", "360", "360p"]:
        itag = 18
    elif resolution in ["Medium", "720", "720p", "hd"]:
        itag = 22
    elif resolution in ["High", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    elif resolution in ["very high", "2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag


def input_links():
    print("Enter the links of the videos (end by entering 'STOP'):")

    links = []
    link = ""

    while link != "STOP" and link != "stop":
        link = input()
        links.append(link)

    links.pop()

    return links