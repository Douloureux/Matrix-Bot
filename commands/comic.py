from lib import xkcd, garfield

def write_file(num):
    file = open("assets/comic.txt", "w")
    file.write(str(num))
    file.close()

def read_file() -> str:
    file = open("assets/comic.txt").read()
    return str(file)

def latest() -> str:
    x = xkcd.getLatestComic()
    x.download(output='assets/', outputFile="temp.jpg")
    write_file(x.getNumber())
    return x.altText

def random() -> str:
    x = xkcd.getRandomComic()
    x.download(output='assets/', outputFile="temp.jpg")
    write_file(x.getNumber())
    return x.altText

def number(comic_num):
    if int(comic_num) > xkcd.getLatestComicNum():
        return "Invalid comic number given"
    else:
        xkcd.getComic(comic_num, silent=True).download(output='assets/', outputFile="temp.jpg")
        write_file(comic_num)
        return "OK"

def explain() -> str:
    link = "https://explainxkcd.com/"
    return link + read_file()

def get_garfield() -> str:
    return garfield.get_info()