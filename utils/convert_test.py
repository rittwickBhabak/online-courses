import os 
dirs = list(filter(lambda x: os.path.isdir(x), os.listdir()))

CWD = os.getcwd()

def convert(x):
    x = x.split(' ')[0]
    if x.endswith('.'):
        return float(x[:-1])
    else:
        return float(x)

for dir in dirs:
    contents = os.listdir(dir)

    for content in contents:
        x = convert(content)
        print(x)