
import os

from akit.environment.context import Context

from flask import Response

context = Context()

DIR_RESULTS = os.path.expanduser(context.lookup("/environment/configuration/paths/results"))

MIME_TYPES = {
    ".css": "text/css",
    ".html": "text/html",
    ".log": "text/plain",
    ".js": "application/javascript",
    ".json": "application/json",
    ".jsos": "application/json",
    ".txt": "text/plain"
}

def view_logstore(leafpath):
    full_path = DIR_RESULTS.rstrip("/") + "/" + leafpath
    base, ext = os.path.splitext(full_path)

    content = None
    with open(full_path, 'r') as cf:
        content = cf.read()

    mimetype = MIME_TYPES[ext]
    response = Response(content, mimetype=mimetype)

    return response
