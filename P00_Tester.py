value = [0, 1, 1, 0, 0, 0, 0, 0, 0]

while True:
    # value = ready()
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