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
    value = ready()

    while True:
        value = ready()
        get_1 = 1 in value
        get_2 = 2 in value
        get_3 = 3 in value
        get_0 = 0 in value

        print(value)
        print(f"get_1: {get_1}")
        print(f"get_2: {get_2}")
        print(f"get_3: {get_3}")
        print(f"get_0: {get_0}")
    
    # ------------------------------- 動作に関して -------------------------------

        if get_1 == True:
            if value[2] == 1:
                print("1-上")
                continue
            elif value[4] == 1:
                print("1-左")
                continue
            elif value[6] == 1:
                print("1-右")
                continue
            elif value[8] == 1:
                print("1-下")
                continue

        if get_3 == True:
            if value[2] == 3:
                print("3-上")
                continue
            elif value[4] == 3:
                print("3-左")
                continue
            elif value[6] == 3:
                print("3-右")        
                continue
            elif value[8] == 3:
                print("3-下")
                continue

        if get_2 == True:
            if value[2] != 2:
                print("NOT_2-上")
                continue
            elif value[4] != 2:
                print("NOT_2-左")
                continue
            elif value[6] != 2:
                print("NOT_2-右")
                continue
            elif value[8] != 2:
                print("NOT_2-下")
                continue

        if get_0 == True:
            if value[2] == 0:
                print("0-上")
                continue
            elif value[4] == 0:
                print("0-左")
                continue
            elif value[6] == 0:
                print("0-右")
                continue
            elif value[8] == 0:
                print("0-下")
                continue
        print("END")