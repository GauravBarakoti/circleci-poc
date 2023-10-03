FROM python:3.10
ADD Flask_application.py .
RUN pip install Flask
ENV FLASK_APP=Flask_application.py
CMD ["flask", "run"]
