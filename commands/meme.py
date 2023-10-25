from lib import reddit

def random():
    memeobj = reddit.random()
    memeobj.download()
    info = []
    info.append(memeobj.getTitle())
    post_info = (
        f"Subreddit: r/{memeobj.getSubreddit()} "
        f"Upvotes: {memeobj.getUpvotes()}"
    )
    info.append(post_info)
    return info

def validate(sub):
    subDB = ["memes", "meme", "dankmemes", "me_irl", "programmerhumor", "mildlyinfuriating", "mildlyinteresting", "facepalm"]
    if sub not in subDB:
        return False
    else:
        return True

def subreddit(sub):
    memeobj = reddit.subreddit(sub)
    memeobj.download()
    info = []
    info.append(memeobj.getTitle())
    info.append("Upvotes: " + str(memeobj.getUpvotes()))
    return info