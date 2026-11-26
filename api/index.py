import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from app import app as flask_app

_orig_wsgi = flask_app.wsgi_app
def _wrapper(environ, start_response):
    path = environ.get('PATH_INFO', '')
    if path.startswith('/api/index.py'):
        environ['PATH_INFO'] = path[len('/api/index.py'):] or '/'
    elif path.startswith('/api/index'):
        environ['PATH_INFO'] = path[len('/api/index'):] or '/'
    return _orig_wsgi(environ, start_response)

flask_app.wsgi_app = _wrapper
app = flask_app
