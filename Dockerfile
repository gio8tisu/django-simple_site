FROM python:3
RUN pip3 install django
COPY . /simple_site
WORKDIR /simple_site

EXPOSE 8080
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0:8080"]
