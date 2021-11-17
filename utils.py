import numpy as np

def convertTuple(tup):
    # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

def a(text):
    chars = "\/*_{}[]()#+-!$';<>|:%=¸”&‚"
    text = text.replace('"', " ")
    text = text.replace(".", " ")
    text = text.replace("\n", "")
    text = text.replace("\t", " ")
    for c in chars:
        text = text.replace(c, " ")
    text = text.replace("'", " ")
    text = text.replace("filler", "'")
    text = text.replace("  ", " ")
    text = text.lower()
    text = text.encode("ascii", "ignore")
    text = text.decode()
    return text

def split(text):
    s = text.split(" ")
    return len(s)

def create_matrix(tokens, padding):
    n = len(tokens)
    matrix = np.zeros(shape=(n,padding),dtype='object')
    for i in range(0, n):
        value = (tokens[i])
        value = value.replace("[", "")
        value = value.replace("]", "") 
        value = value.split(", ")
        #print(len(value), value)
        for j in range(0, len(value)):
            matrix[i][j] = int(value[j])
    return matrix

