import os 

def replace(old):
    return old.replace('--- [ FreeCourseWeb.com ] ---', '')

def path(dirs):
    return os.path.join(*dirs)

dirs = list(filter(lambda x: os.path.isdir(x), os.listdir()))

CWD = os.getcwd()

for dir in dirs:
    contents = os.listdir(dir)

    for content in contents:
        src = path([CWD, dir, content])
        dst = path([CWD, dir, replace(content)])

        os.rename(src, dst)