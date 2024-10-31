import CHaser
import random

def ready():
    return cl.get_ready()

def look(d):
    if d == 1:
        value = cl.look_up()
    elif d == 3:
        value = cl.look_left()
    elif d == 5:
        value = cl.look_right()
    elif d == 7:
        value = cl.look_down()

    if value.count(takara) >= 1:
        return d
    else:
        return tekitou()

def walk(d):
    if value[d] == kabe:
        walk(tekitou())
    else :
        if d == 1:
            cl.walk_up()
        elif d == 3:
            cl.walk_left()
        elif d == 5:
            cl.walk_right()
        elif d == 7:
            cl.walk_down()

def put(d):
    if d == 1:
        cl.put_up()
    elif d == 3:
        cl.put_left()
    elif d == 5:
        cl.put_right()
    elif d == 7:
        cl.put_down()

def search(d):
    if d == 1:
        value = cl.search_up()
    elif d == 3:
        value = cl.search_left()
    elif d == 5:
        value = cl.search_right()
    elif d == 7:
        value = cl.search_down()

    if value.count(takara) >= 2:
        return d
    else:
        return tekitou()

def tekitou():
    muki = [1,3,5,7]
    return muki[random.randint(0,3)]    


if __name__ == "__main__":
    cl = CHaser.Client()
    teki = 1
    kabe = 2
    takara = 3

    #ここから下にプログラムを書いてください。
    
    muki = 0
    while True:

        value = ready()
        muki = search(tekitou())
        value = ready()
        walk(tekitou())