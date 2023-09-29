FROM python:3.10
COPY mian.py .
RUN pip install Flask
ENV FLASK_APP=mian.py
CMD ["flask", "run", "--host=0.0.0.0"]
