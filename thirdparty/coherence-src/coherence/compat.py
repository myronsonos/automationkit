
def bytes_cast(sval):
    if isinstance(sval, str):
        sval = sval.encode('utf-8')
    return sval

def str_cast(sval):
    if isinstance(sval, bytes):
        sval = sval.decode('utf-8')
    return sval
