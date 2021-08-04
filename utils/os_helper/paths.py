def get_last_component(string:str):
    Broken = string.split('/')
    length = len(Broken)

    return Broken[length - 1]

