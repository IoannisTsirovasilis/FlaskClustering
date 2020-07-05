"""
This script runs the FlaskClustering application using a development server.
"""

from os import environ
from FlaskClustering import app

if __name__ == '__main__':
    app.run("0.0.0.0", 9000)
