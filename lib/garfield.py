import random
import os

def _get_comic():
    years = [random.randint(78, 99), random.randint(0, 20)]
    data = [str(random.choice(years)), str(random.randint(1,12)), str(random.randint(1,31))]

    i = 0
    for i in data:
        if len(i) == 1:
            data[i] = "0" + i
        i += 1 
    
    info = [f"./assets/comics/ga{data[0] + data[1] + data[2]}.gif", data[0], data[1], data[2]]
    return info
    
def get_info():
    exists = False
    while exists is False:
        i = _get_comic()
        exists = os.path.exists(i[0])
    return i