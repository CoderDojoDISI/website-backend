FROM python:3-onbuild

EXPOSE 8001

COPY ./ /usr/src/app

CMD ["gunicorn", "app:app", "--log-file=-", "-b", "0.0.0.0:8001"]