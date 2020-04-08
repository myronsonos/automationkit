
from .views.home import view_home

def register_website_blueprints(app):

    app.add_url_rule('/', 'view_home', view_home)

    return
