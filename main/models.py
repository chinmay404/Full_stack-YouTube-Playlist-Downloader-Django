from django.db import models
from pytube import YouTube
from pytube import Playlist


class HashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_val
        else:
            return "No record found"

        def __str__(self):
            return "".join(str(item) for item in self.hash_table)


hash_table = HashTable(8)


global yt
response_dict = {}
urk = None
# Create your models here.


def link_info(url):
    yt = YouTube(url)
    title = yt.title
    tumb_image = yt.thumbnail_url
    discription = yt.description[:70]
    response_dict = {
        "title": title,
        "thubnail": tumb_image,
        "description": discription
        
    }

    return response_dict


def quality_resolver(url, q):
    yt = YouTube(url)

    download = yt.streams.filter(progressive=True, file_extension='mp4',filter = q).desc().first()
    return download
    # download_via_request()

