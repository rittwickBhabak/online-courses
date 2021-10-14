import os, time, datetime, json 

def convert(x):
    try:
        x = x.split(' ')[0]
        if x.endswith('.'):
            return float(x[:-1])
        else:
            return float(x)
    except Exception as e:
        print(f"ERROR AT {x}")
        print(str(e))
        filename = str(datetime.datetime.now()).replace(":", '-')
        with open(f"{filename}.txt", 'w') as f:
            f.write(f"Error at {x}")
        return -1


dirs = list(filter(lambda x: os.path.isdir(x), os.listdir()))
data = {}

for dir in dirs:
    contents = os.listdir(dir)
    data[dir] = {'videos': [], 'slno': convert(dir)}
    for content in contents:
        data[dir]['videos'].append({'title': content, 'slno': convert(content)})


for key, value in data.items():
    videos = value['videos']
    value['videos'] = sorted(videos, key=lambda x: x['slno'])

data = dict(sorted(data.items(), key=lambda x: x[1]['slno']))


index = ''
for key, value in data.items():
    index = index + f"{key}\n"
    for video in value['videos']:
        index = index + f"\t{video['title']}\n"

course = input('Enter Course Name: ')
index = f"{course}\n" + index 
with open(f"{course}.txt", 'w') as f:
    f.write(index)

