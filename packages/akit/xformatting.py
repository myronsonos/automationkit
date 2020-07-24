

from io import StringIO

def indent_lines(msg, level, indent=4):
    
    # Split msg into lines keeping the line endings
    msglines = msg.splitlines(True)

    pfx = " " * (level * indent)

    indented = StringIO()
    for nxtline in msglines:
        indented.write(pfx)
        indented.write(nxtline)
    
    return indented.value()
