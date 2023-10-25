import json
import urllib.request
import os

API_URL = 'https://meme-api.com/gimme'

class Post(object):
    def __init__(self, subreddit, title, upvotes, url):
        self.subreddit = subreddit
        self.title = title
        self.upvotes = upvotes
        self.url = url
    
    def __str__(self):
        return (
            f"{self.subreddit}\n"
            f"{self.title}\n"
            f"{self.upvotes}\n"
            f"{self.url}\n"
        )
    
    def download(self, output="assets/", outputFile="meme.jpg"):
        req = urllib.request.Request(self.url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.0.0"
            })
        image = urllib.request.urlopen(req).read()
        output = os.path.join(output, outputFile)
        meme = open(output, 'wb')
        meme.write(image)
        meme.close()
        return
    
    def getTitle(self):
        return self.title
    
    def getSubreddit(self):
        return self.subreddit
    
    def getUpvotes(self):
        return self.upvotes

def _get_api_json(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.0.0"
        })
    return json.loads(urllib.request.urlopen(req).read().decode('utf-8'))

def _parse_json(json):
    meme = Post(
        subreddit=json['subreddit'],
        title=json['title'],
        upvotes=json['ups'],
        url=json['url']
    )
    return meme

def random():
    json = _get_api_json(API_URL)
    return _parse_json(json)

def subreddit(sub):
    json = _get_api_json(API_URL + f"/{sub}")
    return _parse_json(json)