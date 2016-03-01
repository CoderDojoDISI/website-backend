FROM python:3-onbuild

EXPOSE 8001

COPY ./ /usr/src/app

ENV PYTHONUNBUFFERED TRUE

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8001"]
