def get_last_component(string:str):
    Broken = string.split('/')
    length = len(Broken)

    return Broken[length - 1]

def basePath(URL):
    if URL.endswith('/'):
        URL = URL[:-1]

    Broken = URL.split('/')
    length = len(Broken)

    LastItem = Broken[length - 1]
    NewPath = ''

    for path in Broken:
        Bad = [LastItem, '']

        continuee = False

        for b in Bad:
            if path == b:
                continuee = True

        if continuee:
            continue


        NewPath = NewPath + '/' + path

    return NewPath
