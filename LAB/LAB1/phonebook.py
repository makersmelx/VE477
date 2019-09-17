dict = {}
while True:
    str = input().split()
    if (str[0] == 'quit'):
        break
    elif (str[0] == 'add'):
        dict[str[1]] = int(str[2])
    elif (str[0] == 'edit'):
        if str[1] in dict:
            dict[str[1]] = int(str[2])
    elif (str[0] == 'remove'):
        if str[1] in dict:
            del dict[str[1]]
    print(dict)
