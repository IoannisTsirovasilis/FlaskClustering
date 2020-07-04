"""
This script runs the FlaskClustering application using a development server.
"""

from os import environ
from FlaskClustering import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '9000'))
    except ValueError:
        PORT = 9000
    app.run(HOST, 9000)
