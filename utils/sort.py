import json 

with open('json/data.json', 'r') as f:
    data = json.loads(f.read()) 

def sort_dict(data):
    data = dict(sorted(data.items(), key=lambda x: x[1]['slno']))

    for key, value in data.items():
        value['videos'] = dict(sorted(value['videos'].items(), key=lambda x: x[1]['slno']))
    
    return data 

with open('x.json', 'w') as f:
    f.write(json.dumps(sort_dict(data)))