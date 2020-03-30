
def bytes_cast(sval):
    if isinstance(sval, str):
        sval = sval.encode('utf-8')
    return sval

def str_cast(sval):
    if isinstance(sval, bytes):
        sval = sval.decode('utf-8')
    return sval

def bytes_convert(obj):
    if isinstance(obj, str):
        obj = obj.encode('utf-8')
    elif isinstance(obj, dict):
        nobj = {}
        for ki, kv in obj:
            nobj[bytes_cast(ki)] = bytes_convert(kv)
        obj = nobj
    elif isinstance(obj, list):
        nobj = [lambda nv: bytes_convert(nv) for nv in obj]
        obj = nobj
    elif isinstance(obj, tuple):
        nobj = [lambda nv: bytes_convert(nv) for nv in obj]
        obj = nobj
    return obj
