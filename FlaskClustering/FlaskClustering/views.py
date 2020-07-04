"""
Routes and views for the flask application.
"""

import io, base64
from datetime import datetime
from flask import render_template, Response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from random import random
import numpy as np
from FlaskClustering import app
from PIL import Image
from sklearn.cluster import KMeans

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    size = int(request.args.get('size'))
    clusters = int(request.args.get('clusters'))
    fig = create_figure(clusters, size)
    fig.savefig('/test.png')
    output = io.BytesIO()
    pil_img = Image.open('/test.png', mode='r')
    pil_img.save(output, format='PNG') # convert the PIL image to byte array
    encoded_img = base64.encodebytes(output.getvalue()).decode('ascii') # encode as base64
    return encoded_img

def create_figure(clusters, size):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    for i in range(clusters):
        xscale = random()
        yscale = random()
        xloc = 20 * random() - 10
        yloc = 20 * random() - 10
        if i == 0:
            x = np.random.normal(loc=xloc, scale=xscale, size=size)
            y = np.random.normal(loc=yloc, scale=yscale, size=size)
            continue
        x = np.hstack([x, np.random.normal(loc=xloc, scale=xscale, size=size)])
        y = np.hstack([y, np.random.normal(loc=yloc, scale=yscale, size=size)])
    X = np.hstack((x.reshape(x.shape[0], 1),y.reshape(y.shape[0], 1)))
    kmeans = KMeans(n_clusters=clusters, random_state=0).fit(X)
    y_kmeans = kmeans.predict(X)
    axis.scatter(x, y, c=y_kmeans, s=50, cmap='viridis')

    centers = kmeans.cluster_centers_
    axis.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
    return fig
