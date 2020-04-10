import os

from flask import render_template

def view_devices():
    template = "devices_full.html"

    username = "myron.walker"

    return render_template(template, username=username )
