FROM python:3.7

WORKDIR /opt/FlaskClustering
COPY . .
RUN pip install -r /opt/FlaskClustering/FlaskClustering/requirements.txt

EXPOSE 9000

CMD ["python", "/opt/FlaskClustering/FlaskClustering/runserver.py"]
