from json import *

def load_jsonl(file, **kw):
    with open(file, 'r', newline='\n') as rfile:
        data = [loads(x) for x in rfile.readlines()]
    return data

def loads_jsonl(s, **kw):
    return [loads(x, **kw) for x in s.split('\n')]

def dump_jsonl(data, file, **kw):
    try:
        iter(data)
    except:
        raise TypeError("data should be an iterable")
    with open(file, 'w') as wfile:
        wfile.writelines(dumps(x, **kw)+'\n' for x in data)

def dumps_jsonl(data, **kw):
    try:
        iter(data)
    except:
        raise TypeError("data should be an iterable")
    return "\n".join(dumps(x **kw) for x in data)