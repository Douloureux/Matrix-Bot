from lib import rss
import random
import os
import pathlib

def pull(url):
    n = rss.parse(url)
    titles = []
    links = []
    for i in n.entries[0:]:
        titles.append(i.title)
        links.append(i.link)
    return [titles, links]

def resp(reddit):
    indices = random.sample(range(0, len(reddit[0]) - 1), 10)
    headlines = []
    links = []
    for i in indices:     
        headlines.append(reddit[0][i])
        links.append(reddit[1][i])
    return '\n\n'.join([f"[{headlines}]({links})" for headlines,links in zip(headlines, links)])

def any_reddit(subreddit):
    try:
        x = resp(pull(f"https://old.reddit.com/r/{subreddit}.rss?limit=50"))
        return x
    except:
        return "Subreddit does not exist."

def yt_subscribe(channel_id, user_id) -> str:
    file = f"db/youtube/channels/{channel_id}"
    file2 = f"db/youtube/videos/{channel_id}"

    def already_subbed() -> bool:
        lines = open(file, 'r').readlines()
        for line in lines:
            if line.strip() == user_id:
                return True
            else:
                return False
    
    if not os.path.isfile(file):
        try:
            d = rss.YoutubeChannel(id=channel_id)
            pathlib.Path(file).touch()
            pathlib.Path(file2).touch()
            with open(file, 'w') as i:
                i.write(user_id + "\n")
                i.close()
            with open(file2, 'w') as i:
                i.writelines("null")
                i.close()
            return f"Successfully subscribed to {d.author()}."
        except:
            os.remove(file)
            os.remove(file2)
            return "Invalid channel ID given."
    
    else:
        d = rss.YoutubeChannel(id=channel_id)
        if not already_subbed():
            with open(file, 'a') as i:
                i.writelines(user_id + "\n")
                i.close()
            return f"Successfully subscribed to {d.author()}."
        else:
            return f"You are already subscribed to {d.author()}."
