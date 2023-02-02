# from django.db import models
# from pytube import YouTube
# from pytube import Playlist
import pytube  
import requests
import json


# class HashTable:

#     def __init__(self, size):
#         self.size = size
#         self.hash_table = self.create_buckets()

#     def create_buckets(self):
#         return [[] for _ in range(self.size)]

#     def set_val(self, key, val):
#         hashed_key = hash(key) % self.size
#         bucket = self.hash_table[hashed_key]

#         found_key = False
#         for index, record in enumerate(bucket):
#             record_key, record_val = record
#             if record_key == key:
#                 found_key = True
#                 break
#         if found_key:
#             bucket[index] = (key, val)
#         else:
#             bucket.append((key, val))

#     def get_val(self, key):
#         hashed_key = hash(key) % self.size
#         bucket = self.hash_table[hashed_key]

#         found_key = False
#         for index, record in enumerate(bucket):
#             record_key, record_val = record
#             if record_key == key:
#                 found_key = True
#                 break
#         if found_key:
#             return record_val
#         else:
#             return "No record found"

#         def __str__(self):
#             return "".join(str(item) for item in self.hash_table)


# # yt = None
# # Create your models here.
# hash_table = HashTable(8)


# def quality_resolver(url):
#     yt = YouTube(url)
#     title = yt.title
#     tumb_image = yt.thumbnail_url
#     hash_table.set_val('144p',yt.streams.filter(res="144p").first())
#     hash_table.set_val( '240p',yt.streams.filter(res="240p").first())
#     hash_table.set_val( '360p',yt.streams.filter(res="360p").first())
#     hash_table.set_val( '720p',yt.streams.filter(res="720p").first())
#     hash_table.set_val('480p' ,yt.streams.filter(res="480p").first())
#     hash_table.set_val('1080p',yt.streams.filter(res="1080p").first() )
#     print(title,tumb_image,hash_table)
#     print(hash_table.get_val('720p'))


# quality_resolver("https://youtu.be/EAYlckSaviI")
# # download_request_quality(yt)


class pytube.YouTube(
    url: str, on_progress_callback: Optional[Callable[[Any, bytes, int], None]]=None,
     on_complete_callback: Optional[Callable[[Any, Optional[str]], None]]=None,
      proxies: Dict[str, str]=None,
       use_oauth: bool=False,
        allow_oauth_cache: bool=True)
