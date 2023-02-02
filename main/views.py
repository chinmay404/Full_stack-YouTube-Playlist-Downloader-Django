from django.shortcuts import render
from main.models import *
from main.forms import input_url
from django.http import HttpResponse, FileResponse
from wsgiref.util import FileWrapper
from pytube import YouTube, Playlist
import os
from django.shortcuts import redirect


# import re
# from pytube import Playlist

# YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
# DOWNLOAD_DIR = 'D:\\Users\\Jean-Pierre\\Downloads'

# playlist = Playlist('https://www.youtube.com/playlist?list=PLzwWSJNcZTMSW-v1x6MhHFKkwrGaEgQ-L')

# # this fixes the empty playlist.videos list
# playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

# print(len(playlist.video_urls))

# for url in playlist.video_urls:
#     print(url)

# # physically downloading the audio track
# for video in playlist.videos:
#     audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
#     audioStream.download(output_path=DOWNLOAD_DIR)


def home(request):
    return render(request, 'Home.html', response_dict)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def playlist(request):
    return render(request, 'playlist.html')


def dowload_page(request):
    response_dict = {}
    global url
    url = request.GET['url']
    if url.__contains__('playlist'):
        p = Playlist(url)
        response_dict = {"title": p.title, }
        return render(request, 'playlist_download_page.html', response_dict)
    else:
        response_dict = link_info(url)
        yt = YouTube(url)
        resol = []
        aud = []
        stream_all = yt.streams.all()
        for i in stream_all:
            if i.resolution!= 'None':
                resol.append(i.resolution)
        audio = yt.streams.filter(only_audio=True).all()
        for i in audio:
            aud.append(i.abr)
        resol = list(dict.fromkeys(resol))
        aud = list(dict.fromkeys(aud))
        response_dict['resol'] = resol
        response_dict['audio'] = aud
        return render(request, 'download_page.html', response_dict)


def download(request, q):
    global url
    print(url)
    base_dir = os.path.expanduser("~")
    down_dir = base_dir + '/download'
    if q == 'all_video':
        p = Playlist(url)
        for video in p.videos:
            video.streams.first().download()
    elif q == 'all_audio':
        p = Playlist(url)
        for video in p.videos:
            video.streams.filter(only_audio=True).first().download(down_dir)
    else:
        yt = YouTube(url)
        if q.__contains__('kbps'):
            audio = yt.streams.filter(only_audio=True , abr=q).first().download()
        else:
            video = yt.streams.filter(res=q).desc().first().download()
    return HttpResponse("Download Complete :)")
