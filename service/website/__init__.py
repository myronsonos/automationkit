
from .views.devices import view_devices
from .views.home import view_home
from .views.jobs import view_jobs
from .views.results import view_results


def register_website_blueprints(app):

    app.add_url_rule('/', 'view_home', view_home)

    app.add_url_rule('/devices', 'view_devices', view_devices)
    app.add_url_rule('/jobs', 'view_jobs', view_jobs)
    app.add_url_rule('/results', 'view_results', view_results)

    return
