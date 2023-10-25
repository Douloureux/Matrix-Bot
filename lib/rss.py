import feedparser

def parse(url):
    d = feedparser.parse(url)
    return d

class YoutubeVideo(object):
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def url(self) -> str:
        return "https://www.youtube.com/watch?v=" + self.id

class YoutubeChannel(object):
    def __init__(self, id):
        self.id = id
        self.feed = feedparser.parse(self._feed())

    def _feed(self):
        return "https://www.youtube.com/feeds/videos.xml?channel_id=" + self.id
    
    def author(self) -> str:
        return self.feed.entries[0].author

    def latestVideo(self) -> YoutubeVideo:
        vid = self.feed.entries[0].yt_videoid
        title = self.feed.entries[0].title
        return YoutubeVideo(
            id=vid,
            title=title
        )